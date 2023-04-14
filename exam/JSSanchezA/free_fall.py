#########Caída libre (Cálculo y Gráficos)##############
#User: Juan Sebastián Sánchez
#Username:SolarPunk
#version 1.0

#Se importan las librerias con "import libreria as apodo"
import decimal
import matplotlib.pyplot as plt

# Definir las constantes
g = decimal.Decimal('-9.81')
delta_t = decimal.Decimal('0.000000001')

#Solicitar al usuario que ingrese la cantidad de tiempo que desea medir
tiempo_total = int(input("Ingrese la cantidad de segundos que desea medir: "))
lista_segundos = list(range(1, tiempo_total+1))

##########Calcular las posiciones iniciales y actuales############
#Crear dos listas vacías, una para almacenar las posiciones instantáneas con los tiempos iniciales y otra para almacenar las posiciones instantáneas con los tiempos actualizados con el delta.
posiciones_iniciales = []
posiciones_actualizadas = []

#Usar un ciclo for para medir los segundos y agregarlos a la lista.
for tiempo in lista_segundos:
    tiempo_decimal = decimal.Decimal(str(tiempo))
##############CÁLCULO POSICIONES EN Y ############    
    posiciones_iniciales.append((g * tiempo_decimal * tiempo_decimal) / 2)
    posiciones_actualizadas.append((g * (tiempo_decimal + delta_t) * (tiempo_decimal + delta_t)) / 2)

# Calcular las velocidades instantáneas
velocidades = []
for i in range(len(posiciones_actualizadas)):
    vel = (posiciones_actualizadas[i] - posiciones_iniciales[i]) / delta_t
    velocidades.append(vel)

# Imprimir los resultados
print("Posiciones iniciales:", posiciones_iniciales)
print("Posiciones actualizadas:", posiciones_actualizadas)
print("Velocidades instantáneas:", velocidades)

lista_velocidades = [(posiciones_actualizadas[i]-posiciones_iniciales[i])/delta_t for i in range(len(posiciones_iniciales))]

# Crear listas de tiempos y velocidades
tiempos = lista_segundos
velocidades = lista_velocidades

# Trazar la gráfica de la velocidad en función del tiempo
plt.plot(tiempos, velocidades)

# Darle nombre a los ejes
plt.xlabel('Tiempo (s)')
plt.ylabel('Velocidad (m/s)')

# Mostrar la gráfica
plt.show()
#Gráfica posición
plt.plot(lista_segundos, posiciones_iniciales, label='Posición')
plt.xlabel('Tiempo (s)')
plt.ylabel('Posición (m)')
plt.title('Posición en función del tiempo')
plt.legend()
plt.show()

