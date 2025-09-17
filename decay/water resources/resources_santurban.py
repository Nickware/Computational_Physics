import numpy as np
import matplotlib.pyplot as plt

# Datos hipotéticos basados en estudios
tiempo = np.arange(0, 10)  # 2014-2024
M = np.array([10, 20, 50, 100, 150, 200, 250, 300, 350, 400])  # Ha concesionadas
I = np.array([0.7, 0.6, 0.5, 0.4, 0.3, 0.3, 0.2, 0.2, 0.1, 0.1])  # Gobernanza (0-1)
D = np.array([1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5])  # % crecimiento demanda

# Parámetros del modelo
alpha, beta, gamma = 0.05, 0.03, 0.02
V0 = 100  # Disponibilidad hídrica inicial (%)

# Cálculo de lambda(t) y V(t)
lambda_t = alpha * M/100 + beta * (I < 0.5) + gamma * D
V_t = V0 * np.exp(-lambda_t * tiempo)

# Gráfico
plt.plot(tiempo, V_t, 'b-', label="Disponibilidad hídrica (%)")
plt.fill_between(tiempo, V_t, 0, color='b', alpha=0.1)
plt.xlabel("Años (2014-2024)")
plt.ylabel("Agua disponible (%)")
plt.title("Decaimiento Hídrico en Santurbán por Minería y Gobernanza")
plt.grid()
plt.legend()
plt.show()
