# Cometa como anemómetro: perfil vertical de viento

Este documento describe la extensión del modelo de equilibrio cometa +
catenaria (`modelo_cometa_catenaria.py`) hacia un caso de uso distinto:
usar una cometa instrumentada como un sensor de viento en altura, y con
eso reconstruir un **perfil vertical de viento** — insumo directo para
evaluar si tiene sentido explorar potencial eólico en un punto de la
ciudad.

El código de esta extensión está en `perfil_viento_cometa.py`.

## 1. La propuesta

Un volador en tierra puede medir, con instrumentos simples, dos cosas en
cada vuelo:

- **T0**: la tensión del hilo en su mano (con un dinamómetro sencillo o
  un sensor de fuerza en el carrete).
- **θ0**: el ángulo del hilo respecto al suelo (con un inclinómetro o el
  sensor de un celular).

Si además se controla y se conoce **cuánto hilo se ha desplegado** (ℓ),
esas tres cantidades bastan —apoyándose en el modelo de equilibrio y
catenaria ya construido— para estimar, en cada vuelo:

1. La **altura real** a la que está la cometa.
2. La **velocidad del viento** a esa altura.

Repitiendo el vuelo con distintas longitudes de hilo se obtiene una nube
de puntos (altura, velocidad) que se puede ajustar a un perfil vertical
de viento — el mismo tipo de curva que se usa en estudios formales de
recurso eólico urbano.

## 2. ¿Por qué la altura no depende de suponer nada sobre el viento?

Un punto importante del modelo: de T0 y θ0 se obtienen directamente las
componentes de la tensión,

$$H = T_0\cos\theta_0 \qquad V_0 = T_0\sin\theta_0$$

y con esas dos cantidades —más la masa por metro del hilo (μ), que es una
propiedad física conocida del hilo, no del viento— la forma de la
catenaria completa (y por tanto la altura real de la cometa) se calcula
con las mismas fórmulas cerradas del modelo directo. Es decir, **la
altura es un resultado geométrico**, no depende de haber acertado con
$C_L$, $C_D$ o la densidad del aire.

## 3. ¿Por qué la velocidad del viento sí depende del modelo aerodinámico?

La velocidad, en cambio, requiere conocer (o haber calibrado antes) los
coeficientes aerodinámicos de esa cometa en particular. Hay dos caminos
independientes para estimarla, uno desde el arrastre y otro desde la
sustentación:

$$V_{arrastre} = \sqrt{\dfrac{2H}{\rho\, C_D\, A}} \qquad
V_{sustentacion} = \sqrt{\dfrac{2\,(V_{top}+W_{cometa})}{\rho\, C_L\, A}}$$

En un modelo perfectamente calibrado ambas deberían coincidir. La
**discrepancia relativa entre las dos** es, en la práctica, el indicador
más útil de qué tan confiable es la calibración de $C_L$/$C_D$ para esa
cometa — si la discrepancia es grande, no vale la pena confiar en el
valor de $V$ estimado, sin importar cuántos vuelos se hagan.

## 4. ¿Qué hace el script?

`perfil_viento_cometa.py` implementa el flujo completo, con datos
sintéticos (porque no hay mediciones de campo reales), para poder validar
el método antes de usarlo con datos reales:

1. Define un **perfil de viento verdadero** tipo ley de potencia,
   $V(z)=V_{ref}(z/10)^\alpha$, típico de capa límite urbana.
2. **Simula vuelos autoconsistentes**: para cada longitud de hilo, resuelve
   iterativamente el equilibrio porque el viento que "ve" la cometa
   depende de su altura, y la altura depende del viento — hasta que
   converge. Esto genera las lecturas T0, θ0 que un volador real
   registraría, con ruido de instrumento opcional.
3. **Invierte** esas lecturas, vuelo por vuelo, para recuperar altura y
   velocidad, sin usar el perfil verdadero — solo la física de
   equilibrio.
4. **Ajusta** un perfil de potencia a los puntos reconstruidos y lo
   compara contra el perfil verdadero usado para generar los datos.

