import numpy as np
import matplotlib.pyplot as plt
y0=float(input('ingrese la posición inicial y0='))
v0=float(input('ingrese la velocidad inicial v0='))
h=float(input('ingrese el tiempo inicial t0='))
w=float(input('Paso ='))
g=9.8

t=[h]
ya=[y0]
va=[v0]
ve=[v0]
ye=[y0]
i=0


while ya[i]>0: 
    h=h+w
    t.append(h)
    i=i+1
    c=-g*t[i]**2/2+t[i]*v0+y0
    if c<0:
        c=0
        ya.append(c)
        d=v0-g*t[i]
        va.append(d)
        e=ve[i-1]-g*w
        ve.append(e)
        f=ye[i-1]+w*ve[i]
        if f<0:
            f=0
            ye.append(f)
        else:
            ye.append(f)
    else:
        ya.append(c)
        d=v0-g*t[i]
        va.append(d)
        e=ve[i-1]-g*w
        ve.append(e)
        f=ye[i-1]+w*ve[i]
        if f<0:
            f=0
            ye.append(f)
        else:
            ye.append(f)
    


with open("ya.txt", "w") as archivo: 
    for i in range(len(ya)): 
        archivo.write(f"{t[i]}\t,{ya[i]}\t") 
        archivo.write("\n") 

x, y = np.loadtxt('ya.txt', delimiter=',', unpack=True)

plt.plot(x,y, label='Gráfica')

 
plt.xlabel('t')
plt.ylabel('Posición Analítica ya(t)')
plt.legend()
plt.show()


with open("va.txt", "w") as archivo: 
    for i in range(len(va)): 
        archivo.write(f"{t[i]}\t,{va[i]}\t") 
        archivo.write("\n") 

z, w = np.loadtxt('va.txt', delimiter=',', unpack=True)

plt.plot(z,w, label='Gráfica')

 
plt.xlabel('t')
plt.ylabel('Velocidad Analítica va(t)')
plt.legend()
plt.show()

with open("ve.txt", "w") as archivo: 
    for i in range(len(ve)): 
        archivo.write(f"{t[i]}\t,{ve[i]}\t") 
        archivo.write("\n") 

a, b = np.loadtxt('va.txt', delimiter=',', unpack=True)

plt.plot(a,b, label='Gráfica')

 
plt.xlabel('t')
plt.ylabel('Velocidad Método de Euler ve(t)')
plt.legend()
plt.show()

with open("ye.txt", "w") as archivo: 
    for i in range(len(ye)): 
        archivo.write(f"{t[i]}\t,{ye[i]}\t") 
        archivo.write("\n") 

c, d = np.loadtxt('ye.txt', delimiter=',', unpack=True)

plt.plot(c,d, label='Gráfica')

 
plt.xlabel('t')
plt.ylabel('Posición Método de Euler ye(t)')
plt.legend()
plt.show()
