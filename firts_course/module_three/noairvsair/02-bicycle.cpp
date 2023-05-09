#include <cmath>
#include <fstream>
#include <iostream>
#include <sstream>
#include <vector>

class Bicicleta {
public:
  // Constructor para las condiciones iniciales 
  Bicicleta (double v0, double dt, double pmax, double mass, double tmax, double area, double densidad)
      : v(v0), dt(dt), pmax(pmax), mass(mass), tmax(tmax), area(area), densidad(densidad){}

  // Metodo par simular el movimiento. Este metodo permite almacenar los resultados en un vectores
  void simulacion() {
    double t = 0;
    while (t < tmax) {
      t += dt;
      double dv = pmax * dt / (mass * v)-(densidad * area * v * v) * dt/(2 * mass); // Metodo de Euler
      v += dv;
      tiempos.push_back(t);
      velocidades.push_back(v);
    }
  }

  // Metodo para mostrar los resultados
  void mostrar() {
    std::cout << "Tiempo (s)\tVelocidad (m/s)\n";
    for (int i = 0; i < tiempos.size(); i++) {
      std::cout << tiempos[i] << "\t\t" << velocidades[i] << "\n";
    }
  }

  // Metodo para salvar los resultados a un archivo para luego ser graficados con xmgrace
  void salvar_archivo(std::string archivo) {
    std::ofstream salida(archivo);
    salida << "# Time (s)\tVelocity (m/s)\n";
    for (int i = 0; i < tiempos.size(); i++) {
      salida << tiempos[i] << "\t" << velocidades[i] << "\n";
    }
    salida.close();
  }

private:
  double v;                       // Velocidad inicial
  double dt;                      // Paso de tiempo
  double pmax;                    // Potencia maxima del ciclista
  double mass;                    // Masa del ciclicta y la bicicleta
  double tmax;                    // Tiempo maximo de simulación
  double area;
  double densidad;
  std::vector<double> tiempos;      // Vector que almacena valores de tiempos
  std::vector<double> velocidades; // Vector que almacena valores de velocidades
};

int main() {
  double v0 = 4;        // m/s
  double dt = 1;        // segundos
  double pmax = 400;    // watts
  double mass = 70;     // kg
  double tmax = 200;    // segundos
  double area = 0.33;   // metros cuadrados
  double densidad = 0.5; // kg / metros cubicos 
  std::string archivo = "velocidad_vs_tiempo_air.dat";
  Bicicleta bicicleta(v0, dt, pmax, mass, tmax, area, densidad);
  bicicleta.simulacion();
  bicicleta.salvar_archivo(archivo);
  std::stringstream command;
  command << "xmgrace -nxy " << archivo;
  system(command.str().c_str());
  return 0;
}
