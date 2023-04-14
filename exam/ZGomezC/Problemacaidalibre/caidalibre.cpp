//Calculo de la velocidad y posicion de un objeto en caida libre
//utilizando el mètodo de euler
 
#include <iostream>
#include <math.h>
#include <fstream>

 
int main() {
    // se pide al usuario insertar los datos de posición, tiempo y velocidad inicial
    double y0, v0, h ,t0 ,yf;
 
    std::cout << "Digite la posición inicial: "; 
    std::cin >> y0;
    while (y0 <= 0) { // validar que la posición inicial sea positiva
        std::cout << "La posición inicial debe ser un número positivo. Digite de nuevo: ";
        std::cin >> y0;
    }
 
 std::cout << "Digite la posición final: "; 
    std::cin >> yf;
    while (yf < 0) { // validar que la posición inicial sea positiva o cero
        std::cout << "La posición final debe ser un número positivo o cero. Digite de nuevo: ";
        std::cin >> yf;
    }
 
    std::cout << "Digite el tiempo inicial: "; 
    std::cin >> t0;
    while (t0 < 0) { // validar que la posición inicial sea positiva o cero
        std::cout << "El tiempo inicial debe ser un número positivo o cero. Digite de nuevo: ";
        std::cin >> t0;
    }
 
    std::cout << "Digite la velocidad inicial: "; 
    std::cin >> v0;
    while (v0 < 0) { // validar que la velocidad inicial sea positiva o igual a cero
        std::cout << "La velocidad inicial debe ser un número positivo o cero. Digite de nuevo: ";
        std::cin >> v0;
    }
 
    std::cout << "Introduce el tamaño de paso, se recomienda escoger un valor pequeño para una mayor precision: "; 
    std::cin >> h;
    while (h <= 0) { // validar que el tamaño de paso sea positivo
        std::cout << "El tamaño de paso debe ser un número positivo. Digite de nuevo: ";
        std::cin >> h;
    }
 
    std::cout << "Posición inicial: " << y0 << std::endl;
    std::cout << "Velocidad inicial: " << v0 << std::endl;
    std::cout << "Tamaño de paso: " << h << std::endl;
 
//establemos la constante de la aceleracion gravitacional
const double g = 9.8;
double a=-g;
double v=v0;
double t=t0;
double Ny=y0;
double y=Ny;

//Guardar datos en los archivos de extension .txt y .cvs
std::ofstream outfile_txt("datos1.txt");
std::ofstream outfile_csv("datos1.csv");
outfile_csv << "tiempo,posicion,velocidad\n"; // Escribir encabezado en archivo CSV
//escribimos las ecuaciones de paso
do{ 
    Ny+=v*h;
    if(Ny>=0){
    v+=a*h;
    y=Ny;
    t+=h;
   outfile_txt << t << " " << y << " " << v << " " << a << std::endl; // Escribir datos en archivo de texto
    outfile_csv << t << "," << y << "," << v << std::endl; // Escribir datos en archivo CSV
    }else{
        std::cout << "La posiciòn calculada es menor a cero, falso";
        break;
        }
    }while(y>=(yf-h));
     // crea un archivo script gnuplot
     std::ofstream gnuarchivo("grafica.gp");
     gnuarchivo << "set title 'Posición vs. Tiempo'\n";
     gnuarchivo << "set xlabel 'Tiempo'\n";
     gnuarchivo << "set ylabel 'Posicion'\n";
     gnuarchivo << "plot 'datos1.txt' using 1:2 with lines title 'Posicion'\n\n";
     gnuarchivo << "set terminal png\n";
     gnuarchivo << "set output 'posicion.png'\n";
     gnuarchivo << "replot\n";     
     gnuarchivo << "set title 'Velocidad vs. Tiempo'\n";
     gnuarchivo << "set xlabel 'Tiempo'\n";
     gnuarchivo << "set ylabel 'Velocidad'\n";
     gnuarchivo << "plot 'datos1.txt' using 1:3 with lines title 'Velocidad'\n\n";
     gnuarchivo << "set terminal png\n";
     gnuarchivo << "set output 'velocidad.png'\n";
     gnuarchivo << "replot\n"; 
     gnuarchivo << "set title 'Aceleración vs. Tiempo'\n";
     gnuarchivo << "set xlabel 'Tiempo'\n";
     gnuarchivo << "set ylabel 'Aceleración'\n";
     gnuarchivo << "plot 'datos1.txt' using 1:4 with lines title 'Aceleracion'\n\n";
     gnuarchivo << "set terminal png\n";
     gnuarchivo << "set output 'aceleracion.png'\n";
     gnuarchivo << "replot\n"; 
     gnuarchivo.close();

     // ejecuta gnuplot para generar las graficas
     system("gnuplot grafica.gp");
    
    return 0;
}