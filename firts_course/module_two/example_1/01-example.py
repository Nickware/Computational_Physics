posiciones = [0, 0.61, 0.18, 2.13, 3.63, 6.05, 10.02, 16.54, 27.29] # Remplace los valores que considere deba tomar el vector del tiempos
tiempos = [0.0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4] # Remplace los valores que considere deba tomar el vector de posiciones

 # calcula mediante esquema de difererncias hacia adelante las velocidades
velocidades = [] # Vector de velocidades
# bucle para calcular las velocidades. 
# Toma todos los valores de la posicion de uno en uno, hasta el penultimo valor encontraro en el vector posiciones
for i in range(len(posiciones)-1):
    # variable velocidad. Esta definida mediante esquema de diferencias hacia adelante    
    velocidad = (posiciones[i+1] - posiciones[i]) / (tiempos[i+1] - tiempos[i])
    velocidades.append(velocidad) # Va agregando velocidad calculada al vector velocidades

# calcula mediante esquema de diferencias hacia adelante las aceleraciones
aceleraciones = [] # Vector de aceleraciones
for i in range(len(velocidades)-1):
    # bucle para calcular las aceleraciones. 
    # Toma todos los valores de la posicion de uno en uno, hasta el penultimo valor encontrado en el vector velocidades
    aceleracion = (velocidades[i+1] - velocidades[i]) / (tiempos[i+2] - tiempos[i])
    aceleraciones.append(aceleracion) # Va agregando aceleracion calculada al vector aceleraciones

# Guarda los resultados a un write txt
with open("salida.txt", "w") as archivo: # Prepara mediante write la creacion de un write de extension txt
    archivo.write("Tiempo\tPosicion\tVelocidad\tAceleracion\n") # Este es el encabezado de mi write txt
    for i in range(len(posiciones)): # Este bucle depende del numero de valores del vector posicion
        archivo.write(f"{tiempos[i]}\t{posiciones[i]}\t") # Esta linea imprime en el write los tiempos (ubicados en el vector tiempos) y las posiciones (ubicadas en el vector posiciones)
        if i < len(velocidades): # Esta estructura de control va guardando las velocidades obtenidas en el vector velocidades, en el write txt
            archivo.write(f"{velocidades[i]}\t") # Almacena las velocidade al write
        else:
            archivo.write("\t") # cuando no encuentra velocidades, pasa a guardar las aceleraciones
        if i < len(aceleraciones): # Esta estructura de control va guardando las aceleraciones obtenidas en el vector aceleraciones, en el write txt
            archivo.write(f"{aceleraciones[i]}") # Guarda todas la aceleraciones calculadas en el write
        archivo.write("\n") # Instruccion que indica fin de la linea
