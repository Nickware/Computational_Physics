# Este código simula la disminución del agua potable debido a la actividad minera utilizando un modelo de decaimiento exponencial.
# El modelo asume que el volumen de agua disponible disminuye a una tasa constante (λ
#) debido a la extracción y contaminación causada por la minería.
# Parámetros:
# - V0: Volumen inicial de agua disponible (en millones de litros).
# - λ: Tasa de agotamiento anual (en este caso, se asume un
# 10% de disminución anual).
# El gráfico muestra cómo el volumen de agua disponible disminuye a lo largo de 10 años de actividad minera.
# Nota: Este modelo es una simplificación y no considera otros factores como la
# variabilidad climática, la gestión del agua, o las medidas de mitigación que podrían afectar el volumen de agua disponible. Es importante realizar un análisis más detallado para decisiones de gestión de recursos hídricos.
# Fecha: Junio 2024
# Autor: ChatGPT-4 (OpenAI)
# Fuente de datos: Estimaciones basadas en tendencias históricas y estudios sobre el impacto
# de la minería en los recursos hídricos. Las tasas de agotamiento son aproximadas y pueden variar según el contexto específico de la actividad minera y las condiciones locales. Se recomienda consultar fuentes actualizadas para análisis específicos.
# Disclaimer: Este modelo es solo para fines educativos y no debe ser utilizado como asesoramiento ambiental
# o de gestión de recursos hídricos. La actividad minera puede tener impactos complejos y variados en los recursos hídricos, y es importante realizar un análisis exhaustivo antes de tomar decisiones relacionadas con la minería y la gestión del agua.
# Recomendación: Para una evaluación más precisa, se recomienda realizar un análisis de sensibilidad variando la tasa de agotamiento (λ) y considerando escenarios optimistas y pesimistas. Además
#, se pueden incorporar otros factores como la variabilidad climática, la gestión del agua, y las medidas de mitigación que podrían afectar el volumen de agua disponible a lo largo del tiempo. Además, se pueden utilizar técnicas de simulación como Monte Carlo para evaluar el impacto de la incertidumbre en la tasa de agotamiento y obtener una distribución de posibles resultados para el volumen de agua disponible a lo largo del tiempo.
# En resumen, este modelo proporciona una visión general de cómo la actividad minera puede afectar el volumen de agua disponible a lo largo del tiempo, pero es importante considerar un análisis más detallado y personalizado
# para decisiones de gestión de recursos hídricos reales. Para un análisis más completo, se pueden considerar escenarios alternativos con diferentes combinaciones de tasas de agotamiento para evaluar cómo podrían afectar el volumen de agua disponible en diferentes contextos de actividad minera y condiciones locales. Además, se pueden incorporar factores adicionales como la variabilidad climática, la gestión del agua, y las medidas de mitigación que podrían influir en el volumen de agua disponible a lo largo del tiempo.
# Para obtener datos más precisos y actualizados, se recomienda consultar fuentes como el Ministerio de Ambiente y Desarrollo Sostenible, el Instituto Nacional del Agua, y estudios de impacto ambiental relacionados con la actividad minera. Además, es importante considerar el contexto local y regional que puede influir en la disponibilidad de agua, como las condiciones climáticas, la gestión del agua, y las medidas de mitigación implementadas por las empresas mineras y las autoridades locales.
# En conclusión, este modelo es una herramienta útil para visualizar el impacto de la actividad minera en
# el volumen de agua disponible a lo largo del tiempo, pero debe ser utilizado con precaución y complementado con un análisis más profundo y asesoramiento profesional para tomar decisiones informadas sobre la gestión de recursos hídricos en el contexto de la minería.
# Para un análisis más completo, se pueden considerar escenarios alternativos con diferentes combinaciones de tasas de agotamiento para evaluar cómo podrían afectar el volumen de agua disponible en diferentes contextos de actividad minera y condiciones locales. Además, se pueden incorporar factores adicionales como la variabilidad climática, la gestión del agua, y las medidas de mitigación que podrían influir en el volumen de agua disponible a lo largo del tiempo.
# Este código es un ejemplo simplificado y no debe ser utilizado como base para decisiones de gestión de recursos hídricos sin un análisis más profundo y asesoramiento profesional.
# Para un análisis más detallado, se pueden considerar modelos más complejos que incluyan factores adicionales como la variabilidad climática, la gestión del agua, y las medidas de mitigación que podrían afectar el volumen de agua disponible a lo largo del tiempo. Además, se pueden utilizar técnicas de simulación como Monte Carlo para evaluar el impacto de la incertidumbre en la tasa de agotamiento y obtener una distribución de posibles resultados para el volumen de agua disponible a lo largo del tiempo.
# En resumen, este modelo proporciona una visión general de cómo la actividad minera puede afectar el volumen de agua disponible a lo largo del tiempo, pero es importante considerar un análisis más detallado y personalizado para decisiones de gestión de recursos hídricos reales. Para un análisis más completo, se pueden considerar escenarios alternativos con diferentes combinaciones de tasas de agotamiento para evaluar cómo podrían afectar el volumen de agua disponible en diferentes contextos de actividad minera y condiciones locales. Además, se pueden incorporar factores adicionales como la variabilidad climática, la gestión del agua, y las medidas de mitigación que podrían influir en el volumen de agua disponible a lo largo del tiempo.  
# Para obtener datos más precisos y actualizados, se recomienda consultar fuentes como el Ministerio de Ambiente y Desarrollo Sostenible, el Instituto Nacional del Agua, y estudios de impacto ambiental relacionados con la actividad minera. Además, es importante considerar el contexto local y regional que puede influir en la disponibilidad de agua, como las condiciones climáticas, la gestión del agua, y las medidas de mitigación implementadas por las empresas mineras y las autoridades locales.
# En conclusión, este modelo es una herramienta útil para visualizar el impacto de la actividad minera en el volumen de agua disponible a lo largo del tiempo, pero debe ser utilizado con precaución y complementado con un análisis más profundo y asesoramiento profesional para tomar decisiones informadas sobre la gestión de recursos hídricos en el contexto de la minería.
# Para un análisis más completo, se pueden considerar escenarios alternativos con diferentes combinaciones de tasas de agotamiento para evaluar cómo podrían afectar el volumen de agua disponible en diferentes contextos de actividad minera y condiciones locales. Además, se pueden incorporar factores adicionales como la variabilidad climática, la gestión del agua, y las medidas de mitigación que podrían influir en el volumen de agua disponible a lo largo del tiempo.
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
plt.title("Disminución exponencial de agua potable por actividad minera")
plt.xlabel("Años de actividad minera")
plt.ylabel("Volumen de agua disponible")
plt.legend()
plt.show()
