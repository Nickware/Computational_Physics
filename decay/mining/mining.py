import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Datos hipotéticos de volumen de agua (en millones de litros)
años = np.array([0, 1, 2, 3, 5, 10])
agua = np.array([100, 90, 81, 73, 60, 36])  # Decaimiento ~10% anual

def modelo_exponencial(t, V0, lambd):
    return V0 * np.exp(-lambd * t)

params, _ = curve_fit(modelo_exponencial, años, agua, p0=[100, 0.1])
V0_ajustado, lambda_ajustado = params

print(f"V0: {V0_ajustado:.2f}, λ: {lambda_ajustado:.4f} (tasa de agotamiento)")

# Gráfico
plt.scatter(años, agua, label="Datos observados")
plt.plot(años, modelo_exponencial(años, *params), 'r-', label="Ajuste exponencial")
plt.xlabel("Años de actividad minera")
plt.ylabel("Volumen de agua disponible")
plt.legend()
plt.show()
