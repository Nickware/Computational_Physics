# Modelos de decaimiento exponencial

Esta carpeta reúne modelos educativos que reutilizan una misma idea matemática en contextos físicos, ambientales y económicos. No es una única aplicación: cada subcarpeta contiene un script independiente y su documentación.

## Estructura del proyecto

| Proyecto | Implementación actual | Qué simula | Documentación |
| :-- | :-- | :-- | :-- |
| `radioactive` | Python y True BASIC | Número de núcleos restantes de una muestra radiactiva | [`Readme.md`](radioactive/Readme.md) |
| `credit_risk` | Python | Probabilidad de supervivencia de un crédito con desempleo e inestabilidad política simulados | [`Readme.md`](credit_risk/Readme.md) |
| `loss_value` | Python | Pérdida exponencial del valor de una inversión bajo riesgos económicos, políticos y regulatorios | [`Readme.md`](loss_value/Readme.md) |
| `mining` | Python | Ajuste exponencial de datos hipotéticos de disponibilidad hídrica afectados por minería | [`Readme.md`](mining/Readme.md) |
| `water resources` | Python | Disponibilidad hídrica en Santurbán usando minería, gobernanza y demanda como variables | [`Readme.md`](water%20resources/Readme.md) |
| `plastic_decomposition` | Python | Masa remanente de plástico PET considerando degradación ambiental, biodegradación e intervención humana | [`Readme.md`](plastic_decomposition/Readme.md) |

## Modelo común

La forma elemental del modelo es:

```text
dX/dt = -lambda X  ->  X(t) = X0 exp(-lambda t)
```

`X` representa la magnitud que disminuye y `lambda` su tasa de decaimiento. En el caso radiactivo, `lambda` es constante. En los modelos aplicados, la tasa se interpreta como la suma de factores externos o cambia con variables simuladas.

Los scripts no pretenden producir predicciones reales. Sus datos son hipotéticos o simplificados y sirven para practicar la formulación de modelos, el cálculo con `numpy`, el ajuste de curvas y la visualización con `matplotlib`.

## Cómo ejecutar los modelos

Desde la carpeta correspondiente:

```bash
python3 risk.py
python3 loss_argentina.py
python3 mining.py
python3 resources_santurban.py
python3 plastic_decomposition.py
python3 radiactive.py
```

Los scripts de Python muestran sus gráficos en pantalla. Para instalar las dependencias comunes:

```bash
python3 -m pip install numpy matplotlib scipy
```

`scipy` solo es necesario para `mining.py`, que utiliza `scipy.optimize.curve_fit`.

La carpeta `radioactive` también conserva una implementación histórica en True BASIC, documentada en [`decay.md`](radioactive/decay.md). Esa versión requiere las bibliotecas gráficas mencionadas en su propia documentación y no forma parte de la ejecución de los scripts Python.

---

## Patrones comunes identificados

### 1. Estructura matemática universal
```
dX/dt = -λX  →  X(t) = X₀e^(-λt)
```
Donde **X** representa la cantidad que decae y **λ** la tasa de decaimiento.

### 2. Adaptaciones para sistemas complejos
- **λ constante**: Sistemas puros (decaimiento radiactivo)
- **λ(t) dinámica**: Sistemas con influencias externas
  - `λ(t) = f(variables socioeconómicas, políticas, ambientales)`

### 3. Métodos de validación
- **Ajuste por mínimos cuadrados** a datos experimentales
- **Estimación de parámetros** con regresión no lineal
- **Validación cruzada** con datos históricos

---

## Limitaciones y extensiones

| **Modelo** | **Limitaciones** | **Extensiones Propuestas** |
|------------|------------------|---------------------------|
| **Todos** | Supone independencia de eventos | Incorporar correlaciones temporales |
| **Recursos hídricos** | No captura umbrales de colapso | Modelos con puntos de no retorno |
| **Riesgo financiero** | Asume normalidad en distribuciones | Usar distribuciones de cola pesada (Cauchy, Pareto) |
| **Contaminantes** | Ignora interacciones entre compuestos | Modelos de decaimiento acoplado |

---

## Herramientas computacionales utilizadas

- **Python**: `numpy`, `matplotlib` y `scipy.optimize.curve_fit`.
- **True BASIC**: implementación histórica del modelo radiactivo.
- **Software externo propuesto**: MODFLOW aparece como posible extensión hidrológica en la documentación, pero no está incluido en este repositorio.

---

## Principio fundamental

> **"El decaimiento exponencial emerge en sistemas donde la tasa de cambio es proporcional al estado actual, independientemente del dominio científico"**

Esta universalidad permite transferir metodologías entre disciplinas aparentemente no relacionadas, desde la física nuclear hasta la economía conductual.
