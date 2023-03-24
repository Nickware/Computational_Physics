#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main() {
    //vector<double> posiciones {0.0, 1.5, 3.0, 4.5}; // replace with your own values
    //vector<double> tiempos {0.0, 1.0, 2.0, 3.0}; // replace with your own values

    vector<double> tiempos {0.0,0.5,1,1.5,2,2.5,3,3.5,4};
    vector<double> posiciones {0, 0.61, 0.18,2.13, 3.63,	6.05, 10.02,16.54, 27.29};


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

    // salvar los resultados a archivo
    ofstream archivo("salida.txt");
    archivo << "Tiempo\tPosicion\tVelocidad\tAceleracion\n";
    for (int i = 0; i < posiciones.size(); i++) {
        archivo << tiempos[i] << "\t" << posiciones[i] << "\t";
        if (i < velocidades.size()) {
            archivo << velocidades[i] << "\t";
        } else {
            archivo << "\t";
        }
        if (i < aceleraciones.size()) {
            archivo << aceleraciones[i];
        }
        archivo << endl;
    }
    archivo.close();

    return 0;
}
