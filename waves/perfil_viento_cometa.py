"""
Cometa como anemómetro: solver inverso y perfil vertical de viento
--------------------------------------------------------------------

Este script extiende el modelo directo de equilibrio cometa + catenaria
(modelo_cometa_catenaria.py) para resolver el problema inverso:

    Dado lo que un volador puede medir en tierra con instrumentos simples
    -- tensión T0 y ángulo theta0 del hilo respecto al suelo, para varias
    longitudes de hilo desplegado -- estimar la velocidad del viento V y
    la altura real z en cada caso, y con eso reconstruir un perfil
    vertical de viento V(z).

Estructura del script
----------------------
1) Se reutilizan las funciones del modelo directo (fuerzas_aerodinamicas,
   resolver_equilibrio) desde modelo_cometa_catenaria.py.
2) Se simula un "experimento sintético": se asume un perfil de viento
   verdadero tipo ley de potencia, V(z) = V10 * (z/10)^alpha, y para cada
   longitud de hilo se resuelve el equilibrio de forma autoconsistente
   (iterando porque la velocidad del viento en la cometa depende de su
   altura, y la altura depende de la velocidad del viento). Esto genera
   las lecturas "medidas" T0, theta0 que tendría un volador real, con
   ruido opcional para imitar el error de instrumento.
3) Un solver inverso reconstruye, a partir de esas lecturas, la velocidad
   del viento y la altura en cada longitud de hilo -- sin usar el perfil
   verdadero, solo la física de equilibrio.
4) Se ajusta un perfil de potencia a los puntos (z_i, V_i) reconstruidos
   y se compara contra el perfil verdadero usado para generar los datos.

Notas sobre el solver inverso
------------------------------
De T0 y theta0 medidos se obtienen directamente H y V0 (geometría pura,
sin necesitar conocer la velocidad del viento):

    H  = T0 * cos(theta0)
    V0 = T0 * sin(theta0)

La altura real se calcula con las mismas fórmulas de catenaria del modelo
directo, y NO depende de ninguna hipótesis aerodinámica -- es un resultado
puramente geométrico una vez que se conoce H, V0 y la masa por metro del
hilo (mu).

La velocidad del viento, en cambio, sí requiere un modelo aerodinámico
(CL, CD, A conocidos de antemano, calibrados para esa cometa). Hay DOS
maneras de estimarla, una desde el arrastre y otra desde la sustentación:

    V_arrastre     = sqrt( 2H / (rho * CD * A) )
    V_sustentacion = sqrt( 2*(V_top + W_cometa) / (rho * CL * A) )

En un mundo ideal ambas coinciden. La diferencia entre ellas es un buen
diagnóstico de qué tan bien calibrados están CL y CD para esa cometa en
particular.
"""

import numpy as np
import matplotlib.pyplot as plt

from modelo_cometa_catenaria import fuerzas_aerodinamicas, resolver_equilibrio, G


# ---------------------------------------------------------------------
# 1) Perfil de viento "verdadero" (solo para generar datos sintéticos)
# ---------------------------------------------------------------------

def viento_ley_potencia(z, V_ref, alpha, z_ref=10.0):
    """Ley de potencia clásica de capa límite urbana: V(z) = V_ref*(z/z_ref)^alpha."""
    return V_ref * (z / z_ref) ** alpha


# ---------------------------------------------------------------------
# 2) Simulación autoconsistente del vuelo (genera las "mediciones")
# ---------------------------------------------------------------------

def simular_vuelo(longitud_hilo, perfil_viento, rho, CL, CD, A, W_cometa,
                   mu, g=G, max_iter=50, tol=1e-3):
    """
    Resuelve de forma autoconsistente el equilibrio para una longitud de
    hilo dada, cuando el viento depende de la altura (perfil_viento(z)).

    Itera: se propone una altura, se evalúa el viento a esa altura, se
    resuelve el equilibrio (que da una nueva altura), y se repite hasta
    que la altura converge.
    """
    if max_iter <= 0 or tol <= 0:
        raise ValueError("max_iter y tol deben ser positivos.")

    z = longitud_hilo * 0.7  # semilla inicial razonable
    convergio = False
    for _ in range(max_iter):
        V_local = perfil_viento(z)
        L, D = fuerzas_aerodinamicas(rho, V_local, CL, CD, A)
        res = resolver_equilibrio(L, D, W_cometa, mu, g, longitud_hilo)
        z_nuevo = res["altura"]
        if abs(z_nuevo - z) < tol:
            z = z_nuevo
            convergio = True
            break
        z = z_nuevo

    if not convergio:
        raise RuntimeError(
            f"El equilibrio no convergió en {max_iter} iteraciones "
            f"para {longitud_hilo:.1f} m de hilo."
        )

    # Recalcular con la altura convergida para que la velocidad de referencia
    # y la altura almacenadas pertenezcan al mismo estado del vuelo.
    V_local = perfil_viento(z)
    L, D = fuerzas_aerodinamicas(rho, V_local, CL, CD, A)
    res = resolver_equilibrio(L, D, W_cometa, mu, g, longitud_hilo)
    res["V_local_verdadero"] = perfil_viento(res["altura"])
    res["altura_verdadera"] = res["altura"]
    return res


