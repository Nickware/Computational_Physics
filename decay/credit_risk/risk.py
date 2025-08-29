import numpy as np
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
