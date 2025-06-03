from Lib.Numero_total_personas import Numero_total_personas

totaldocentes = 0
totalestudiantes = 0
totalvisitantes = 0

masculinos = 0
femeninos = 0

cursomatematica = 0
cursocomunicacion = 0
cursoedfisica = 0

def menu_principal():
    while True:
        print("\n==== Menú Principal ====")
        print("1. Procesar")
        print("2. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            submenu()
        elif opcion == "2":
            print("Saliendo del sistema...")
            break
        else:
            print("ERROR . vuelva a ingresar.")

def submenu():
    while True:
        print("\n=== Submenú ===")
        print("1. Ingresar datos")
        print("2. Reporte")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ingresar_datos()
        elif opcion == "2":
            mostrar_reporte()
        elif opcion == "3":
            print("Regresando al menú principal...")
            break
        else:
            print("ERROR . vuelva a ingresar.")

def ingresar_datos():
    global totaldocentes, totalestudiantes, totalvisitantes
    global masculinos, femeninos
    global cursomatematica, cursocomunicacion, cursoedfisica

    while True:
        print("\n--- Tipo de Persona ---")
        print("1. Docente")
        print("2. Estudiante")
        print("3. Visitante")
        tipo = input("Seleccione el tipo de persona: ")
        if tipo == "1":
            totaldocentes += 1
            break
        elif tipo == "2":
            totalestudiantes += 1
            break
        elif tipo == "3":
            totalvisitantes += 1
            break
        else:
            print("ERROR . vuelva a ingresar.")

    while True:
        print("\n--- Género ---")
        genero = input("Ingrese género (M o m/F o f): ").upper()
        if genero == "M":
            masculinos += 1
            break
        elif genero == "F":
            femeninos += 1
            break
        else:
            print("ERROR . vuelva a ingresar.")

    while True:
        print("\n--- Curso ---")
        print("1. Matemática")
        print("2. Comunicación")
        print("3. Educación Física")
        curso = input("Seleccione el curso: ")
        if curso == "1":
            cursomatematica += 1
            break
        elif curso == "2":
            cursocomunicacion += 1
            break
        elif curso == "3":
            cursoedfisica += 1
            break
        else:
            print("ERROR . vuelva a ingresar.")

    print("Datos registrados con éxito.")

def mostrar_reporte():
    print("\n==== Reporte de datos ====")
    print("El total de docentes es:", totaldocentes)
    print("El total de estudiantes es:", totalestudiantes)
    print("El total de visitantes es:", totalvisitantes)
    print("El total de personas masculinas es:", masculinos)
    print("El total de personas femeninas es:", femeninos)
    print("El total de personas en Matemática es:", cursomatematica)
    print("El total de personas en Comunicación es:", cursocomunicacion)
    print("El total de personas en Educaciom fisica  es:", cursoedfisica)

    print("El numero total de personas que ingresaron es:",Numero_total_personas(totaldocentes,totalestudiantes,totalvisitantes))

menu_principal()
