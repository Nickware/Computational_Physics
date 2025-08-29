

# Decrecimiento Exponencial aplicado al **riesgo crediticio**

El modelo de **decaimiento exponencial** (y sus variantes) puede aplicarse al **riesgo crediticio**, especialmente cuando se incorporan variables **socioeconómicas** y **políticas de Estado**. A continuación se explica cómo se adapta este enfoque, con ejemplos concretos y herramientas para modelarlo.

---

## **1. Riesgo Crediticio: Decaimiento Exponencial en Probabilidad de Default**
En finanzas, la probabilidad de que un deudor incumpla (**default**) puede modelarse como un proceso de decaimiento, donde la "supervivencia" del crédito depende de factores económicos y políticos.

### **Modelo Básico (Sin Variables Externas)**
- **Fórmula**:  
  \[
  P_{\text{surv}}(t) = e^{-\lambda t}
  \]
  - \( P_{\text{surv}}(t) \): Probabilidad de que el crédito siga vigente en el tiempo \( t \).  
  - \( \lambda \): Tasa de riesgo constante (similar a la vida media radiactiva).  

- **Ejemplo**:  
  Si un préstamo tiene \( \lambda = 0.1 \) (10% de probabilidad de default anual), la probabilidad de que **no haya default** en 5 años es:  
  \[
  P_{\text{surv}}(5) = e^{-0.1 \times 5} \approx 60.7\%.
  \]

### **Limitación**:  
Este modelo supone que \( \lambda \) es constante, pero en la realidad, el riesgo crediticio depende de:  
- Crisis económicas.  
- Cambios regulatorios.  
- Inestabilidad política.  

---

## **2. Incorporando Variables Socioeconómicas y Políticas**
Para hacer el modelo más realista, \( \lambda \) debe ser una **función dinámica** de variables externas.  

### **Variables Clave**  
| Variable                   | Efecto en \( \lambda \) (Tasa de Default)  | Ejemplo de Impacto                            |
| -------------------------- | ------------------------------------------ | --------------------------------------------- |
| **Desempleo (%)**          | Aumenta \( \lambda \)                      | +5% desempleo → \( \lambda \uparrow \)        |
| **PIB per cápita**         | Disminuye \( \lambda \)                    | Recesión → \( \lambda \uparrow \)             |
| **Tasa de interés**        | Aumenta \( \lambda \) (más carga de deuda) | Subida de tasas → \( \lambda \uparrow \)      |
| **Inestabilidad política** | Aumenta \( \lambda \) (riesgo país)        | Golpe de Estado → \( \lambda \uparrow \)      |
| **Regulación financiera**  | Puede aumentar o disminuir \( \lambda \)   | Leyes pro-deudores → \( \lambda \downarrow \) |

### **Modelo Ajustado**  
\[
\lambda(t) = \lambda_0 + \beta_1 X_1(t) + \beta_2 X_2(t) + \dots + \beta_n X_n(t),
\]  
donde:  
- \( \lambda_0 \): Riesgo base.  
- \( X_i(t) \): Variables socioeconómicas/políticas en el tiempo \( t \).  
- \( \beta_i \): Peso de cada variable (se estima con datos históricos).  

**Ejemplo**:  
\[
\lambda(t) = 0.05 + 0.02 \times \text{Desempleo}(t) + 0.01 \times \text{InestabilidadPolítica}(t).
\]  
- Si el desempleo sube al 10% y hay inestabilidad política (valor = 1), entonces:  
  \[
  \lambda = 0.05 + 0.02 \times 10 + 0.01 \times 1 = 0.26 \quad (26\% \text{ de default anual}).
  \]

---

## **3. Aplicación en Datos Reales: Crisis Argentina (2001)**
### **Variables Consideradas**  
- **Desempleo**: Subió del 12% al 21%.  
- **Devaluación del peso**: +200%.  
- **Corralito financiero**: Restricción de retiros bancarios.  

### **Resultado**:  
- El \( \lambda \) se disparó, llevando a una **ola de defaults** en créditos y bonos soberanos.  
- Modelos avanzados (como **Merton con variables macro**) hubieran predicho el colapso.  

## **4. Extensiones del Modelo**  
1. **Redes Neuronales**: Para capturar interacciones no lineales entre variables.  
2. **Cadenas de Markov**: Modelar transiciones entre estados de riesgo (ej: de "bajo riesgo" a "default").  
3. **Teoría de Juegos**: Incluir estrategias de deudores y acreedores.  

---

## **Conclusión**  
El modelo de decaimiento exponencial es útil para riesgo crediticio, pero debe **ajustarse con variables macro**. Países con inestabilidad política (ej: Venezuela) o crisis económicas (ej: Grecia 2010) muestran cómo el riesgo puede dispararse en forma no lineal.  
