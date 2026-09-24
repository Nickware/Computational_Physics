"""
Modelo de equilibrio de una cometa incluyendo la catenaria del hilo.

Idea del modelo
----------------
1) La cometa se trata como un punto en el extremo superior del hilo. Sobre
   ella actúan: su peso propio, la sustentación L (vertical) y el arrastre D
   (horizontal, en la dirección del viento), y la tensión que el hilo ejerce
   justo en el punto de amarre. El equilibrio de la cometa da directamente
   las componentes de la tensión en ese punto:

       H       = D                     (componente horizontal, constante
                                         en todo el hilo)
       V_top   = L - W_cometa           (componente vertical en el punto
                                         de amarre)

2) El hilo tiene una masa por unidad de longitud mu (kg/m). Como no hay
   fuerzas horizontales distribuidas sobre el hilo (se desprecia el
   arrastre del aire sobre el hilo mismo, solo su peso), H es constante en
   toda su longitud. La componente vertical crece con la longitud de hilo
   que hay que sostener por debajo de cada punto:

       V(s) = V0 + mu * g * s      ,   s in [0, longitud_hilo]

   Con V(longitud_hilo) = V_top ya conocido, se despeja V0 (lo que siente
   el volador en la mano).

3) La forma del hilo (x(s), y(s)) tiene solución cerrada, la misma que una
   cadena colgante clásica:

       x(s) = (H / (mu*g)) * [asinh(V(s)/H) - asinh(V0/H)]
       y(s) = (1 / (mu*g)) * [T(s) - T0]

   con T(s) = sqrt(H^2 + V(s)^2).

Este script calcula todo lo anterior para un caso concreto y grafica la
forma real del hilo (con su curvatura), comparándola contra la aproximación
de línea recta.
"""

import numpy as np
import matplotlib.pyplot as plt


G = 9.81  # m/s^2


def fuerzas_aerodinamicas(rho, V, CL, CD, A):
    """Sustentación (L) y arrastre (D) en Newtons."""
    if rho <= 0 or V < 0 or CL <= 0 or CD <= 0 or A <= 0:
        raise ValueError("rho, CL, CD y A deben ser positivos; V no puede ser negativa.")
    q = 0.5 * rho * V**2
    L = q * CL * A
    D = q * CD * A
    return L, D


def resolver_equilibrio(L, D, W_cometa, mu, g, longitud_hilo):
    """
    Dado el par (L, D) de la cometa, su peso propio, la masa por metro del
    hilo (mu) y la longitud de hilo desplegada, devuelve un diccionario con
    las tensiones, ángulos, altura y alcance horizontal.
    """
    if L < 0 or D <= 0 or W_cometa < 0 or mu <= 0 or g <= 0 or longitud_hilo <= 0:
        raise ValueError("Las fuerzas, la masa lineal, g y la longitud deben ser válidas.")

    H = D
    V_top = L - W_cometa
    if V_top <= 0:
        raise ValueError(
            "La sustentación no alcanza a compensar el peso de la cometa: "
            "no hay vuelo estable con estos parámetros."
        )

    V0 = V_top - mu * g * longitud_hilo
    if V0 <= 0:
        raise ValueError(
            "El hilo es demasiado largo o pesado para esta sustentación: "
            "V0 <= 0 (el modelo de catenaria no converge a un vuelo alto)."
        )

    T0 = np.hypot(H, V0)
    T_top = np.hypot(H, V_top)
    theta0 = np.degrees(np.arctan2(V0, H))
    theta_top = np.degrees(np.arctan2(V_top, H))

    # Forma completa del hilo, muestreada en s
    s = np.linspace(0, longitud_hilo, 400)
    V_s = V0 + mu * g * s
    T_s = np.hypot(H, V_s)

    x_s = (H / (mu * g)) * (np.arcsinh(V_s / H) - np.arcsinh(V0 / H))
    y_s = (1.0 / (mu * g)) * (T_s - T0)

    altura = y_s[-1]
    alcance_horizontal = x_s[-1]

    # Comparación con la aproximación de línea recta (mismo theta0)
    theta0_rad = np.radians(theta0)
    altura_recta = longitud_hilo * np.sin(theta0_rad)
    alcance_recta = longitud_hilo * np.cos(theta0_rad)

    return {
        "H": H, "V0": V0, "V_top": V_top,
        "T0": T0, "T_top": T_top,
        "theta0_deg": theta0, "theta_top_deg": theta_top,
        "altura": altura, "alcance_horizontal": alcance_horizontal,
        "altura_aprox_recta": altura_recta,
        "alcance_aprox_recta": alcance_recta,
        "x_s": x_s, "y_s": y_s, "s": s,
    }


