#include <cmath>
#include <fstream>
#include <iostream>

using namespace std;

const double sigma = 10.0;
const double beta = 8.0 / 3.0;
const double rho = 28.0;

void lorenz(double t, double *x, double *dxdt) {
  dxdt[0] = sigma * (x[1] - x[0]);
  dxdt[1] = x[0] * (rho - x[2]) - x[1];
  dxdt[2] = x[0] * x[1] - beta * x[2];
}

int main() {
  const double dt = 0.01;
  const double tmax = 100.0;

  const int n = tmax / dt;
  double x[3] = {1.0, 1.0, 1.0};
  double dxdt[3];

  // Abre archivo de salida
  ofstream archivo("lorenz.dat");

  for (int i = 0; i < n; i++) {
    double t = i * dt;
    lorenz(t, x, dxdt);

    // Metodo de Runge-Kutta de 4to-orden
    double k1[3], k2[3], k3[3], k4[3];
    for (int j = 0; j < 3; j++) {
      k1[j] = dt * dxdt[j];
      k2[j] = dt * (dxdt[j] + k1[j] / 2);
      k3[j] = dt * (dxdt[j] + k2[j] / 2);
      k4[j] = dt * (dxdt[j] + k3[j]);
      x[j] += (k1[j] + 2 * k2[j] + 2 * k3[j] + k4[j]) / 6;
    }

    // Escribir datos a archivo
    archivo << t << "\t" << x[0] << "\t" << x[1] << "\t" << x[2] << endl;
  }

  // Cerrar archivo 
  archivo.close();

  // Grafica con datos usando Gnuplot
  FILE *gnuplot = popen("gnuplot -persist", "w");
  if (gnuplot) {
    fprintf(gnuplot, "set xlabel 'x'\n");
    fprintf(gnuplot, "set ylabel 'z'\n");
    fprintf(gnuplot, "plot 'lorenz.dat' using 2:4 with lines title 'Estado de Fase'\n");
    fflush(gnuplot);
    getchar();
    pclose(gnuplot);
  }

  return 0;
}
