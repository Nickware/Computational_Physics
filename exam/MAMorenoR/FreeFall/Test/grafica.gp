set title 'Posición vs. Tiempo'
set xlabel 'Tiempo'
set ylabel 'Posicion'
plot 'datos.txt' using 1:2 with lines title 'Posicion'

set terminal png
set output 'posicion.png'
replot
set title 'Velocidad vs. Tiempo'
set xlabel 'Tiempo'
set ylabel 'Velocidad'
plot 'datos.txt' using 1:3 with lines title 'Velocidad'

set terminal png
set output 'velocidad.png'
replot
