//============================================================================
// Name        : Lissajous.cpp
// Author      : Nickware
// Version     :
// Copyright   : GPL
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <stdio.h>
#include <math.h>

#define pi 3.141592

using namespace std;

//const double PI = 3.1416;

int main()
{

	double  x;
	double y;
	double A;
	double B;
	double  fx;
	double fy;
	double dt;
	//double delta;
	double t;

	dt=0.01;
	//delta=PI/2;

	cout << "Valor para frecuencia natural en X" << endl;
	cin >> fx;
	cout << "Valor para frecuencia natural en Y" << endl;
	cin >> fy;
	cout << "Valor para amplitud en X" << endl;
	cin >> A;
	cout << "Valor para amplitud en Y" << endl;
	cin >> B;

	FILE *lissajous;
	char nombre[]="lisajouss.dat";
	lissajous = fopen (nombre, "w");

	for (int i=0; i<360; i=i++){
		//t=i*delta;
		t=i+dt;
		x=A*sin(fx*t+dt);
		y=B*cos(fy*t);

		//x=A*sin(fx*t);
		//y=B*cos(fy*t);

		fprintf(lissajous, "%f %f %f\n", x, y, t);

	}
	return 0;
}
