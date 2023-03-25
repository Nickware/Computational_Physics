#include <iostream> // libreria standard para escribir y leer (Entrada y salida)
#include <fstream> // libreria para escribir archivos
#include <vector> // Libreria para crear vectores

using namespace std; // Contiene todos los elementos de la libreria standard de C++

int main() {
    vector<double> tiempos {0.0,0.5,1,1.5,2,2.5,3,3.5,4}; // Remplace los valores que considere deba tomar el vector del tiempos
    vector<double> posiciones {0, 0.61, 0.18,2.13, 3.63,	6.05, 10.02,16.54, 27.29}; // Remplace los valores que considere deba tomar el vector de posiciones


    // calcula mediante esquema de diferencias hacia adelante las velocidades
    vector<double> velocidades; // Vector de velocidades
    // bucle para calcular las velocidades. 
    //Toma todos los valores de la posicion de uno en uno, hasta el penultimo valor encontraro en el vector posiciones
    for (int i = 0; i < posiciones.size() - 1; i++) { 
    // variable velocidad. Esta definida mediante esquema de diferencias hacia adelante
        double velocidad = (posiciones[i + 1] - posiciones[i]) / (tiempos[i + 1] - tiempos[i]);
        velocidades.push_back(velocidad); // Va agregando velocidad calculada al vector velocidades
    }

    // calcula mediante esquema de diferencias hacia adelante las aceleraciones
    vector<double> aceleraciones;
    // bucle para calcular las aceleraciones. 
    // Toma todos los valores de la posicion de uno en uno, hasta el penultimo valor encontrado en el vector velocidades
    for (int i = 0; i < velocidades.size() - 1; i++) {
    // variable aceleracion. Esta definida mediante esquema de diferencias hacia adelante    
        double aceleracion = (velocidades[i + 1] - velocidades[i]) / (tiempos[i + 2] - tiempos[i]);
        aceleraciones.push_back(aceleracion); // Va agregando aceleracion calculada al vector aceleraciones
    }

    // Guarda los resultados a un archivo txt
    ofstream archivo("salida.txt"); // Prepara mediante archivo la creacion de un archivo de extension txt
    archivo << "Tiempo\tPosicion\tVelocidad\tAceleracion\n"; // Este es el encabezado de mi archivo txt
    for (int i = 0; i < posiciones.size(); i++) { // Este bucle depende del numero de valores del vector posicion
        archivo << tiempos[i] << "\t" << posiciones[i] << "\t"; // Esta linea imprime en el archivo los tiempos (ubicados en le vector tiempos) y las posiciones (ubicada en le vector posiciones)
        if (i < velocidades.size()) { // Esta estructura de control va guardando las velocidades obtenidas en el vector velocidades, en el archivo txt
            archivo << velocidades[i] << "\t"; // Almacena las velocidade al archivo
        } else {
            archivo << "\t"; // cuando no encuentra velocidades, pasa a guardar las aceleraciones
        }
        if (i < aceleraciones.size()) { // Esta estructura de control va guardando las aceleraciones obtenidas en el vector aceleraciones, en el archivo txt
            archivo << aceleraciones[i]; // Guarda todas la aceleraciones calculadas en el archivo
        }
        archivo << endl; // Finaliza la fila cada vez que imprime el ultimo valor de la fila, en este caso la aceleracion
    }
    archivo.close(); // Instruccion que indica que se cierra el archivo txt

    return 0; // Le indica al cuerpo del programa (main) la finalizacion del programa.
}
