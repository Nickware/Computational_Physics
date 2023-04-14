#makefile para  agilizar y eliminar residuos

#.PHONY: all
#all: Freefallc++


# reglas para decirle a make que vamos a contruir desde el archivo cpp
.PHONY: all
all:
	g++ -o FreeBall FreeBall.cpp
run: FreeBall
	./FreeBall
 
.PHONY: install
install:
	mkdir images
	mv *.png images/
	mkdir data
	mv *.txt data/

.PHONY: clean
clean: 
	rm -rf data images