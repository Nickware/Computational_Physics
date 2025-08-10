import numpy as np
import matplotlib.pyplot as plt

def decay_simulation(N0, tau, total_time, dt):
    time_steps = np.arange(0, total_time, dt)
    N = N0 * np.exp(-time_steps / tau)  # Ley exponencial
    plt.plot(time_steps, N)
    plt.xlabel("Tiempo")
    plt.ylabel("Núcleos restantes")
    plt.title("Decaimiento Radiactivo")
    plt.show()

# Ejemplo para Uranio-238 (vida media ≈ 4.468e9 años)
decay_simulation(N0=10000, tau=4.468e9, total_time=1e10, dt=1e8)
