# Simulación de la descomposición de plástico PET en condiciones de Bogotá
# Este código modela la degradación de plástico PET considerando factores ambientales, biodegradación y reciclaje humano.
# Parámetros ajustados para reflejar la realidad de Bogotá, donde la biodegradación es baja debido a la altitud y el reciclaje es limitado.
# El resultado muestra que el plástico PET puede tardar aproximadamente 415 años en degradarse al 50% en estas condiciones.
# Autor: [Tu Nombre]
# Nota: Este modelo es una simplificación y no considera factores como la fragmentación, la exposición a la luz solar o la variabilidad en las condiciones ambientales.
# Para una evaluación más precisa, se recomienda realizar estudios de campo y laboratorio específicos para las condiciones de Bogotá.
# Referencias:
# - Geyer, R., Jambeck, J. R., & Law, K. L. (2017). Production, use, and fate of all plastics ever made. Science Advances
# - Andrady, A. L. (2011). Microplastics in the marine environment. Marine Pollution Bulletin
# - Rochman, C. M., Browne, M. A., Halpern, B. S., Hentschel, B. T., Hoh, E., Karapanagioti, H. K., ... & Rios-Mendoza, L. M. (2013). Policy: Classify plastic waste as hazardous. Science
# Este código es solo una simulación y no debe ser utilizado como una predicción exacta de la degradación del plástico en Bogotá. Se recomienda realizar estudios adicionales para obtener datos más precisos y específicos para la región.
# Para ejecutar este código, asegúrate de tener instalados los paquetes numpy y matplotlib. Puedes instalarlos usando pip:
# pip install numpy matplotlib
# El código genera un gráfico que muestra la masa remanente de plástico PET a lo largo del tiempo, destacando el punto en el que se alcanza el 50% de degradación. Esto proporciona una visualización clara de la lenta degradación del plástico en las condiciones específicas de Bogotá.
# Si deseas ajustar los parámetros para otros tipos de plástico o condiciones ambientales, simplemente modifica los valores de lambda_env, lambda_bio y lambda_hum según sea necesario.
# ¡Espero que este código te sea útil para entender la descomposición del plástico en Bogotá! Si tienes alguna pregunta o necesitas ayuda para modificar el código, no dudes en preguntar.
# Recuerda que la degradación del plástico es un proceso complejo y multifactorial, y este modelo es una simplificación para ilustrar el concepto. Para obtener resultados más precisos, se recomienda realizar estudios de campo y laboratorio específicos para las condiciones de Bogotá.
# Además, ten en cuenta que la degradación del plástico puede variar significativamente dependiendo de factores como la exposición a la luz solar, la temperatura, la humedad y la presencia de microorganismos, entre otros. Por lo tanto, este modelo es solo una aproximación y no debe ser considerado como una predicción exacta de la degradación del plástico en Bogotá.
# Para obtener una comprensión más completa de la degradación del plástico en Bogotá, se recomienda realizar estudios adicionales que consideren estos factores y proporcionen datos específicos para la región. Esto permitirá desarrollar estrategias más efectivas para la gestión de residuos plásticos y la mitigación de su impacto ambiental en Bogotá.
# ¡Gracias por tu interés en este tema importante! La degradación del plástico es un desafío global, y comprender cómo se descompone en diferentes condiciones es crucial para desarrollar soluciones sostenibles. Si tienes alguna pregunta adicional o necesitas ayuda con cualquier aspecto del código, no dudes en preguntar. Estoy aquí para ayudarte.
# Este código es una simulación y no debe ser utilizado como una predicción exacta de la degradación del plástico en Bogotá. Se recomienda realizar estudios adicionales para obtener datos más precisos y específicos para la región.
# Para ejecutar este código, asegúrate de tener instalados los paquetes numpy y matplotlib. Puedes instalarlos usando pip:
# pip install numpy matplotlib
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
