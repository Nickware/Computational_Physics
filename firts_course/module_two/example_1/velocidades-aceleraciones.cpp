#include <iostream>     // Librería estándar para entrada y salida (cout, cerr)
#include <fstream>      // Librería para manejo de archivos (ifstream, ofstream)
#include <vector>       // Librería para utilizar vectores dinámicos
#include <sstream>      // Librería para manipulación de cadenas y conversión
#include <string>       // Librería para manejar cadenas de texto

using namespace std;    // Permite usar los elementos estándar de C++ sin anteponer 'std::'

int main() {
    vector<double> tiempos;     // Vector para almacenar los valores de tiempo leídos del archivo
    vector<double> posiciones;  // Vector para almacenar las posiciones leídas del archivo

    // Abrir el archivo de entrada que contiene los datos experimentales
    ifstream archivo("datos.txt");
    if (!archivo.is_open()) {   // Verifica si el archivo se abrió correctamente
        cerr << "No se pudo abrir el archivo de datos." << endl;
        return 1;               // Termina el programa si no se pudo abrir el archivo
    }

    string linea;
    // Leer y descartar la primera línea del archivo (encabezado)
    getline(archivo, linea);

    // Leer los datos línea por línea hasta el final del archivo
    while (getline(archivo, linea)) {
        istringstream iss(linea);      // Crea un flujo de entrada a partir de la línea leída
        double tiempo, posicion;
        if (iss >> tiempo >> posicion) {   // Intenta extraer dos valores numéricos (tiempo y posición)
            tiempos.push_back(tiempo);     // Agrega el tiempo al vector de tiempos
            posiciones.push_back(posicion);// Agrega la posición al vector de posiciones
        }
        // Si la línea no tiene el formato correcto, simplemente la ignora
    }
    archivo.close();  // Cierra el archivo de entrada

    // Validar que existen suficientes datos y que los vectores tienen el mismo tamaño
    if (tiempos.size() < 3 || posiciones.size() < 3 || tiempos.size() != posiciones.size()) {
        cerr << "Datos insuficientes o formato incorrecto." << endl;
        return 1;   // Termina el programa si hay un problema con los datos
    }

    // Calcular las velocidades usando diferencias hacia adelante
    vector<double> velocidades;     // Vector para almacenar las velocidades calculadas
    for (size_t i = 0; i < posiciones.size() - 1; i++) {
        // Esquema de diferencias hacia adelante: (x_{i+1} - x_i) / (t_{i+1} - t_i)
        double velocidad = (posiciones[i + 1] - posiciones[i]) / (tiempos[i + 1] - tiempos[i]);
        velocidades.push_back(velocidad);  // Agrega la velocidad calculada al vector
    }

    // Calcular las aceleraciones usando diferencias hacia adelante
    vector<double> aceleraciones;   // Vector para almacenar las aceleraciones calculadas
    for (size_t i = 0; i < velocidades.size() - 1; i++) {
        // Esquema de diferencias hacia adelante: (v_{i+1} - v_i) / (t_{i+2} - t_i)
        double aceleracion = (velocidades[i + 1] - velocidades[i]) / (tiempos[i + 2] - tiempos[i]);
        aceleraciones.push_back(aceleracion);  // Agrega la aceleración calculada al vector
    }

    // Guardar los resultados en un archivo de texto de salida
    ofstream salida("salida.txt");  // Crea el archivo de salida para escribir los resultados
    salida << "Tiempo\tPosicion\tVelocidad\tAceleracion\n"; // Escribe el encabezado de la tabla

    // Escribe los datos en el archivo, alineando cada columna con su valor correspondiente
    for (size_t i = 0; i < posiciones.size(); i++) {
        salida << tiempos[i] << "\t" << posiciones[i] << "\t"; // Escribe tiempo y posición
        if (i < velocidades.size()) {                          // Si hay velocidad para este índice
            salida << velocidades[i] << "\t";
        } else {
            salida << "\t";                                    // Si no, deja la celda vacía
        }
        if (i < aceleraciones.size()) {                        // Si hay aceleración para este índice
            salida << aceleraciones[i];
        }
        salida << endl;                                        // Termina la línea
    }
    salida.close();    // Cierra el archivo de salida

    cout << "Cálculo completado. Resultados en salida.txt" << endl; // Mensaje de confirmación

    return 0;   // Indica que el programa terminó correctamente
}
