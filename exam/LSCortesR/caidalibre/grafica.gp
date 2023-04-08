set title 'y vs. t'
set xlabel 't'
set ylabel 'y'
plot 'salidacpp.txt' using 1:2 with lines title 'y'

set terminal png
set output 'posicion.png'
replot
set title 'v vs. t'
set xlabel 't'
set ylabel 'v'
plot 'salidacpp.txt' using 1:3 with lines title 'v'

set terminal png
set output 'velocidad.png'
replot