def generar_mediciones(longitudes_hilo, perfil_viento, rho, CL, CD, A,
                        W_cometa, mu, g=G, ruido_relativo=0.0, semilla=None):
    """
    Genera lecturas sintéticas (T0, theta0) para cada longitud de hilo,
    con ruido relativo opcional para imitar el error de instrumento.
    """
    rng = np.random.default_rng(semilla)
    mediciones = []
    for ell in longitudes_hilo:
        res = simular_vuelo(ell, perfil_viento, rho, CL, CD, A, W_cometa, mu, g)
        T0 = res["T0"]
        theta0 = res["theta0_deg"]
        if ruido_relativo > 0:
            T0 *= (1 + rng.normal(0, ruido_relativo))
            theta0 += rng.normal(0, ruido_relativo * theta0)
        mediciones.append({
            "longitud_hilo": ell,
            "T0_medido": T0,
            "theta0_medido_deg": theta0,
            "V_verdadero": res["V_local_verdadero"],
            "altura_verdadera": res["altura_verdadera"],
        })
    return mediciones


# ---------------------------------------------------------------------
# 3) Solver inverso: de (T0, theta0) medidos a (V, altura) estimados
# ---------------------------------------------------------------------

def invertir_medicion(T0, theta0_deg, longitud_hilo, rho, CL, CD, A,
                       W_cometa, mu, g=G):
    """
    A partir de una lectura (T0, theta0) y de la longitud de hilo
    desplegada, estima:
      - la altura real de la cometa (geometría pura, vía catenaria)
      - la velocidad del viento en dos formas independientes
        (desde el arrastre y desde la sustentación), más su discrepancia
        relativa como diagnóstico de calibración de CL/CD.
    """
    if T0 <= 0 or not 0 <= theta0_deg < 90:
        raise ValueError("T0 debe ser positiva y theta0 debe estar entre 0 y 90 grados.")
    if longitud_hilo <= 0 or rho <= 0 or CL <= 0 or CD <= 0 or A <= 0 or mu <= 0:
        raise ValueError("Los parámetros geométricos y aerodinámicos deben ser positivos.")

    theta0 = np.radians(theta0_deg)
    H = T0 * np.cos(theta0)
    V0 = T0 * np.sin(theta0)

    # --- Altura: geometría pura de la catenaria, sin modelo aerodinámico ---
    s = np.linspace(0, longitud_hilo, 300)
    V_s = V0 + mu * g * s
    T_s = np.hypot(H, V_s)
    T0_calc = np.hypot(H, V0)
    y_s = (1.0 / (mu * g)) * (T_s - T0_calc)
    altura = y_s[-1]

    V_top = V0 + mu * g * longitud_hilo

    # --- Velocidad del viento: dos estimaciones independientes ---
    V_arrastre = np.sqrt(2 * H / (rho * CD * A))

    termino_sustentacion = V_top + W_cometa
    if termino_sustentacion > 0:
        V_sustentacion = np.sqrt(2 * termino_sustentacion / (rho * CL * A))
    else:
        V_sustentacion = np.nan

    V_prom = np.nanmean([V_arrastre, V_sustentacion])
    if np.isfinite(V_sustentacion):
        discrepancia_rel = abs(V_arrastre - V_sustentacion) / V_prom
    else:
        discrepancia_rel = np.nan

    return {
        "altura_estimada": altura,
        "V_desde_arrastre": V_arrastre,
        "V_desde_sustentacion": V_sustentacion,
        "V_estimado": V_prom,
        "discrepancia_relativa": discrepancia_rel,
    }


# ---------------------------------------------------------------------
# 4) Ajuste de perfil vertical de viento a los puntos reconstruidos
# ---------------------------------------------------------------------

