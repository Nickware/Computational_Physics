# !/usr/bin/env python3
# Este código simula el riesgo crediticio de un préstamo a lo largo del tiempo, considerando el impacto de la tasa de desempleo y la inestabilidad política en la probabilidad de default.
# El modelo asume que el riesgo de default (lambda) aumenta con la tasa de desempleo y la inestabilidad política, y calcula la probabilidad de supervivencia del crédito a lo largo del tiempo.
# Se generan datos simulados para la tasa de desempleo y la inestabilidad política a lo largo de 10 años, y se grafica la probabilidad de no default en función del tiempo.
# El código define los parámetros del modelo, simula los datos de desempleo e inestabilidad política, calcula el riesgo de default y la probabilidad de supervivencia, y finalmente grafica los resultados.
# Nota: Este es un modelo simplificado y no debe ser utilizado para decisiones financieras reales sin una validación adecuada y un análisis más profundo de los factores de riesgo involucrados.
# Ejecutar el código para visualizar cómo el riesgo crediticio evoluciona con el tiempo bajo diferentes condiciones socioeconómicas

# Asegúrarse de tener estas librerías instaladas en tu entorno de Python para ejecutar este código correctamente.
# Instalar estas librerías usando pip si no se tiene:
# pip install numpy matplotlib

# Importar las librerías necesarias
import numpy as np
# numpy para cálculos numéricos y matplotlib para gráficos
import matplotlib.pyplot as plt

# Parámetros del modelo
lambda_0 = 0.05  # Riesgo base (5%)
beta_desempleo = 0.02  # Impacto del desempleo en lambda
beta_politica = 0.01   # Impacto de inestabilidad política

# Datos simulados (años 0 a 10)
tiempo = np.arange(0, 10)
desempleo = np.array([5, 7, 10, 12, 15, 18, 20, 15, 10, 8])  # Tasa de desempleo (%)
inestabilidad = np.array([0, 0, 1, 1, 1, 1, 0, 0, 0, 0])      # 1 = crisis, 0 = estable

# Cálculo de lambda(t)
lambda_t = lambda_0 + beta_desempleo * desempleo + beta_politica * inestabilidad

# Probabilidad de supervivencia del crédito
P_surv = np.exp(-lambda_t * tiempo)

# Gráfico
plt.plot(tiempo, P_surv, 'o-', label="Prob. de no default")
plt.xlabel("Años")
plt.ylabel("P(surv)")
plt.title("Riesgo Crediticio con Variables Socioeconómicas")
plt.grid()
plt.legend()
plt.show()
