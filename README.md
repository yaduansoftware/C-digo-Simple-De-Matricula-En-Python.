# C-digo-Simple-De-Matricula-En-Python.
Programa en Python para registrar y administrar estudiantes desde la consola. 
# Sistema de estudiantes

Este es un programa que hice en Python para manejar una lista de estudiantes desde la consola. Funciona con un menú donde uno elige qué quiere hacer.

#QUE SE PUEDE HACER 

- Agregar un estudiante (nombre, carnet, edad, carrera y promedio)
- Mostrar todos los estudiantes que se han agregado
- Buscar un estudiante por su nombre
- Editar los datos de un estudiante
- Eliminar un estudiante
- Salir del programa

#COMO ESTA HECHO 

Cada estudiante se guarda en un diccionario y todos los diccionarios van dentro de una lista. El menú está dentro de un ciclo while True que se repite hasta que se elige la opción 6. Para buscar, editar y eliminar recorro la lista con un for y comparo los nombres sin importar si están en mayúscula o minúscula.

No usa ninguna librería externa, solo Python.

#COMO SE USA 

Solo hay que tener Python 3 instalado y ejecutar en la terminal:

    

#NOTA

Los datos se guardan solo mientras el programa está abierto. Al cerrarlo, la lista se borra.
