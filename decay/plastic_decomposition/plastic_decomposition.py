import numpy as np
import matplotlib.pyplot as plt

# Parámetros para PET en Bogotá
lambda_env = 0.0012  # Degradación ambiental
lambda_bio = 0.0001  # Biodegradación (baja por altitud)
lambda_hum = 0.011   # Intervención humana (11% reciclaje)

M0 = 100  # 100 gramos de plástico inicial
tiempo = np.arange(0, 500)  # 500 años

# Cálculo de masa remanente
M_t = M0 * np.exp(-(lambda_env + lambda_bio + lambda_hum) * tiempo)

# Gráfico
plt.figure(figsize=(10, 6))
plt.plot(tiempo, M_t, 'g-', linewidth=2, label="PET en Bogotá")
plt.axhline(y=50, color='r', linestyle='--', label='50% degradación (≈415 años)')
plt.xlabel("Años")
plt.ylabel("Masa remanente (%)")
plt.title("Descomposición de Plástico PET en Condiciones de Bogotá")
plt.grid(True, alpha=0.3)
plt.legend()
plt.show()
