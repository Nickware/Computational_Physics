# Física de las cometas

Las cometas vuelan porque el viento, al chocar con su superficie inclinada, genera una fuerza de sustentación que vence al peso y se equilibra con la tensión de la cuerda y el arrastre aerodinámico. En agosto, los vientos alisios que se intensifican sobre Colombia proporcionan las condiciones ideales de velocidad y constancia para que ese equilibrio se mantenga y las cometas se queden “ancladas” en el cielo.[1][2][3][4]

## Vientos de agosto en Colombia

En gran parte del país, en especial en el centro y norte, los vientos aumentan su velocidad en agosto porque los vientos alisios del sureste alcanzan un pico de intensidad, con valores típicos del orden de 20–30 km/h. Esa velocidad es suficiente para generar una sustentación apreciable en superficies ligeras como las cometas, sin llegar a ser tan extrema como para destruirlas con turbulencias fuertes.[2][3][1]

- Los vientos alisios son corrientes casi constantes que soplan cerca del Ecuador, frescas y húmedas, muy usadas históricamente en navegación a vela.[1][2]
- Sobre Colombia, estos vientos se intensifican desde finales de julio hasta septiembre, de ahí que agosto se conozca como el mes de las cometas.[3][5][1]

## Fuerzas que actúan sobre una cometa

En vuelo estacionario, sobre una cometa actúan principalmente tres fuerzas: el **peso**, la tensión de la cuerda y la fuerza aerodinámica debida al viento. Esta fuerza aerodinámica puede descomponerse en sustentación (perpendicular al viento) y arrastre o resistencia (paralela al viento).[4]

- La sustentación debe ser mayor que la suma del peso de la cometa y del hilo para que esta se mantenga arriba.[6][4]
- El arrastre tiende a empujar la cometa en la dirección del viento y es compensado por la componente horizontal de la tensión en la cuerda.[4][6]

Cuando estas tres fuerzas se equilibran vectorialmente, la cometa queda en una posición aparentemente fija, aunque en realidad oscila alrededor de un punto de equilibrio.[6][4]

## Ángulo de ataque y forma

El ángulo de ataque es el ángulo entre el viento y el plano de la cometa, y es clave para generar la cantidad adecuada de sustentación sin perder estabilidad. Si el ángulo es muy grande, la cometa ofrece mucha área al viento, aumenta la sustentación, pero también el arrastre y la tendencia a entrar en pérdida o a caer de manera caótica.[7][4][6]

- Para cada velocidad de viento existe un rango de ángulos en el que la cometa genera suficiente sustentación para equilibrar peso y tensión de la cuerda, manteniendo un vuelo estable.[4][6]
- La distribución del centro de presiones respecto al centro de gravedad determina si la cometa tiende a estabilizarse o a voltearse, por eso se usan colas y diseños asimétricos que actúan como quillas estabilizadoras.[8][7][6]

## Equilibrio estático y estabilidad dinámica

Desde el punto de vista estático, el vuelo de una cometa plana ideal se puede analizar con las ecuaciones de equilibrio de un cuerpo rígido: suma de fuerzas y momentos igual a cero. Para que una cometa se mantenga en cierta inclinación, la línea de acción de la resultante aerodinámica y la tensión deben producir un momento neto nulo alrededor del centro de gravedad.[9][7][6]

- Si el centro de presiones queda demasiado adelantado o atrasado respecto al centro de gravedad, la cometa tenderá a picar o a voltearse, perdiendo estabilidad.[7][9]
- Las colas, aletas o curvaturas introducen momentos de corrección que devuelven la cometa hacia su ángulo de equilibrio cuando una ráfaga la perturba, mejorando la estabilidad dinámica.[8][6]

## Papel de la cuerda y del “piloto”

La cuerda no solo “sujeta” la cometa; a través de su tensión y de la posición del brida se controla el ángulo de ataque y, con él, la sustentación y la altura alcanzada. Al recoger o soltar la cuerda, el cometista modifica el ángulo que forma la cuerda con el suelo y la cometa con el viento, cambiando las condiciones de equilibrio.[10][4]

- Aumentar la tensión suele disminuir ligeramente el ángulo de la cometa respecto al viento, permitiendo que gane altura hasta un nuevo equilibrio donde la sustentación vuelve a compensar peso y tensión.[10][4]
- Soltar la cuerda reduce la tensión, lo que puede hacer que la cometa se aleje más y oscile; la habilidad está en ajustar continuamente la tensión para mantener un vuelo estable incluso cuando el viento de agosto es racheado.[10][4]

# Modelo numérico para modelar la física de la cometa

Se puede hacer un modelo numérico sencillo usando la fórmula estándar de sustentación y unos parámetros típicos de Bogotá en agosto (densidad del aire reducida por la altura, viento moderado, cometa ligera de tamaño mediano). Con ese modelo se ve que, con viento suave, la sustentación apenas iguala o incluso queda por debajo del peso, por lo que en la práctica se requiere un viento algo más fuerte o una cometa optimizada (mayor área o mayor coeficiente de sustentación) para mantener un vuelo estable a buena altura.[1][2][3][4]

