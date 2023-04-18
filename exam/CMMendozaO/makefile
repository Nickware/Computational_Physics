
# este es un objetivo por defecto
# emplearemos make
.PHONY: all
all: 02-example

# reglas para decirle a make que vamos a contruir desde el archivo cpp
hello: 02-example.cpp
	g++ -o 02-example 02-example.cpp

# esta regla le indica a make que debe copiar los archvos en algun subdirectorio
# es opcional

.PHONY: install
install:
	chmod +x 02-example
	./02-example
	mkdir -p binaries
	cp -p 02-example binaries
	mkdir -p images
	mv *.png images/
	mkdir -p data
	mv salida.txt *.gp data/

	

# esta regla le indica a make que borre hello y hello.o
.PHONY: clean
clean: 
	rm -f 02-example
	rm -rf binaries data images