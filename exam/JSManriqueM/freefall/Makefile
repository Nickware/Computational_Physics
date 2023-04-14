# Autor: Juan Sebastian Manrique Moreno
# Curso: Física Computacional 1

# La siguiente regla compila el archivo "frefallcode.cpp" y lo convierte 
# en un binario llamado mismamente "freefall". Todo esto de manera 
# silenciosa gracias a colocar "@" al principio de la acción.

freefall : freefallcode.cpp
	@g++ freefallcode.cpp -o freefall

# La siguiente regla, compila y ejecuta el binario, por si no estaba
# compilado, si ya estaba compilado solo ejecuta el binario, luego lo 
# elimina ya que no es necesario y si se necesita el binario se ejecuta 
# la anterior acción. Todo esto de manera silenciosa gracias a colocar 
# "@" al principio de la acción.

run : freefall
	@./freefall
	@rm freefall

# Finalmente, esta regla elimina el binario, los archivos .txt y .gp 
# junto a las gráficas para volver a ejecutar y tener todo limpio, en el 
# caso en el que el archivo exista, la función "-f" lo ignora, así no 
# genera ningún tipo de conflicto.

.PHONY : clean
clean :
	@rm -f freefall datos.txt graph.gp position.png velocity.png