## Parámetros para una cometa típica en Bogotá

Tomemos como ejemplo una cometa plana de un hilo, de las que suelen usarse en la sabana de Bogotá. Supondremos valores redondos para ilustrar órdenes de magnitud:[4]

- Área efectiva de la cometa: $\(A \approx 0{,}8\ \text{m}^2\)$ (algo así como 0,8 m × 1 m).  
- Masa de la estructura y el papel/tela: $\(m \approx 0{,}20\ \text{kg}\)$.  
- Masa equivalente del hilo elevado: $\(\approx 0{,}05\ \text{kg}\)$ (según longitud en el aire).  
- Densidad del aire en Bogotá (2600 m): $\(\rho \approx 0{,}89\ \text{kg/m}^3\)$.[2]
- Viento “suave” en un parque de Bogotá: tomemos $\(V \approx 8\ \text{km/h} \approx 2{,}2\ \text{m/s}\)$, dentro del rango típico urbano aunque puede ser mayor en agosto.[5][6][1]
- Coeficientes aerodinámicos típicos de cometa plana: $\(C_L \approx 0{,}8\)$, \(C_D \approx 0{,}3\).[7][3]

El peso total efectivo es entonces $\(W = (m + m_h)\,g \approx 0{,}25 \times 9{,}81 \approx 2{,}45\ \text{N}\)$.[4]

## Cálculo de sustentación y arrastre

La sustentación y el arrastre se pueden estimar con:[3][8]
$\[
L = \tfrac{1}{2}\,\rho\,V^2\,C_L\,A
\]$  
$\[
D = \tfrac{1}{2}\,\rho\,V^2\,C_D\,A
\]$

Usando los valores anteriores se obtiene aproximadamente:

- Sustentación: $\(L \approx 1{,}4\ \text{N}\)$.  
- Arrastre: $\(D \approx 0{,}53\ \text{N}\)$.  
- Peso: $\(W \approx 2{,}45\ \text{N}\)$.  

En estas condiciones de viento suave, la sustentación $\(L\)$ es menor que el peso $\(W\)$, así que la cometa apenas se mantendría cerca del suelo o tendería a caer si no hay ráfagas o si el ángulo de ataque no se optimiza.[3][4]

Si en agosto el viento sube a, por ejemplo, 15–20 km/h (4,2–5,6 m/s), la sustentación, que crece con $\(V^2\)$, se multiplica por un factor entre $\((4{,}2/2{,}2)^2 \approx 3{,}6\)$ y $\((5{,}6/2{,}2)^2 \approx 6{,}5\)$. Así, $\(L\)$ podría pasar a estar claramente por encima de $\(W\)$, permitiendo alturas de vuelo mucho mayores.[9][3]

## Ángulo de la cuerda y equilibrio geométrico

En equilibrio, la suma vectorial de peso, sustentación, arrastre y tensión de la cuerda debe ser cero, lo que fija el ángulo de la cometa y de la cuerda con el suelo. Una forma intuitiva de verlo:[7][4]

- La resultante aerodinámica (suma de sustentación y arrastre) debe estar casi alineada con la cuerda para que la tensión pueda equilibrarla.  
- El ángulo de la cometa respecto al viento (ángulo de ataque) se ajusta con el punto de amarre de la brida; pequeños cambios desplazan el centro de presiones y cambian la orientación de esa resultante.[10][7]

Si \(L\) es mucho mayor que $\(W\)$ y el arrastre $\(D\)$ no es enorme, la cuerda se inclina bastante respecto del suelo (ángulos de 45–60° son típicos), y la cometa alcanza altitudes del orden de decenas a pocos centenares de metros, limitadas por la longitud del hilo y la normativa local.[4]

## Estimación de altura alcanzada

Si se conoce la longitud de hilo desplegado $\(s\)$ y el ángulo medio $\(\theta\)$ de la cuerda con el suelo, la altura geométrica aproximada de la cometa es:[4]
$\[
h \approx s \,\sin\theta
\]$

Como ejemplo numérico:

- Supón $\(s = 120\$ $\text{m}\)$ de hilo fuera.  
- Con viento de 15–20 km/h y buena configuración, es razonable un $\(\theta \approx 50^\circ\)$.[4]

Entonces:  
$\[
h \approx 120\,\sin 50^\circ \approx 120 \times 0{,}77 \approx 92\ \text{m}
\]$  

En la práctica, turbulencias, peso real del hilo, flexibilidad de la cometa y pérdidas aerodinámicas reducen algo esa altura, pero el orden de magnitud (decenas de metros para longitudes de hilo del orden de 100 m) es realista para parques y la sabana de Bogotá.[6][5]

## Cómo ajustar el modelo a condiciones reales

Para hacerlo más cercano a una cometa específica en Bogotá podrías:

- Medir masa real de la cometa y del hilo por metro.  
- Estimar área proyectada real (según forma y curvatura).  
- Medir con un anemómetro simple la velocidad del viento en agosto en tu sitio de vuelo.  
- Ajustar $\(C_L\)$ y $\(C_D\)$ según la forma (rombo, delta, cometas tipo foil), usando rangos de literatura.[7][3]

