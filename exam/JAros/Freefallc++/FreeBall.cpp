//Title: Freefall ideal case
//Author: Julian Aros
//Date: april 8, 2023

//Cargamos las librerias
#include <iostream>
#include <fstream>
#include <cmath>

//utilizamos el espacio de nombres std de la biblioteca estándar de C++
using namespace std;
//Funcion principal del programa y el cuerpo del programa
int main() {

    //Definimos las variables
    double g; //gravedad
    double h; //Tamaño de paso
    double t_1; //Tiempo maximo
    double t; //Tiempo de la condicion inicial
    double y; //Altura de la condicion inicial
    double v; //Rapidez de la condicion inicial

    //Solicita al usuario el valor de la gravedad, el tamaño de paso, el tiempo de la condicion inial
    //el tiempo maximo, la altura de la condición inicial y la velocidad de la condicion inicial


    do {
        cout << "Ingrese el valor de la gravedad (m/s^2). Tenga en cuenta que dicho valor es negativo: ";
        cin >> g;
        if (g > 0) {
        cout << "Recuerde que la gravedad debe ser negativa, desde el punto de vista vectorial. " << endl;
        }
    }
    while (g > 0);
    
    do {
        cout << "Ingrese el tamaño de paso h para el tiempo. Entre más pequeño mejor: ";
        cin >> h;
        if (h <= 0)
        {
            cout <<"El tamaño de paso h debe ser mayor cero" << endl;
        }
        
    }
    while (h <= 0);


    do {
        cout << "Ingrese el tiempo de su condicion inicial, tenga en cuenta que debe ser menor al tiempo maximo (s): ";
        cin >> t;
        if (t < 0) {
        cout << "El tiempo debe ser mayor o igual a cero. En física no tiene mucho sentido tiempos negativos" << endl;
        }
    }
    while (t < 0);
    
    
    do {
    cout << "Ingrese el tiempo máximo (s): ";
    cin >> t_1; 
    } 
    while (t_1 <= t); // mientras t_1 sea menor o igual a t, se seguirá pidiendo al usuario que ingrese el valor de t_1

    do {
        cout << "Ingrese la altura de su condicion inicial (m): ";
        cin >> y;
        if (y < 0)
        {
            cout << " En Física no tiene mucho sentido posiciones negativas" << endl;
        }
        
    }
    while (y < 0);
        
    do{
        cout << "Ingrese la rapidez  de su condicion inicial (m/s): ";
        cin >> v;
        if (v < 0)
        {
            cout << "En Física no tiene mucho sentido tratar la rapidez como una cantidad vectorial" << endl;
        }
        
    }
    while (v < 0);
    
    int n_pasos = t_1 / h;  // calcula el número de pasos requeridos

    ofstream file("datos.txt");  // crea un archivo para guardar los datos
    file << t << " " << y << " " << v << " " << g << endl;  // guarda los datos iniciales

    for (int i = 1; i <= n_pasos; i++) {  // iteramos dependiendo del tiempo max que quiere ver el usuario veces (el tamaño depende de lo que elijamos)
        t += h;
        y += h * v;
        v += h * g;

        file << t << " " << y << " " << v << " " << g << endl;  // guarda los datos actualizados
    }

    file.close();  // cierra el archivo

    ofstream gnuarchivo("grafica.gp"); //Se crea un archivo gnuplot
     gnuarchivo << "set title 'Posición vs. Tiempo'\n";
     gnuarchivo << "set xlabel 'Tiempo (s)'\n";
     gnuarchivo << "set ylabel 'Posicion (m)'\n";
     gnuarchivo << "plot 'datos.txt' using 1:($2 >= 0 ? $2 : 2/0) with lines title 'Posicion'\n\n"; //Restringimos la graficacion de posiciones negativas
     gnuarchivo << "set terminal png\n";
     gnuarchivo << "set output 'posicion.png'\n";
     gnuarchivo << "replot\n";     
     gnuarchivo << "set title 'Velocidad vs. Tiempo'\n";
     gnuarchivo << "set xlabel 'Tiempo (s)'\n";
     gnuarchivo << "set ylabel 'Velocidad (m/s)'\n";
     gnuarchivo << "plot 'datos.txt' using 1:3 with lines title 'Velocidad'\n\n";
     gnuarchivo << "set terminal png\n";
     gnuarchivo << "set output 'velocidad.png'\n";
     gnuarchivo << "replot\n"; 
     gnuarchivo << "set title 'Aceleración vs. Tiempo'\n";
     gnuarchivo << "set xlabel 'Tiempo (s)'\n";
     gnuarchivo << "set ylabel 'Aceleración (m/s^2)'\n";
     gnuarchivo << "plot 'datos.txt' using 1:4 with lines title 'Aceleracion'\n\n";
     gnuarchivo << "set terminal png\n";
     gnuarchivo << "set output 'aceleracion.png'\n";
     gnuarchivo << "replot\n";
     
     gnuarchivo.close();


     // ejecuta gnuplot para generar las graficas
     system("gnuplot grafica.gp");



    return 0;

}