def imprimir_resultados(res, L, D, longitud_hilo):
    print(f"Sustentación L = {L:.2f} N   |   Arrastre D = {D:.2f} N")
    print(f"Longitud de hilo desplegado: {longitud_hilo:.1f} m\n")
    print(f"Tensión en la mano del volador : T0   = {res['T0']:.2f} N"
          f"   (ángulo con el suelo: {res['theta0_deg']:.1f}°)")
    print(f"Tensión en el punto de amarre  : Ttop = {res['T_top']:.2f} N"
          f"   (ángulo con el suelo: {res['theta_top_deg']:.1f}°)")
    print(f"\nAltura real de la cometa (con catenaria) : {res['altura']:.1f} m")
    print(f"Alcance horizontal (con catenaria)       : "
          f"{res['alcance_horizontal']:.1f} m")
    print(f"\nAltura si el hilo fuera recto (aprox.)   : "
          f"{res['altura_aprox_recta']:.1f} m")
    print(f"Alcance si el hilo fuera recto (aprox.)   : "
          f"{res['alcance_aprox_recta']:.1f} m")
    diff = res['altura_aprox_recta'] - res['altura']
    print(f"\nDiferencia de altura por la curvatura del hilo: {diff:.2f} m")


def graficar(res, nombre_archivo="forma_hilo_cometa.png"):
    plt.figure(figsize=(7, 5))
    plt.plot(res["x_s"], res["y_s"], label="Forma real del hilo (catenaria)",
              linewidth=2)
    plt.plot([0, res["alcance_aprox_recta"]], [0, res["altura_aprox_recta"]],
              "--", label="Aproximación de línea recta", color="gray")
    plt.scatter([res["x_s"][-1]], [res["y_s"][-1]], color="red", zorder=5,
                 label="Posición de la cometa")
    plt.xlabel("Distancia horizontal (m)")
    plt.ylabel("Altura (m)")
    plt.title("Forma del hilo de la cometa en equilibrio")
    plt.legend()
    plt.grid(alpha=0.3)
    plt.axis("equal")
    plt.tight_layout()
    plt.savefig(nombre_archivo, dpi=150)
    print(f"\nGráfico guardado en: {nombre_archivo}")


if __name__ == "__main__":
    # --- Caso: cometa Delta de 1 m en Ciudad Bolívar, viento fuerte de agosto ---
    rho = 0.89          # kg/m^3, densidad del aire en Bogotá (~2600 m)
    V = 5.6             # m/s (~20 km/h)
    CL, CD = 1.0, 0.2   # coeficientes típicos de una Delta bien ajustada
    A = 0.7             # m^2, área proyectada

    m_cometa = 0.20     # kg, masa de la estructura (sin el hilo)
    W_cometa = m_cometa * G

    mu = 0.0005         # kg/m, masa por metro de un hilo delgado de cometa
    longitud_hilo = 120  # m, hilo desplegado

    L, D = fuerzas_aerodinamicas(rho, V, CL, CD, A)
    res = resolver_equilibrio(L, D, W_cometa, mu, G, longitud_hilo)
    imprimir_resultados(res, L, D, longitud_hilo)
    graficar(res)
