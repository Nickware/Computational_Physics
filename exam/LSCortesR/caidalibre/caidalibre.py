#Programa para hallar las velocidades y posiciones de la caida libre teniendo condiciones iniciales
#Laura Sofia Cortes Rodriguez 20202107049
import matplotlib.pyplot as plt       #imprtar librerias
import matplotlib
matplotlib.use('Qt5Agg')    #permite mostrar las graficas
#Definición de las variables
g=float(input('Ingrese magnitud de la aceleración de la gravedad:')) # aceleración de la gravedad
y0=float(input('Ingrese posicion inicial:')) # posición inicial
t0=float(input('Ingrese tiempo inicial:')) # tiempo inicial
tf=float(input('Ingrese tiempo final:')) # tiempo final
dt=float(input('Ingrese paso de tiempo:')) # paso de tiempo

#Función para calcular la posición y velocidad en la caída libre
def caida_libre(g, y0, t0, tf, dt):
    t = [t0]         #lista tiempo
    y = [y0]         #lista posicion
    v = [0]          #lista velocidad

    while t[-1] < tf:       #bucle while, mientras que el ultimo dato de la lista de tiempos sea menor que el tiempo final, haga lo siguiente
        #Calcular la velocidad y posición en el siguiente instante de tiempo
        v_nuevo=v[-1]-g*dt       #ecuacion de velocidad
        y_nuevo=y[-1]+v[-1]*dt   #ecuacion de posicion
        
        #Añadir los valores nuevos a las listas
        v.append(v_nuevo)     #lista de velocidad
        y.append(y_nuevo)     #lista de posicion
        t.append(t[-1] + dt)  #lista de tiempo

    #Guardar los datos en un archivo de texto
    with open("salidapy.txt", "w") as f:   #abrir archivo txt en modo escritura y lo asigna a la variable f
        for i in range(len(t)):   #bucle for para iterar los datos de t
            f.write(f"{t[i]}\t{y[i]}\t{v[i]}\n")   #Escribe las listas de t, y, v en el txt

    #Graficar la posición y velocidad en función del tiempo
    plt.subplot(2, 1, 1)    #crea una grafica 
    plt.plot(t, y)          #grafica y versus t
    plt.xlabel("tiempo")   #titulo del eje x:tiempo
    plt.ylabel("posición")  #titulo del eje y:posicion

    plt.subplot(2, 1, 2)      #crea otra grafica
    plt.plot(t, v)         #grafica v versus t
    plt.xlabel("tiempo")   #titulo eje x:tiempo
    plt.ylabel("velocidad")  #titulo eje y:velocidad

    plt.show()    #muestra la grafica

caida_libre(g, y0, t0, tf, dt)    #corre la funcion de caida libre
