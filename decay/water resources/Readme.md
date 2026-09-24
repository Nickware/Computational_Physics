# Disponibilidad hídrica en Santurbán

Este proyecto explora, con un modelo exponencial sencillo, cómo distintas presiones podrían asociarse con una disminución de la disponibilidad hídrica en el páramo de Santurbán, Colombia. Su objetivo es didáctico: practicar la construcción de un modelo, trabajar con arreglos de `numpy` y visualizar resultados con `matplotlib`.

El programa no utiliza una base de datos externa. Los valores incluidos en [`resources_santurban.py`](resources_santurban.py) son hipotéticos y no deben interpretarse como mediciones de Santurbán ni como un pronóstico ambiental.

## Modelo implementado

El script define tres series de entrada para diez instantes:

- `M`: hectáreas mineras concesionadas, con valores hipotéticos.
- `I`: índice de gobernanza entre 0 y 1.
- `D`: crecimiento porcentual de la demanda.

También define los parámetros:

| Parámetro | Valor | Interpretación en el script |
| :-- | --: | :-- |
| `alpha` | `0.05` | Peso de `M / 100` |
| `beta` | `0.03` | Penalización cuando `I < 0.5` |
| `gamma` | `0.02` | Peso de `D` |
| `V0` | `100` | Disponibilidad hídrica inicial, expresada como porcentaje |

La tasa calculada por el código es:

$$
\lambda_t = \alpha\frac{M_t}{100} + \beta\,\mathbf{1}_{I_t < 0.5} + \gamma D_t
$$

donde $\mathbf{1}_{I_t < 0.5}$ vale 1 cuando la gobernanza está por debajo de 0.5 y 0 en caso contrario. La disponibilidad se calcula como:

$$
V_t = V_0 e^{-\lambda_t t}
$$

Es importante notar que esta implementación usa la tasa correspondiente a cada instante directamente en la exponencial. No calcula una integral acumulada de una tasa variable. Para un modelo temporal más riguroso, sería necesario definir con claridad la unidad de cada variable y acumular el efecto de $\lambda(t)$ entre pasos.

## Ejecución

Desde esta carpeta, ejecuta:

```bash
python3 resources_santurban.py
```

También puede ejecutarse desde la raíz del repositorio:

```bash
python3 "decay/water resources/resources_santurban.py"
```

Dependencias:

```bash
python3 -m pip install numpy matplotlib
```

El programa muestra una gráfica con:

- La disponibilidad hídrica estimada como una línea azul.
- Un área sombreada bajo la curva.
- El tiempo en años y la disponibilidad porcentual en los ejes.

## Cómo interpretar el resultado

La gráfica permite observar cómo el valor `V_t` disminuye cuando aumentan las presiones representadas por `M`, `D` o por el indicador de baja gobernanza. El resultado ilustra la sensibilidad del modelo a sus parámetros; no demuestra causalidad ni cuantifica el comportamiento real del ecosistema.

Para usar datos de campo sería necesario sustituir los arreglos del script por mediciones documentadas, especificar sus unidades, calibrar `alpha`, `beta` y `gamma`, y comparar el ajuste con observaciones independientes.

## Limitaciones

- Los datos son hipotéticos y no están conectados a una fuente de mediciones.
- El modelo resume la minería, la gobernanza y la demanda en una sola tasa de decaimiento.
- No incluye recarga natural, precipitación, sequías, contaminación, caudal, calidad del agua ni umbrales de colapso.
- No representa retroalimentaciones sociales o ambientales.
- La fórmula implementada no es una integración temporal de una tasa variable.
- El resultado depende de parámetros elegidos manualmente y no incluye incertidumbre.

## Posibles extensiones

1. Incorporar datos observados de caudal, precipitación, calidad del agua y extracción.
2. Ajustar los parámetros mediante regresión y reportar intervalos de incertidumbre.
3. Reemplazar el modelo exponencial simple por una ecuación diferencial con recarga y consumo:
   $$\frac{dV}{dt} = -\lambda(t)V + R(t) - C(t)$$
4. Comparar escenarios de regulación, demanda y actividad minera.
5. Validar los resultados con un modelo hidrológico especializado, sin presentar este script como sustituto de un estudio ambiental.

## Contexto y referencias

Santurbán es un ecosistema relevante para el abastecimiento de agua y objeto de debates sobre minería, delimitación y protección ambiental. Las siguientes referencias sirven como contexto general y no constituyen los datos utilizados por el script:

- [Corte Constitucional de Colombia](https://www.corteconstitucional.gov.co)
- [Agencia Nacional de Minería](https://www.anm.gov.co)
- [IDEAM](https://www.ideam.gov.co)
- [WWF Colombia](https://www.wwf.org.co)
