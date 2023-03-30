#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <iomanip>

using namespace std;

int main() {
    ifstream archivo("datos.txt");
    double tiempo, posicion;
    vector<double> tiempos, posiciones;
    
    while (archivo >> tiempo >> posicion) {
        tiempos.push_back(tiempo);
        posiciones.push_back(posicion);
    }
    
    // calcula las velocidades
    vector<double> velocidades;
    for (int i = 0; i < posiciones.size() - 1; i++) {
        double velocidad = (posiciones[i + 1] - posiciones[i]) / (tiempos[i + 1] - tiempos[i]);
        velocidades.push_back(velocidad);
    }

    // calcula las aceleraciones
    vector<double> aceleraciones;
    for (int i = 0; i < velocidades.size() - 1; i++) {
        double aceleracion = (velocidades[i + 1] - velocidades[i]) / (tiempos[i + 2] - tiempos[i]);
        aceleraciones.push_back(aceleracion);
    }

    // guarda los resultados a archivo
    ofstream archivoo("salida.txt");
    archivoo << "Tiempo\tPosicion\tVelocidad\tAceleracion\n";
    for (int i = 0; i < posiciones.size(); i++) {
        archivoo << tiempos[i] << "\t" << posiciones[i] << "\t";
        if (i < velocidades.size()) {
            archivoo << setprecision(2) << velocidades[i] << "\t";
        } else {
            archivoo << "\t";
        }
        if (i < aceleraciones.size()) {
            archivoo << setprecision(2) << aceleraciones[i];
        }
        archivoo << endl;
    }
    archivoo.close();

     // crea un archivo script gnuplot
     ofstream gnuarchivo("grafica.gp");
     gnuarchivo << "set title 'Posición vs. Tiempo'\n";
     gnuarchivo << "set xlabel 'Tiempo'\n";
     gnuarchivo << "set ylabel 'Posicion'\n";
     gnuarchivo << "plot 'salida.txt' using 1:2 with lines title 'Posicion'\n\n";
     gnuarchivo << "set terminal png\n";
     gnuarchivo << "set output 'posicion.png'\n";
     gnuarchivo << "replot\n";     
     gnuarchivo << "set title 'Velocidad vs. Tiempo'\n";
     gnuarchivo << "set xlabel 'Tiempo'\n";
     gnuarchivo << "set ylabel 'Velocidad'\n";
     gnuarchivo << "plot 'salida.txt' using 1:3 with lines title 'Velocidad'\n\n";
     gnuarchivo << "set terminal png\n";
     gnuarchivo << "set output 'velocidad.png'\n";
     gnuarchivo << "replot\n"; 
     gnuarchivo << "set title 'Aceleración vs. Tiempo'\n";
     gnuarchivo << "set xlabel 'Tiempo'\n";
     gnuarchivo << "set ylabel 'Aceleración'\n";
     gnuarchivo << "plot 'salida.txt' using 1:4 with lines title 'Aceleracion'\n\n";
     gnuarchivo << "set terminal png\n";
     gnuarchivo << "set output 'aceleracion.png'\n";
     gnuarchivo << "replot\n"; 
     gnuarchivo.close();

     // ejecuta gnuplot para generar las graficas
     system("gnuplot grafica.gp");
    
    return 0;
}
