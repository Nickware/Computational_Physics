// Nombre: Juan Sebastian Manrique Moreno
// Curso: Física Computacional 1
// Título: freefallcode.cpp

// Se incluyen las librerías/cabeceras necesarias para ciertos comandos.
#include <iostream> // Imprime en la terminal.
#include <fstream> // Escribe datos en un archivo.
#include <vector> // Permite un mejor manejo de los vectores.
#include <stdio.h> // Necesario para manejar "printf()" y "scanf()".
#include <cmath> // Librería para matemáticas en C++.
#include <iomanip> // Necesario para manejar "setprecision()".

using namespace std; // Usando el espacio estándar para el lenguaje.

int main(){
    // Se inician los vectores.
    vector<double> y, dy;
    // Se declaran las variables necesarias, junto a las constantes.
    double g = 9.80665, deltat = 1e-12, y0, dy0; // Delta(t) muy pequeño.

    // Se piden los valores de posición y velocidad inicial.
    printf("Ingrese la posición inicial y la velocidad inicial separadas por un espacio respectivamente: ");
    scanf("%lf %lf", &y0, &dy0);
    y.push_back(y0); // Primer dato para la posición.
    dy.push_back(dy0); // Primer dato para la velocidad.

    // Enseña los valores insertados para estar al pendiente de lo que se
    // está ejecutando dentro del programa.
    printf("Los valores de posición y velocidad inicial ingresados son: %lf m y %lf m/s, respectivamente.\n", y[0], dy[0]);

    // Abre los archivos tanto para guardar los datos, como para crear
    // las gráficas con el aplicativo "gnuplot".
    ofstream archivo("datos.txt", ios::trunc);
    ofstream archivoplot("graph.gp", ios::trunc);

    // Si alguno de los archivos no fueron abiertos correctamente, termina
    // el programa y arroja un error.
    if (!archivo.is_open() && !archivoplot.is_open()){
        printf("Error al abrir algún archivo necesario para la ejecución del programa, por favor, vuelva a ejecutar.");
        return 1;
    }

    /*
    El siguiente ciclo es el que lleva a cabo la labor de aplicar el
    método de diferencias finitas, dentro de las condiciones para el ciclo
    se comienza declarando la variable entera "i" la cual nos ayudará a la
    hora de registrar los datos en los diferentes vectores. La condición
    principal dentro del ciclo es que la posición sea diferente de cero,
    como esta disminuye para nuestro caso (caída libre), entonces cuando
    esta sea negativa, es porque ya se llegó al suelo, y ahí termina el
    ciclo.

    Respecto a cómo fue empleado el método de diferencias finitas, se
    tomaron los valores de posición inicial y velocidad inicial queriendo
    hallar el siguiente valor, es decir, para una posición i = 1. Luego,
    simplemente usando para las siguientes iteraciones el valor anterior,
    se puede obtener los datos para posición y velocidad para graficarlos.
    */
    for (int i = 0; y[i] >= 0; i++){
        archivo << setprecision(15) << deltat*(i) << "\t";
        y.push_back(y[i] + dy[i]*(deltat));
        archivo << setprecision(15) << y[i] << "\t";
        dy.push_back(dy[i] - g*(deltat));
        archivo << setprecision(15) << dy[i] << endl;
    }

    // Código enviado al script de gnuplot y que pueda graficar.
    archivoplot << "reset\n";
    archivoplot << "set title 'Posición vs. Tiempo' font 'Times New Roman,12'\n";
    archivoplot << "set xlabel 'Tiempo' font 'Times New Roman,12'\n";
    archivoplot << "set ylabel 'Posición' font 'Times New Roman,12'\n";
    archivoplot << "set xtics font 'Times New Roman,11'\n";
    archivoplot << "set ytics font 'Times New Roman,11'\n";
    archivoplot << "plot 'datos.txt' using 1:2 w lp notitle\n";
    archivoplot << "set terminal png\n";
    archivoplot << "set output 'position.png'\n";
    archivoplot << "replot\n";
    archivoplot << "reset\n";
    archivoplot << "set title 'Velocidad vs. Tiempo' font 'Times New Roman,12'\n";
    archivoplot << "set xlabel 'Tiempo' font 'Times New Roman,12'\n";
    archivoplot << "set ylabel 'Velocidad' font 'Times New Roman,12'\n";
    archivoplot << "set xtics font 'Times New Roman,11'\n";
    archivoplot << "set ytics font 'Times New Roman,11'\n";
    archivoplot << "plot 'datos.txt' using 1:3 w lp notitle\n";
    archivoplot << "set terminal png\n";
    archivoplot << "set output 'velocity.png'\n";
    archivoplot << "replot";
    
    // Se cierran ambos archivos.
    archivo.close();
    archivoplot.close();

    // Y finalmente se ejecuta el script de gnuplot y se termina el programa.
    system("gnuplot graph.gp");

    return 0;
}