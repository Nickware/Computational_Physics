#include <iostream>
#include <fstream>
#include <cmath>
 
class PendulumSimulation {
 
private:
    double b;        // Constante de amortiguamiento
    double m;        // Masa
    double L;        // Longitud del péndulo
    double thetaMax; // Valor inicial de theta
    double h;        // Tamaño del paso
    double tf;       // Tiempo final
 
public:
    // Constructor
    PendulumSimulation(double damping, double mass, double length,
                       double initialTheta, double stepSize, int finalTime)
        : b(damping), m(mass), L(length),
          thetaMax(initialTheta), h(stepSize), tf(finalTime) {}
 
    // Función f2
    double f2(double theta, double alpha) {
        return -(b / (m * L)) * alpha - (9.8 / L) * std::sin(theta);
    }
 
    // Resolver usando método de Runge-Kutta de cuarto orden
    void solve() {
 
        double t = 0.0;          // Tiempo inicial
        double theta = thetaMax; // Theta inicial
        double alpha = 0.0;      // Alpha inicial
 
        // Calcular número de pasos
        int numSteps = static_cast<int>(std::round(tf / h));
 
        // Abrir archivo de texto en modo escritura
        // Guardar tiempo vs theta
        std::ofstream outputFile1("results1.txt");
        // Abrir archivo de texto en modo escritura
        // Guardar alpha vs theta
        std::ofstream outputFile2("results2.txt");
        // Verificar si el archivo se abrió correctamente
        if (!outputFile1 || !outputFile2) {
            std::cerr << "Error al abrir el archivo de salida." << std::endl;
            return;
        }
 
        // Escribir al archivo los valores iniciales de t y theta
        outputFile1 << t << " " << theta * 180.0 / M_PI << "\n";
        
        // Escribir al archivo los valores iniciales de alpha y theta
        outputFile2 << alpha << " " << theta * 180.0 / M_PI << "\n";
 
        for (int i = 0; i < numSteps; i++) {
 
            // Calcular coeficientes k
            double k11 = alpha;
            double k12 = f2(theta, alpha);
 
            double k21 = alpha + (h / 2.0) * k12;
            double k22 = f2(theta + (h / 2.0) * k11, alpha + (h / 2.0) * k12);
 
            double k31 = alpha + (h / 2.0) * k22;
            double k32 = f2(theta + (h / 2.0) * k21, alpha + (h / 2.0) * k22);
 
            double k41 = alpha + h * k32;
            double k42 = f2(theta + h * k31, alpha + h * k32);
 
            // Actualizar los valores de theta y alpha
            theta = theta + (h / 6.0) * (k11 + 2 * k21 + 2 * k31 + k41);
            alpha = alpha + (h / 6.0) * (k12 + 2 * k22 + 2 * k32 + k42);
 
            // Actualizar tiempo
            t = t + h;
 
            // Escribir al archivo los valores de t y theta
            outputFile1 << t << " " << theta * 180.0 / M_PI << "\n";
            outputFile2 << alpha << " " << theta * 180.0 / M_PI << "\n";
        }
 
        // Cerrar el archivo de texto
        outputFile2.close();
        outputFile2.close();
    }
 
    // Graficar theta vs tiempo
    void graphThetaVsTime(std::string expfile) {
        std::string command = "xmgrace -nxy results1.txt -nxy " + expfile + " -pexec \"";
        // Título
        command += "title \\\"Posicion vs tiempo\\\";";
        // Estilizar
        command += "legend loctype view;";
        command += "s0 legend \\\"Calculada\\\";";
        command += "s1 legend \\\"Experimental\\\";";
        command += "s0 line color 15;";
        command += "s1 line color 12;";
        command += "s1 line linestyle 2;";
        command += "s1 line linewidth 2;";
        // Etiqueta de eje x
        command += "xaxis label \\\"Tiempo (s)\\\";";
        // Etiqueta de eje y, con fuente cambiada para visualización
        command += "yaxis label font 12;";
        command += "yaxis label \\\"q\\\";";
        command += "\" ";
        system(command.c_str());
    }
 
    // Graficar alpha vs theta
    void graphAlphaVsTheta() {
        std::string command = "xmgrace -nxy results2.txt -pexec \"";
        // Título
        command += "title \\\"Diagrama de Fase\\\";";
        // Estilizar
        command += "legend loctype view;";
        command += "s0 legend \\\"Calculada\\\";";
        command += "s0 line color 15;";
        // Etiqueta de eje x
        command += "xaxis label font 12;";
        command += "xaxis label \\\"a\\\";";
        // Etiqueta de eje y, con fuente cambiada para visualización
        command += "yaxis label font 12;";
        command += "yaxis label \\\"q\\\";";
        command += "\" ";
        system(command.c_str());
    }
};
 
int main() {
 
    double b = 0.0002;                   // Constante de amortiguamiento
    double m = 0.0464;                   // Masa
    double L = 0.22;                     // Longitud del péndulo
    double thetaMax = 24 * M_PI / 180.0; // Valor inicial de theta
    double h = 0.01;                     // Tamaño del paso
    double tf = 30.0;                    // Tiempo final
 
    // Ruta al artchivo con datos experimentales para graficar theta vs tiempo
    std::string expfile = "1.txt";
 
    // Instanciar objeto
    PendulumSimulation simulation(b, m, L, thetaMax, h, tf);
    // Resolver
    simulation.solve();
    // Graficar theta vs tiempo en xmgrace
    simulation.graphThetaVsTime(expfile);
    
    simulation.graphAlphaVsTheta();
 
    return 0;
}