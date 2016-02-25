from numpy import sin,pi,linspace
from pylab import plot,show,subplot

a = [1,3,5,3] # plotting the curves for
b = [1,5,7,4] # different values of a/b
delta = pi/2
t = linspace(-pi,pi,300)

for i in range(0,4):
 x = sin(a[i] * t + delta)
 y = sin(b[i] * t)
 subplot(2,2,i+1)
 plot(x,y)

show()
