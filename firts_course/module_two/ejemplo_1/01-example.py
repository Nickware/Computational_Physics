posiciones = [0, 0.61, 0.18, 2.13, 3.63, 6.05, 10.02, 16.54, 27.29]
tiempos = [0.0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4]

# calculate forward velocities
velocidades = []
for i in range(len(posiciones)-1):
    velocidad = (posiciones[i+1] - posiciones[i]) / (tiempos[i+1] - tiempos[i])
    velocidades.append(velocidad)

# calculate aceleraciones
aceleraciones = []
for i in range(len(velocidades)-1):
    aceleracion = (velocidades[i+1] - velocidades[i]) / (tiempos[i+2] - tiempos[i])
    aceleraciones.append(aceleracion)

# save results to file
with open("salida.txt", "w") as outfile:
    outfile.write("Tiempo\tPosicion\tVelocidad\tAceleracion\n")
    for i in range(len(posiciones)):
        outfile.write(f"{tiempos[i]}\t{posiciones[i]}\t")
        if i < len(velocidades):
            outfile.write(f"{velocidades[i]}\t")
        else:
            outfile.write("\t")
        if i < len(aceleraciones):
            outfile.write(f"{aceleraciones[i]}")
        outfile.write("\n")
