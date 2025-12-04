# Caso de estudio  **riesgo de inversión** en Argentina

**Argentina es un caso de estudio fascinante** para analizar **riesgo de inversión** (no solo crediticio) en un contexto de alta volatilidad macroeconómica, inestabilidad política y crisis recurrentes. Su situación actual (2023-2024) ofrece un laboratorio vivo de cómo estos factores se combinan para disuadir o distorsionar las inversiones. Veamos:

---

### **1. Variables Clave que Afectan el Riesgo de Inversión en Argentina**  
#### **A. Crisis Macroeconómica Estructural**  
- **Inflación galopante**: +200% interanual (2023), la más alta desde 1991.  
  - Efecto: Destruye el valor real de los activos y contratos en pesos.  
- **Déficit fiscal crónico**: El Estado gasta más de lo que recauda, financiándose con emisión monetaria.  
- **Control de capitales**: Restricciones para acceder a dólares (cepo cambiario), lo que genera múltiples tipos de cambio paralelos.  

#### **B. Inestabilidad Política y Regulatoria**  
- **Cambios bruscos de políticas**:  
  - Ejemplo: Nacionalización de YPF (2012), medidas proteccionistas, fluctuaciones entre liberalismo e intervencionismo.  
- **Riesgo de default soberano**: Argentina ha entrado en default 9 veces en su historia (la última en 2020).  
- **Incertidumbre electoral**: Las elecciones (como las de 2023) suelen generar volatilidad en mercados.  

#### **C. Mercado Financiero Distorsionado**  
- **Brecha cambiaria**: El dólar oficial ($350 ARS en 2023) vs. paralelo ($1000 ARS) crea arbitrajes y especulación.  
- **Bonos en dólares con descuentos brutales**: Ejemplo: Bonos AL30 cotizando a ~30% de su valor nominal (2023), reflejando escepticismo sobre pagos futuros.  

---

### **2. ¿Cómo se Modela el Riesgo de Inversión?**  
El **decaimiento exponencial** puede adaptarse para representar la **pérdida de valor de los activos** en este entorno:  

#### **Fórmula Ajustada**  
$\[V(t) = V_0 \cdot e^{-(\lambda_{\text{econ}} + \lambda_{\text{pol}} + \lambda_{\text{reg}}) \cdot t},\$]
donde:  
- $\( \lambda_{\text{econ}} \$): Tasa de deterioro por inflación y recesión.  
- $\( \lambda_{\text{pol}} \$): Incremento por inestabilidad política (ej: elecciones, protestas).  
- $\( \lambda_{\text{reg}} \$): Riesgo regulatorio (ej: impuestos a exportaciones, controles de precios).  

**Ejemplo**:  
- Si un proyecto de energía renovable tiene $\( V_0 = \$100M \$) y \$( \lambda_{\text{total}} = 0.2 \$) (20% de pérdida anual por riesgos combinados), en 3 años valdrá:  
  $\[V(3) = 100 \cdot e^{-0.2 \times 3} \approx \$54.9M.\$]

---

### **3. Casos Reales de Inversiones Afectadas**  
| **Sector**      | **Riesgo Específico**                   | **Ejemplo**                                                  |
| --------------- | --------------------------------------- | ------------------------------------------------------------ |
| **Energía**     | Nacionalización/regulación cambiaria    | Vaca Muerta: Inversiones retrasadas por controles de precios y falta de dólares. |
| **Agricultura** | Retenciones a exportaciones (impuestos) | Sojeros desincentivados por derechos de exportación del 33%. |
| **Tech**        | Restricciones para repatriar ganancias  | Startups que migran a Uruguay o Paraguay para evitar el cepo. |

---

### **4. Datos Duros (2023-2024)**  
- **Fuga de capitales**: USD 100,000 millones en la última década (BCRA).  
- **Riesgo país (EMBI+)**: +2000 puntos (vs. ~100 para Chile), indicando alta percepción de default.  
- **Inversión Extranjera Directa (IED)**: Solo USD 6,500M en 2022 (vs. USD 45,000M en Brasil).  

---

### **5. Estrategias de Inversión en este Contexto**  
Los inversores usan tácticas no convencionales:  
1. **Coberturas cambiarias**: Compra de dólar futuro o cripto (USDT) para eludir el cepo.  
2. **Activos dolarizados**: Invertir en propiedades o commodities con precios atados al USD.  
3. **Bonos de alto riesgo**: Especular con deuda en default (ej: bonos argentinos a 10-20 centavos por dólar).  

---

### **6. Resultado**  
Ejecutar via terminal
```bash
python loss_argentina.py
```
- La inversión pierde ~50% de su valor en 3 años.  

---

### **7. ¿Por Qué Argentina Sigue Atrayendo Inversiones?**  
A pesar de todo, algunos inversores asumen riesgos por:  
- **Recursos naturales**: Litio en Salta, shale oil en Vaca Muerta.  
- **Mano de obra calificada**: Sector IT competitivo.  
- **Activos baratos**: Compra de empresas en quiebra a precios de remate.  

---

### **Conclusión**  
Argentina es un **caso extremo de riesgo no lineal**, donde el modelo exponencial clásico debe combinarse con:  
- **Saltos discretos** (ej: devaluaciones bruscas).  
- **Teoría de juegos** (anticipar movimientos del gobierno).  
- **Análisis de redes** (cómo el riesgo se propaga entre sectores).  
