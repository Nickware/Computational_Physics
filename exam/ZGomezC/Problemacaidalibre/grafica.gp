set title 'Posición vs. Tiempo'
set xlabel 'Tiempo'
set ylabel 'Posicion'
plot 'datos1.txt' using 1:2 with lines title 'Posicion'

set terminal png
set output 'posicion.png'
replot
set title 'Velocidad vs. Tiempo'
set xlabel 'Tiempo'
set ylabel 'Velocidad'
plot 'datos1.txt' using 1:3 with lines title 'Velocidad'

set terminal png
set output 'velocidad.png'
replot
set title 'Aceleración vs. Tiempo'
set xlabel 'Tiempo'
set ylabel 'Aceleración'
plot 'datos1.txt' using 1:4 with lines title 'Aceleracion'

set terminal png
set output 'aceleracion.png'
replot
