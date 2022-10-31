from Desarrolladores import Desarroladores
from Videojuegos_competencias import Videojuegos
desarrolladores=[]
def menu():
    print(" Seleccione la opcion del menu")
    print(" 1.Alta de desarrollador","\n","2.Alta de videojuego","\n","3.Simular competencia","\n","4.Realizar consultas","\n","5.Finalizar programa")
    print("-------------------------------------------------")
    seleccion=int(input("Seleccione un numero:"))
    match seleccion:
        case 1:
            print("Selecciono alta de desarrollador")
            cedula = int(input("Ingrese la cedula"))
            nombre_completo = input("Ingrese el nombre y apellido completo(separado por espacio)")
            pais_origen = input("ingresa tu pais de origen ")
            fecha_de_nac = int(input("ingresa tu fecha de nacimiento "))
            años_experiencia = int(input("cuando años tenes de experiencia "))
            nuevo_desarrollador=Desarroladores(cedula,nombre_completo,pais_origen,fecha_de_nac,años_experiencia)
            desarrolladores.append(nuevo_desarrollador)
            #todavia hay q chequear lo edad fecha de nacimiento mayor a años de experiencia
        case 2:
            categorias=[]
            cedulas=[]
            print("Selecciono alta de Videojuego")
            nombre=input("Ingrese el nombre del juego:")
            categorias_in=input("Ingrese las categorias del videojuegoo(1: Acción, 2: Aventura, 3: Estrategia, 4: Puzzle, ingresandolo sin comas por ejemplo 123 seria un juego de accion aventura y estrategia:")
            for numeros in categorias_in:
                categorias.append(numeros)
            while True:
                cedula_dev=int(input("Ingrese las cedulas completo, cuando haya puesto todas ingrese 0:"))
                if cedula_dev==0:
                    break
                cedulas.append(cedula_dev)
            print(cedulas,categorias)

        case 3:
            print("Selecciono simular competencia")
        case 4:
            print("Selecciono realizar consultas")
        case 5:
            print("Finalizar programa")        
menu()
