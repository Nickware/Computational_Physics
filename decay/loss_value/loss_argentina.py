import numpy as np
import matplotlib.pyplot as plt

# Parámetros del modelo (tasas anuales)
lambda_econ = 0.15  # Inflación + recesión
lambda_pol = 0.10    # Elecciones 2023 + protestas
lambda_reg = 0.05    # Nuevos impuestos (2024)

# Valor inicial de la inversión (USD)
V0 = 100  # USD 100 millones
tiempo = np.arange(0, 5)  # 5 años

# Cálculo del valor ajustado
V_t = V0 * np.exp(-(lambda_econ + lambda_pol + lambda_reg) * tiempo)

# Gráfico
plt.plot(tiempo, V_t, 'ro-', label="Valor de la inversión")
plt.xlabel("Años")
plt.ylabel("Valor (USD millones)")
plt.title("Decaimiento de una Inversión en Argentina (Riesgo Integral)")
plt.grid()
plt.legend()
plt.show()
