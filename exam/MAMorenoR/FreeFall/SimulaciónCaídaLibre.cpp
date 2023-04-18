#include<iostream>
#include<fstream>
#include<cmath>
#include <vector>
#include <string>
#include <iomanip>

using namespace std;

const float g = 9.80665;

int main(){
	
	float t = 0;
	float dt;
	float y; 
	float v = 0 ;
	float tf;
	vector<float> tmp, p , vel ; 
	
	ofstream archivo("datos.txt");
	
	
	cout << "Ingrese el tiempo que cae la particula :"<< endl;
	cin >> tf; 
	
	cout << "Ingrese cada cuanto desea obtener datos de posción y tiempo: "<< endl;
	cin>> dt; 
	
	cout << " Ingrese la posición inicial de la la particula: "<< endl; 
	cin>> y; 
	
	if (dt == 0){
		cout << "Ingrese cada cuanto desea obtener datos de posción y tiempo: "<< endl;
		cin>> dt; 
		
	}
		
	{
		for ( float i = 0; i<= tf ; i = i+dt){
			t =+i;
			if (t ==0 ){
			tmp.push_back(t);
			vel.push_back(v); 
			p.push_back(y);
			
			}else{
			
			  float vnext = v + g* dt;
			  float ynext =  y + v*dt	;
			v =  vnext;
			y = ynext; 
			
			tmp.push_back(t);
			vel.push_back(v); 
			p.push_back(y); 
			
		}}}

    archivo << "Tiempo\tPosicion\tVelocidad\n";
    	 for (size_t j = 0; j < tmp.size(); ++j) {
        	archivo << tmp.at(j) << "\t"<<p.at(j)<<"\t"<<vel.at(j)<< "\n" ;
        	      	
    }
	archivo.close(); 
	
	 // crea un archivo script gnuplot
     ofstream gnuarchivo("grafica.gp");
     gnuarchivo << "set title 'Posición vs. Tiempo'\n";
     gnuarchivo << "set xlabel 'Tiempo'\n";
     gnuarchivo << "set ylabel 'Posicion'\n";
     gnuarchivo << "plot 'datos.txt' using 1:2 with lines title 'Posicion'\n\n";
     gnuarchivo << "set terminal png\n";
     gnuarchivo << "set output 'posicion.png'\n";
     gnuarchivo << "replot\n";     
     gnuarchivo << "set title 'Velocidad vs. Tiempo'\n";
     gnuarchivo << "set xlabel 'Tiempo'\n";
     gnuarchivo << "set ylabel 'Velocidad'\n";
     gnuarchivo << "plot 'datos.txt' using 1:3 with lines title 'Velocidad'\n\n";
     gnuarchivo << "set terminal png\n";
     gnuarchivo << "set output 'velocidad.png'\n";
     gnuarchivo << "replot\n"; 
     gnuarchivo.close();

     // ejecuta gnuplot para generar las graficas
     system("gnuplot grafica.gp");


	
	return 0; 
	
	
	}
