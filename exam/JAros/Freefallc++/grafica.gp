set title 'Posición vs. Tiempo'
set xlabel 'Tiempo (s)'
set ylabel 'Posicion (m)'
plot 'datos.txt' using 1:($2 >= 0 ? $2 : 2/0) with lines title 'Posicion'

set terminal png
set output 'posicion.png'
replot
set title 'Velocidad vs. Tiempo'
set xlabel 'Tiempo (s)'
set ylabel 'Velocidad (m/s)'
plot 'datos.txt' using 1:3 with lines title 'Velocidad'

set terminal png
set output 'velocidad.png'
replot
set title 'Aceleración vs. Tiempo'
set xlabel 'Tiempo (s)'
set ylabel 'Aceleración (m/s^2)'
plot 'datos.txt' using 1:4 with lines title 'Aceleracion'

set terminal png
set output 'aceleracion.png'
replot
