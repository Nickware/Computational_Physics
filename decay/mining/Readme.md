# Decrecimiento Exponencial de los Recursos Hídricos por Minería

La **disponibilidad de agua** en comunidades cercanas a operaciones mineras puede disminuir de forma **exponencial** o explicarse mediante otros modelos. En general el fenómeno presenta varias complejidades. A continuación se describe cómo se podría modelarse mediante el modelo **exponencial** y cuáles factores lo alteran.

## 1. Analogía: Modelo Exponencial

La **tasa de pérdida de agua** (volumen o calidad) puede modelarse así:
$$
V(t) = V_0 e^{-\lambda t}
$$
- $$V(t)$$: Volumen/calidad de agua en el tiempo $$t$$
- $$V_0$$: Valor inicial
- $$\lambda$$: Tasa de agotamiento, ligada a:
  - Intensidad de extracción minera
  - Contaminación química (ej.: drenaje ácido)
  - Alteración de acuíferos/cauces naturales

Ejemplo: Si una minera reduce un 10% el agua disponible por año, $$\lambda \approx 0.1\,\text{año}^{-1}$$.

## 2. Factores que Afectan la Dinámica

El modelo puro es una **simplificación**; influyen:

- **No linealidades**
  - *Umbrales críticos*: El agua puede agotarse abruptamente si un acuífero se seca completamente.
  - *Retroalimentación positiva*: Menos agua → más erosión → menos recarga del acuífero.

- **Externalidades**
  - *Contaminación*: Metales pesados (como mercurio y arsénico) deterioran irreversible la calidad del agua[11].
  - *Clima*: Sequías aceleran el agotamiento.

- **Escalas temporales**
  - *Corto plazo*: Agotamiento rápido por extracción directa (ej.: desvío de ríos).
  - *Largo plazo*: Contaminación gradual de napas subterráneas.

## 3. Casos Reales

- **Cerro de Pasco (Perú)**: Disminución exponencial de agua potable por contaminación minera.
- **Cuenca del Río Pilcomayo (Bolivia/Argentina)**: Sedimentos tóxicos por minería reducen agua disponible para comunidades indígenas[9].

## 4. Modelos Más Complejos

Para mayor precisión, se emplean:

- **Ecuaciones diferenciales acopladas**:
  $$
  \frac{dV}{dt} = -\lambda V + R(t) - C(t)
  $$
  - $$R(t)$$: Recarga natural
  - $$C(t)$$: Consumo minero

- **Sistemas dinámicos**: Modelan umbrales de colapso, como puntos de "no retorno".

## 5. Demostración en Datos Reales

- **Recopilación**: Medir niveles/calidad de agua (ej.: metales) por años.
- **Ajuste de curvas**: Usar regresión no lineal (Python o R) para verificar el ajuste exponencial.
- **Validación**: Utilizar modelos hidrológicos, como MODFLOW (USGS), para simular flujos subterráneos afectados por minería.

---

La modelización matemática ayuda a entender y prever el **impacto complejo y acelerado** de la minería sobre los recursos hídricos, facilitando estrategias de gestión y protección ambiental.