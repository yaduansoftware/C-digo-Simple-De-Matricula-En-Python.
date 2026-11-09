# Este proyecto fue construido por Yaduán Sánchez con el fin de demostrar sus conocimientosp
# No fue utilizado para venderlo y no fue un trabajo para alguien más 

datos = []

while True:
    print("\n--- MENU ---")
    print("1. Agregar estudiante")
    print("2. mostrar estudiantes")
    print("3. buscar estudiante")
    print("4. editar estudiante")
    print("5. eliminar estudiante")
    print("6. Salir")
    opcion = input("Elija una opcion: ")

    if opcion == "1": #op 1
        nombre = input("Ingrese el nombre del estudiante: ") # datos
        carnet = int(input("Ingrese el carne del estudiante: "))
        edad = int(input("Ingrese la edad del estudiante: "))
        carrera = (input("Ingrese la carrera del estudiante: "))
        promedio = float(input("ingrese el promedio del estudiante: "))

        # diccionario
        dato = {"nombre": nombre, "carnet": carnet, "edad": edad, "carrera": carrera, "promedio": promedio}
        datos.append(dato)
        print("Datos agregados")

    elif opcion == "2": #op 2
        if len(datos) == 0:
            print("No ha agregado ningun estudiante todavia")
        else:
            subtotal = 0
            print("\nestudiantes agregados:")
            for dato in datos:
                print(f"Nombre: {dato['nombre']}, Carnet: {dato['carnet']}, Edad: {dato['edad']}, Carrera: {dato['carrera']}, Promedio: {dato['promedio']}, Fin")

    elif opcion == "3": #op 3

        nombre_buscar = input("Ingrese el nombre del estudiante: ")

        encontrado = False

        for dato in datos:

            if dato["nombre"].lower() == nombre_buscar.lower():

                print("\n--- Estudiante encontrado ---")
                print(f"Nombre: {dato['nombre']}")
                print(f"Carnet: {dato['carnet']}")
                print(f"Edad: {dato['edad']}")
                print(f"Carrera: {dato['carrera']}")
                print(f"Promedio: {dato['promedio']}")

                encontrado = True
                break

        if encontrado == False:
            print("No se encontró ese estudiante.")

    elif opcion == "4":
        nombre_buscar = input("Ingrese el nombre del estudiante a editar: ")

        encontrado = False

        for dato in datos:
            if dato["nombre"].lower() == nombre_buscar.lower():

                nuevo_nombre = input("Nuevo nombre: ")
                nueva_edad = int(input("Nueva edad: "))
                nueva_carrera = input("Nueva carrera: ")
                nuevo_promedio = float(input("Nuevo promedio: "))

                dato["nombre"] = nuevo_nombre
                dato["edad"] = nueva_edad
                dato["carrera"] = nueva_carrera
                dato["promedio"] = nuevo_promedio

                print("Estudiante actualizado")

                encontrado = True
                break

        if encontrado == False:
            print("No se encontró ese estudiante.")

    elif opcion == "5":

        nombre_buscar = input("Ingrese el nombre del estudiante a eliminar: ")

        encontrado = False

        for dato in datos:

            if dato["nombre"].lower() == nombre_buscar.lower():

                datos.remove(dato)

                print("Estudiante eliminado correctamente.")

                encontrado = True
                break

        if encontrado == False:
            print("No se encontró ese estudiante.")

    elif opcion == "6":
        break

