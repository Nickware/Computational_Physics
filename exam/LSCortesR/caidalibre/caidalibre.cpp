//Programa para hallar las velocidades y posiciones de la caida libre teniendo condiciones iniciales
//Laura Sofia Cortes Rodriguez 20202107049
#include <iostream>    
#include <fstream>
#include <vector>
#include <cmath>             //importar librerias necesarias
#include <string>
#include <iomanip>  

using namespace std;

//Define función que calcula la posición de la caída libre
double calcular_y(double y0, double v0, double t, double g) {
    return y0+v0*t;        //ecuacion de posicion
}

//Definine función que calcula la velocidad de la caída libre
double calcular_v(double v0, double t, double g) {
    return -g*t;        //ecuacion de velocidad
}

int main() {   //inicio
    //Insertar y definir condiciones iniciales
    double g; //gravedad, variable double
        cout << "Introducir aceleracion de la gravedad: ";     //pregunta insertar gravedad
        cin >> g;          //define lo escrito como g
    double y0;  //posicion inicial
        cout << "Introducir posicion inicial: ";
        cin >> y0;    //define lo escrito como y0
    double v0=0;  //la velocidad inicial es por defecto 0
    double t0;    //tiempo inicial
        cout << "Introducir tiempo inicial: ";
        cin >> t0;  //define lo escrito como t0...
    double tf;
        cout << "Introducir tiempo final: ";
        cin >> tf;
    double dt;
        cout << "Introducir paso de tiempo: ";
        cin >> dt;

    //Se define variables como las iniciales
    double tactual=t0;             //el tiempo inicial es igual al tiempo actual
    double yactual=y0;              //la posicion inicial es igual a la posicion actual
    double vactual=v0;              //la velocidad inicial es igual a la velocidad actual

    //Listas para almacenar los datos
    vector<double> t;   //crea lista de t
    vector<double> y;   //crea lista de y
    vector<double> v;   //crea lista de v

    //Bucle while que calcula y agrega a las listas las posicones y velocidades y para cuanto t=tf
    while (tactual<=tf) {
        t.push_back(tactual);          //agrega valores de t a la lista
        y.push_back(yactual);       //agrega valores de y a la lista
        v.push_back(vactual);       //agrega valores de v a la lista

        //Calcular la nueva posición y velocidad
        yactual=calcular_y(yactual, vactual, tactual, g);
        vactual=calcular_v(vactual, tactual, g);

        tactual += dt;        //Sumar el paso al tiempo actual
    }

    //Guardar los datos en un txt
    ofstream archivo_salida("salidacpp.txt");    //crea el archivo txt y lo llama archivo_salida
    archivo_salida << "t \t y \t v \n";          //pone el titulo de la tabla que se va a crear en el txt
    for (int i = 0; i < t.size(); i++) {         //bucle for para iterar desde t0 hasta el ultimo valor de la lista t, que es igual a tf
        archivo_salida << t[i] << "\t" << y[i] << "\t" << v[i] << "\n";    //imprime en el txt cada iteracion de t, y, v en forma de tabla
    }
    archivo_salida.close(); //cierra el archivo de salida

     //Crea un archivo script gnuplot
     ofstream gnuarchivo("grafica.gp");    
     gnuarchivo << "set title 'y vs. t'\n";   //titulo
     gnuarchivo << "set xlabel 't'\n";   //titulo eje x
     gnuarchivo << "set ylabel 'y'\n";   //titulo eje y
     gnuarchivo << "plot 'salidacpp.txt' using 1:2 with lines title 'y'\n\n";   //grafique los datos de las columnas 1 y 2 de salidacpp.txt 
     gnuarchivo << "set terminal png\n";   //pasarlo a un png
     gnuarchivo << "set output 'posicion.png'\n";    //crear el png
     gnuarchivo << "replot\n";       //hacer otra grafica
     gnuarchivo << "set title 'v vs. t'\n";    //lo mismo pero con la velocidad...
     gnuarchivo << "set xlabel 't'\n";
     gnuarchivo << "set ylabel 'v'\n";
     gnuarchivo << "plot 'salidacpp.txt' using 1:3 with lines title 'v'\n\n";
     gnuarchivo << "set terminal png\n";
     gnuarchivo << "set output 'velocidad.png'\n";
     gnuarchivo << "replot\n"; 
     gnuarchivo.close();   //cerrar graficaciones

     //ejecuta gnuplot para generar las graficas
     system("gnuplot grafica.gp");

    return 0;   //fin
}
