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

using namespace std;

int main()
{
	double x;
	double y;
	double A;
	double B;
	double wx;
	double wy;
	double dt;
	double t;

	dt=0.01;

	cout << "Valor para wx" << endl;
	cin >> wx;
	cout << "Valor para wy" << endl;
	cin >> wy;
	cout << "Valor para A" << endl;
	cin >> A;
	cout << "Valor para B" << endl;
	cin >> B;

	FILE *lissajous;
	char nombre[]="lisajouss.dat";
	lissajous = fopen (nombre, "w");

	for (int i=0; i<360; i=i++){
		t=i*dt;

		x=A*sin(wx+t);
		y=B*cos(wy+t);

		fprint(lissajous, "%f %f $f\n", x, y, t);

	}
	return 0;
}
