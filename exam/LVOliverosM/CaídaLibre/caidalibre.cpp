//Laura V. Oliveros M.
//Física Computacional 1

//Librerías:

#include <iostream>  // Facilita las operaciones de entrada y sálida de datos
#include <fstream>   // Manejo de archivos: abrir, cerrar, leer, escribir, crear, eliminar
#include <vector>    // Permite almacenar y manipular conjunto de datos en la memoria
#include <string>    // Manipulación de cadenas
#include <iomanip>   // Sálida de datos: precisión en los decimales, ancho del campo, etc.

using namespace std;

    int main() {

    float g = 9.807, dt = 0.01; // g = valor de la gravedad, dt = paso en el tiempo,
    int N = 100; // N = num. de instantes en el tiempo
    

    double y[N], v[N], t[N]; // Arreglos para almacenar la posición y velocidad
    y[0] = 2; // Posición inicial
    v[0] = 0; // Velocidad inicial
    t[0] = 0; // Tiempo inicial

    // Calcular la posición y velocidad de la partícula en cada instante de tiempo
    for (int i = 1; i < N; i++) {
        y[i] = y[i-1] + v[i-1]*dt; // Posición en el instante i
        v[i] = v[i-1] - g*dt; // Velocidad en el instante i
        t[i] = t[i-1] + dt; // Instante de tiempo
    }

    // Abrir un archivo de texto para guardar los valores de la posición y velocidad
    ofstream archivo("datoscl.txt");
    if (archivo.is_open()) {
        // Escribir las cabeceras de las columnas en el archivo
        archivo << "Tiempo\tPosición\tVelocidad\n";
        // Guardar los valores positivos de la posición en el archivo de texto
        for (int i = 0; i < N; i++) {
            if (y[i] >= 0) {
                archivo << t[i] << "\t" << y[i] << "\t\t" << v[i] << endl;
            }
        }
    }
    archivo.close(); // Cerrar el archivo


    // Crea un archivo script gnuplot
     ofstream gnuarchivo("graficascl.gp");
     gnuarchivo << "set title 'Posición vs. Tiempo'\n";
     gnuarchivo << "set xlabel 'Tiempo'\n";
     gnuarchivo << "set ylabel 'Posicion'\n";
     gnuarchivo << "plot 'datoscl.txt' using 1:2 with lines title 'Posicion'\n\n";
     gnuarchivo << "set terminal png\n";
     gnuarchivo << "set output 'posicioncl.png'\n";
     gnuarchivo << "replot\n";     
     gnuarchivo << "set title 'Velocidad vs. Tiempo'\n";
     gnuarchivo << "set xlabel 'Tiempo'\n";
     gnuarchivo << "set ylabel 'Velocidad'\n";
     gnuarchivo << "plot 'datoscl.txt' using 1:3 with lines title 'Velocidad'\n\n";
     gnuarchivo << "set terminal png\n";
     gnuarchivo << "set output 'velocidadcl.png'\n";
     gnuarchivo << "replot\n"; 

     gnuarchivo.close();

     // Ejecuta gnuplot para generar las graficas
     system("gnuplot graficascl.gp");
    
    return 0;
}