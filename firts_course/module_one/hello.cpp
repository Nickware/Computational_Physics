#include <fstream>
#include <iostream>

int main() {
    const int nx = 3;
    const int ny = 3;
    const int nz = 1;

    const char* filename = "hello_structured_points.vtk";
    std::ofstream out(filename);
    if (!out) {
        std::cerr << "No se pudo abrir " << filename << " para escritura\n";
        return 1;
    }

    // Encabezado VTK legacy
    out << "# vtk DataFile Version 3.0\n";
    out << "Simple structured points example\n";
    out << "ASCII\n";
    out << "DATASET STRUCTURED_POINTS\n";

    // Definición de la malla
    out << "DIMENSIONS " << nx << " " << ny << " " << nz << "\n";
    out << "ORIGIN 0 0 0\n";
    out << "SPACING 1 1 1\n";

    // Número total de puntos
    const int npoints = nx * ny * nz;
    out << "POINT_DATA " << npoints << "\n";
    out << "SCALARS u float 1\n";
    out << "LOOKUP_TABLE default\n";

    // Recorremos la malla en orden VTK: z más interno, luego y, luego x
    for (int k = 0; k < nz; ++k) {
        for (int j = 0; j < ny; ++j) {
            for (int i = 0; i < nx; ++i) {
                float x = static_cast<float>(i);
                float y = static_cast<float>(j);
                float u = x + y;  // u(x,y)=x+y
                out << u << "\n";
            }
        }
    }

    std::cout << "Escrito " << filename << "\n";
    return 0;
}
