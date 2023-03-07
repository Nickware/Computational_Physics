# este es un objetivo por defecto
# emplearemos make
.PHONY: all
all: hello

# reglas para decirle a make que vamos a contruir desde el archivo cpp
hello: hello.cpp
	g++ -o hello hello.cpp

# esta regla le indica a make que debe copiar los archvos en algun subdirectorio
# es opcional

.PHONY: install
install:
	mkdir -p binaries
	cp -p hello binaries

# esta regla le indica a make que borre hello y hello.o
.PHONY: clean
clean: 
	rm -f hello
