#Definimos las variables
CC=g++
CFLAGS=-Wall -g

# Este es un objetivo por defecto que compilará el programa
.PHONY: all
all:
	g++ -o  caidalibre caidalibre.cpp
#ejecutar progrma
run: caidalibre
	./caidalibre
# Regla para eliminar el programa y cualquier archivo objeto generado durante la compilación
.PHONY: install
install:
	mkdir freefall
	mv *.png freefall/
	mv *.txt freefall/
	mv *.csv freefall/
	mv *.dat freefall/
.PHONY: clean
clean:
	rm -rf freefall