def ajustar_perfil_potencia(alturas, velocidades, z_ref=10.0):
    """
    Ajusta V(z) = V_ref*(z/z_ref)^alpha por regresión lineal en log-log.
    Devuelve (V_ref, alpha).
    """
    z = np.asarray(alturas, dtype=float)
    V = np.asarray(velocidades, dtype=float)
    if z.shape != V.shape or z.size < 2:
        raise ValueError("alturas y velocidades deben tener la misma forma y al menos dos datos.")
    if z_ref <= 0 or not np.all(np.isfinite(z)) or not np.all(np.isfinite(V)):
        raise ValueError("Los datos y z_ref deben ser finitos.")
    if np.any(z <= 0) or np.any(V <= 0):
        raise ValueError("Las alturas y velocidades deben ser positivas para el ajuste logarítmico.")
    if np.unique(z).size < 2:
        raise ValueError("El ajuste necesita al menos dos alturas diferentes.")
    log_z = np.log(z / z_ref)
    log_V = np.log(V)
    alpha, log_V_ref = np.polyfit(log_z, log_V, 1)
    V_ref = np.exp(log_V_ref)
    return V_ref, alpha


# ---------------------------------------------------------------------
# 5) Demostración completa
# ---------------------------------------------------------------------

if __name__ == "__main__":
    # Parámetros de la cometa y del hilo (mismos del modelo directo)
    rho = 0.89
    CL, CD = 1.0, 0.2
    A = 0.7
    m_cometa = 0.20
    W_cometa = m_cometa * G
    mu = 0.0005

    # Perfil de viento "verdadero" que vamos a tratar de recuperar
    V_ref_verdadero, alpha_verdadero = 4.5, 0.25
    perfil_verdadero = lambda z: viento_ley_potencia(z, V_ref_verdadero, alpha_verdadero)

    longitudes_hilo = [30, 50, 70, 90, 110, 130, 150]

    mediciones = generar_mediciones(
        longitudes_hilo, perfil_verdadero, rho, CL, CD, A, W_cometa, mu,
        ruido_relativo=0.03, semilla=42,
    )

    print(f"{'ℓ (m)':>7} {'T0 (N)':>8} {'θ0 (°)':>8} {'z_est (m)':>10} "
          f"{'V_est (m/s)':>12} {'disc. (%)':>10} {'V_real (m/s)':>13}")

    alturas_est, velocidades_est = [], []
    for med in mediciones:
        inv = invertir_medicion(
            med["T0_medido"], med["theta0_medido_deg"], med["longitud_hilo"],
            rho, CL, CD, A, W_cometa, mu,
        )
        alturas_est.append(inv["altura_estimada"])
        velocidades_est.append(inv["V_estimado"])
        print(f"{med['longitud_hilo']:>7.0f} {med['T0_medido']:>8.2f} "
              f"{med['theta0_medido_deg']:>8.1f} {inv['altura_estimada']:>10.1f} "
              f"{inv['V_estimado']:>12.2f} {inv['discrepancia_relativa']*100:>10.1f} "
              f"{med['V_verdadero']:>13.2f}")

    V_ref_est, alpha_est = ajustar_perfil_potencia(alturas_est, velocidades_est)

    print(f"\nPerfil verdadero : V(z) = {V_ref_verdadero:.2f} * (z/10)^{alpha_verdadero:.2f}")
    print(f"Perfil recuperado: V(z) = {V_ref_est:.2f} * (z/10)^{alpha_est:.2f}")

    # --- Gráfico ---
    z_plot = np.linspace(min(alturas_est) * 0.8, max(alturas_est) * 1.1, 200)
    plt.figure(figsize=(7, 5))
    plt.plot(perfil_verdadero(z_plot), z_plot, label="Perfil verdadero", linewidth=2)
    plt.plot(viento_ley_potencia(z_plot, V_ref_est, alpha_est), z_plot,
              "--", label="Perfil recuperado (ajuste)", linewidth=2)
    plt.scatter(velocidades_est, alturas_est, color="red", zorder=5,
                 label="Puntos reconstruidos por vuelo")
    plt.xlabel("Velocidad del viento (m/s)")
    plt.ylabel("Altura (m)")
    plt.title("Perfil vertical de viento reconstruido a partir de vuelos de cometa")
    plt.legend()
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig("perfil_viento_cometa.png", dpi=150)
    print("\nGráfico guardado en: perfil_viento_cometa.png")