En la corrida de ejemplo (7 vuelos, hilo entre 30 y 150 m, ruido de
instrumento del 3%), el perfil verdadero era $V=4{,}5\,(z/10)^{0{,}25}$ y
el recuperado fue $V\approx4{,}8\,(z/10)^{0{,}22}$ — razonablemente
cercano, con discrepancias arrastre/sustentación del orden de 3–12% por
vuelo, coherentes con el nivel de ruido introducido.

## 5. Conexión con la evaluación de un parque eólico

Este perfil reconstruido es exactamente el tipo de insumo (exponente α de
capa límite, velocidad de referencia) que alimenta un cálculo de densidad
de potencia eólica, $P/A=\tfrac12\rho V^3$, a distintas alturas. Sirve
como:

- Una estimación **puntual y rápida** de la estructura vertical del
  viento en un parque específico, en un punto donde no hay torre
  meteorológica.
- Un método de **calibración/validación** para modelos CFD o de capa
  límite urbana que después sí se usan para el dimensionamiento formal.

No reemplaza series largas de datos ni redes de anemómetros fijos —eso
sigue siendo el estándar para decidir si un parque eólico es viable—,
pero es una manera barata de obtener una primera lectura del recurso
eólico en altura antes de invertir en instrumentación permanente.

## 6. Limitaciones de este caso concreto

- Los datos usados aquí son **sintéticos**; el método no se ha validado
  todavía contra mediciones reales de viento en Bogotá.
- Se asume $C_L$, $C_D$ y $A$ constantes y conocidos de antemano — en la
  práctica requieren una calibración previa de esa cometa específica
  (por ejemplo, comparando contra un anemómetro de referencia en tierra
  en un día de viento conocido).
- El muestreo está sesgado hacia condiciones "buenas para volar cometas"
  (viento suficiente, sin lluvia, sin ráfagas extremas), lo que
  probablemente subestima la variabilidad real del viento a lo largo del
  año.
- Se sigue despreciando el arrastre aerodinámico sobre el hilo mismo.

## 7. Perspectivas para un modelo mejorado

- **Calibración experimental de $C_L$ y $C_D$**: en vez de asumirlos
  fijos, estimarlos en campo volando la cometa a una altura conocida
  frente a un anemómetro de referencia, y ajustar los coeficientes para
  minimizar la discrepancia arrastre/sustentación descrita en la sección 3.
- **Incluir el arrastre del hilo**: actualmente el hilo solo aporta peso
  a la catenaria; con hilos largos y viento fuerte, el arrastre
  distribuido sobre el propio hilo deja de ser despreciable y rompe la
  hipótesis de que $H$ es constante en toda su longitud. Un modelo más
  completo resolvería la catenaria como una ecuación diferencial con
  fuerza horizontal distribuida, no en forma cerrada.
- **Propagación de incertidumbre**: en vez de un solo valor de $V$ por
  vuelo, propagar el error de instrumento de $T0$ y $\theta_0$ (y la
  incertidumbre en $C_L$/$C_D$) hasta una banda de confianza sobre
  $\alpha$ y $V_{ref}$ del perfil ajustado — hoy el ajuste no reporta
  incertidumbre.
- **Perfil no estacionario**: el modelo asume viento constante durante
  cada vuelo. Incorporar ráfagas y su efecto dinámico (la cometa oscila
  alrededor del punto de equilibrio, como se señaló en el documento de
  física base) permitiría además estimar intensidad de turbulencia, un
  parámetro relevante para el diseño estructural de un aerogenerador.
- **Validación cruzada con datos reales**: repetir el experimento
  sintético con mediciones de campo reales en un parque de Bogotá
  (Ciudad Bolívar u otro punto con vientos fuertes de agosto), comparando
  contra estaciones meteorológicas cercanas del IDEAM, para cuantificar
  el error real del método y no solo el error frente a un perfil
  sintético conocido.
- **Extensión a rosa de vientos**: el modelo actual asume una única
  dirección de viento. Repitiendo el experimento en distintos días y
  condiciones se podría construir no solo un perfil vertical sino una
  rosa de vientos aproximada por altura, más cercana a lo que exige un
  estudio formal de potencial eólico.