Si quieres, se puede refinar el modelo con un diagrama de fuerzas completo y resolver explícitamente el ángulo de equilibrio y la tensión para un caso que te interese (por ejemplo, Delta de 1 m de envergadura volando en Ciudad Bolívar con vientos fuertes de agosto).

[1](https://ogabogota.unal.edu.co/vientos/)
[2](https://repositorio.uniandes.edu.co/bitstreams/16889422-24b9-4034-833d-2a68ec10f20c/download)
[3](https://es.scribd.com/document/522228467/Aerodinamica-de-Una-Cometa)
[4](https://es.slideshare.net/slideshow/articulo-cientifico-de-las-cometas/250533841)
[5](https://blog.properati.com.co/agosto-tuneles-de-viento-en-bogota/)
[6](http://www.scielo.org.co/scielo.php?script=sci_arttext&pid=S1900-38032019000200286)
[7](https://www.kimerius.com/app/download/5783713555/Aspectos+f%C3%ADsicos+elementales+del+vuelo+de+las+cometas+est%C3%A1ticas+planas.pdf)
[8](https://es.wikipedia.org/wiki/Sustentaci%C3%B3n)
[9](https://www.infobae.com/colombia/2024/08/01/fuertes-vientos-de-agosto-y-fenomeno-de-la-nina-en-bogota-recomendaciones-para-prevenir-emergencias/)
[10](https://www.monografias.com/trabajos6/vuco/vuco2)
[11](https://es.weatherspark.com/y/23324/Clima-promedio-en-Bogot%C3%A1-Colombia-durante-todo-el-a%C3%B1o)
[12](https://www.andi.com.co/uploads/viento.compressed.pdf)
[13](https://es.weatherspark.com/m/23324/8/Tiempo-promedio-en-agosto-en-Bogot%C3%A1-Colombia)
[14](https://www.calculatorsconversion.com/es/calculo-de-densidad-del-aire-segun-altitud-y-temperatura/)
[15](https://visorgeo.ambientebogota.gov.co/micka/record/full/velocidad_viento)
[16](https://es.wikipedia.org/wiki/Densidad_del_aire)
[17](https://es.scribd.com/document/551292673/ESTUDIO-DE-VUELO-DE-COMETA)
[18](https://dialnet.unirioja.es/descarga/articulo/6680928.pdf)
[19](https://es.windfinder.com/windstatistics/bogota)
[20](https://brainly.lat/tarea/45360504)
[21](https://www.meteoblue.com/es/tiempo/historyclimate/climatemodelled/bogot%C3%A1_colombia_3688689)

[1](https://www.radionacional.co/cultura/tradiciones/vientos-de-agosto-en-colombia-un-fenomeno-natural-y-cultural)
[2](https://caracol.com.co/2023/08/02/por-que-hay-tanto-viento-en-el-mes-de-agosto-en-colombia/)
[3](https://www.misenal.tv/noticias/agosto-cometas-colombia-historia)
[4](https://cometasviento.blogspot.com/2018/07/las-fuerzas-aerodinamicas-del-vuelo-de.html)
[5](https://lascarolas.com/fechas-especiales/el-mes-de-las-cometas-en-colombia/)
[6](https://www.monografias.com/trabajos6/vuco/vuco2)
[7](https://www.kimerius.com/app/download/5783713555/Aspectos+f%C3%ADsicos+elementales+del+vuelo+de+las+cometas+est%C3%A1ticas+planas.pdf)
[8](https://cometasviento.blogspot.com/2017/10/la-estabilidad-del-vuelo-de-una-cometa.html)
[9](https://es.scribd.com/document/551292673/ESTUDIO-DE-VUELO-DE-COMETA)
[10](https://www.flyorange-kite.com/es/the-operating-principle-of-kites/)
[11](https://storymaps.arcgis.com/stories/1c27ed228e8443c2839807c8a2643cdd)
[12](https://www.senalmemoria.co/cometas-vuelan-agosto)
[13](https://colombia.travel/es/ferias-y-fiestas/festival-del-viento-y-de-las-cometas)
[14](https://www.senalmemoria.co/piezas/cometa-como-se-hace)
[15](https://www.ideam.gov.co/file-download/download/public/13372)
[16](https://www.colsubsidio.com/recreacion/eventos-recreativos/festival-viento)
[17](https://bdigital.upme.gov.co/bitstream/001/22/4/Upme_362_Atlas%20de%20viento%20y%20energia%20eolica.pdf)
[18](https://www.youtube.com/watch?v=CEE9N4z9ZSA)
[19](https://www.villadeleyva-boyaca.gov.co/Paginas/FESTIVAL-DEL-VIENTO-Y-LAS-COMETAS.aspx)
[20](https://www.infobae.com/colombia/2023/08/08/recomendaciones-para-volar-cometa-durante-los-vientos-de-agosto-segun-chatgpt/)
