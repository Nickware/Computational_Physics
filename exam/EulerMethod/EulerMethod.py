y0=float(input('ingrese la posición inicial y0='))
v0=float(input('ingrese la velocidad inicial v0='))
h=float(input('ingrese el tiempo inicial t0='))
g=9.8

t=[h]
ya=[y0]
va=[v0]
ve=[v0]
ye=[y0]
i=0


while ya[i]>0:
    h=h+0.01
    t.append(h)
    i=i+1
    c=-g*t[i]**2/2+t[i]*v0+y0
    if c<0:
        c=0
        ya.append(c)
        d=v0-g*t[i]
        va.append(d)
        e=ve[i-1]-g*0.01
        ve.append(e)
        f=ye[i-1]+0.01*ve[i]
        if f<0:
            f=0
            ye.append(f)
        else:
            ye.append(f)
    else:
        ya.append(c)
        d=v0-g*t[i]
        va.append(d)
        e=ve[i-1]-g*0.01
        ve.append(e)
        f=ye[i-1]+0.01*ve[i]
        if f<0:
            f=0
            ye.append(f)
        else:
            ye.append(f)
    


with open("salida.txt", "w") as archivo: # Prepara mediante write la creacion de un write de extension txt
    archivo.write("Tiempo\tya\tva\tve\tye\n") # Este es el encabezado de mi write txt
    for i in range(len(ya)): # Este bucle depende del numero de valores del vector posicion
        archivo.write(f"{t[i]}\t{ya[i]}\t") # Esta linea imprime en el write los tiempos (ubicados en el vector tiempos) y las posiciones (ubicadas en el vector posiciones)
        if i < len(va): # Esta estructura de control va guardando las velocidades obtenidas en el vector velocidades, en el write txt
            archivo.write(f"{va[i]}\t") # Almacena las velocidade al write
        else:
            archivo.write("\t") # cuando no encuentra velocidades, pasa a guardar las aceleraciones
        if i < len(ve): # Esta estructura de control va guardando las aceleraciones obtenidas en el vector aceleraciones, en el write txt
            archivo.write(f"{ve[i]}\t") # Guarda todas la aceleraciones calculadas en el write
        if i < len(ye): # Esta estructura de control va guardando las aceleraciones obtenidas en el vector aceleraciones, en el write txt
            archivo.write(f"{ye[i]}") # Guarda todas la aceleraciones calculadas en el write
        archivo.write("\n") # Instruccion que indica fin de la linea

