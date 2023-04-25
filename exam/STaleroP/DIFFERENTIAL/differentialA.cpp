#include <iostream>
#include <cmath>
#include <iomanip>
#include <vector>
#include <fstream>
#include <string>
using namespace std;
int main() {
    double g, yi, vi, ya, va, ta = 0.0;
	vector<double> zeit, position, velocity;	//vectores para almacenar datos
    cout << "Ingrese la altura inicial del objeto en metros: ";
    cin >> yi;
    cout << "Ingrese la velocidad inicial del objeto en metros por segundo: ";
    cin >> vi;
    cout << "Ingrese la aceleración gravitacional (Bogotá = 9.78 m/s²): ";
    cin >> g;
    ya = yi;
    va = vi;
    while (ya >= 0){	// Ciclo para calcular la posición de la esfera hasta que toque el suelo
		// Calculamos la altura y velocidad actual usando la expresión y = y_0 + v_0t - (gt^2)/2 y v = v_0 - gt
        ya = yi + (vi * ta) - (0.5 * g * (ta*ta));
        va = vi - g * ta;
        if(ya >= 0){
            // enviar datos de altura, velocidad y el tiempo actual a los vectores
            zeit.push_back(ta);
            position.push_back(ya);
    		velocity.push_back(va);
        }else{
        	//mostrar en pantalla el tiempo de caída
            cout << "El objeto ha llegado al suelo después de " << setprecision (5) << ta << " segundos" << endl;
        }
        ta += 0.05;	// Incrementamos el tiempo actual en 0.5 segundo
    }
    //write in the "analytic.txt" the time, position and velociy data
    ofstream file("analytic.txt");
    file << fixed << setw(9) << setprecision (9) << "Tiempo" << "\t" << "Posición" << "\t" << "Velocidad" << "\t\n";
    for (int i = 0; i < zeit.size(); i++) {
        file << fixed << setw(7) << setprecision (7) << zeit[i] << "\t" << position[i] << "\t" << velocity[i] << "\t";
        if (i < position.size()) {
            file << fixed << setw(7) << setprecision (7) << position[i] << "\t";
        } else {
            file << "\t";
        }
        if (i < velocity.size()) {
            file << fixed << setw(7) << setprecision (7) << velocity[i];
        }
        file << endl;
    }
    file.close();
	// crea un archivo script gnuplot
    ofstream gnuarchivo("analytic.gp");
    gnuarchivo << "set title 'Posición'\n";
    gnuarchivo << "set xlabel 'Tiempo'\n";
    gnuarchivo << "set ylabel 'Posición'\n";
    gnuarchivo << "plot 'analytic.txt' using 1:2 with lines title 'Posicion'\n\n";
    gnuarchivo << "set terminal png\n";
    gnuarchivo << "set output 'posicion.png'\n";
    gnuarchivo << "replot\n";
    gnuarchivo << "set title 'Velocidad'\n";
    gnuarchivo << "set xlabel 'Tiempo'\n";
    gnuarchivo << "set ylabel 'Velocidad'\n";
    gnuarchivo << "plot 'analytic.txt' using 1:3 with lines title 'Velocidad'\n\n";
    gnuarchivo << "set terminal png\n";
    gnuarchivo << "set output 'velocidad.png'\n";
    gnuarchivo << "replot\n";
    gnuarchivo.close();
    // ejecuta gnuplot para generar las graficas
    system("gnuplot analytic.gp");
    return 0;
}
