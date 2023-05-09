#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;

const double pi = acos(-1.0);

double f(double t, double x, double v, double alpha, double beta, double delta, double gamma, double omega)
{
    return -delta * v - alpha * x - beta * pow(x, 3) + gamma * cos(omega * t);
}

int main()
{
    double t0 = 0.0;
    double tf = 50.0;
    double dt = 0.01;
    double alpha = 1.0;
    double beta = 1.0;
    double delta = 0.2;
    double gamma = 0.3;
    double omega = 1.2;
    double x0 = 0.5;
    double v0 = 0.0;
    double t = t0;
    double x = x0;
    double v = v0;

   // Abre archivo de salida
  ofstream archivo("duffing.dat");

    while (t <= tf)
    {
        double k1x = v;
        double k1v = f(t, x, v, alpha, beta, delta, gamma, omega);
        double k2x = v + 0.5 * k1v * dt;
        double k2v = f(t + 0.5 * dt, x + 0.5 * k1x * dt, v + 0.5 * k1v * dt, alpha, beta, delta, gamma, omega);
        double k3x = v + 0.5 * k2v * dt;
        double k3v = f(t + 0.5 * dt, x + 0.5 * k2x * dt, v + 0.5 * k2v * dt, alpha, beta, delta, gamma, omega);
        double k4x = v + k3v * dt;
        double k4v = f(t + dt, x + k3x * dt, v + k3v * dt, alpha, beta, delta, gamma, omega);

        x += (k1x + 2 * k2x + 2 * k3x + k4x) * dt / 6;
        v += (k1v + 2 * k2v + 2 * k3v + k4v) * dt / 6;
        t += dt;

        // Escribir datos a archivo
        archivo << t << "\t" << x << "\t" << v << endl;
    }

    // Cerrar archivo 
  archivo.close();

  // Grafica con datos usando Gnuplot
  FILE *gnuplot = popen("gnuplot -persist", "w");
  if (gnuplot) {
    fprintf(gnuplot, "set xlabel 'x'\n");
    fprintf(gnuplot, "set ylabel 'v'\n");
    fprintf(gnuplot, "plot 'duffing.dat' using 2:3 with lines title 'Estado de Fase'\n");
    fflush(gnuplot);
    getchar();
    pclose(gnuplot);
  }

  return 0;
}
