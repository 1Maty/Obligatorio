
from Entities.desarrolladores import Productor, Programador, Tester, Diseñador
from Entities.desarrolladores import Desarroladores
from Entities.videojuegos import Videojuegos
from datetime import date
from time import sleep

developers=[]
año_actual = date.today().year
def menu():
    while True:

        print(" Seleccione la opcion del menu")
        print(" 1.Alta de desarrollador","\n","2.Alta de videojuego","\n","3.Simular competencia","\n","4.Realizar consultas","\n","5.Finalizar programa")
        print("-------------------------------------------------")
        seleccion=int(input("Seleccione un numero:"))
        match seleccion:
            case 1:
                def formulario():
                    cedula = input("pone la cedula")
                    nombre_completo = input("ingresa tu nombre completo ")
                    pais_origen = input("ingresa tu pais de origen ")
                    fecha_de_nac = input("ingresa tu fecha de nacimiento ")
                    años_experiencia = input("cuantos años de exp tenes ")
                    tipo_de_dev = input("en q rol trabajas 1-diseñador, 2-productor 3-programador 4-tester")

                    
                    print("--------------------------------")


                    #comprobacion de cedula
                    try: 
                        cedula = int(cedula)

                    except ValueError:
                        print("la cedula tiene q ser un numero")
                        return menu()

                    #comprobacion de nombre
                    try:
                        a,b = nombre_completo.split(" ")
                        nombre = a + b


                    except Exception:
                        print("separalo por espacios , tienen q ser 2")
                        return menu()


                    #comprobacion fecha de nacimiento
                    try:
                        dd,mm,yyyy = fecha_de_nac.split("/")
                        dd = int(dd)
                        mm = int(mm)
                        yyyy = int(yyyy)
                        
                        if dd > 0 and dd <= 31 and mm > 0 and mm <= 12 and yyyy <= 2003:
                            pass

                    except ValueError:
                            print("tiene q ser dd/mm/yyyy")
                            return menu()
                            

                    #comprobacion pais de nacimiento
                    try:
                        pais_origen = str(pais_origen)
                        pais_origen = pais_origen.capitalize()
                        paises = ["Uruguay", "Argentina", "Chile", "Brasil"]
                        
                        if pais_origen not in paises or type(pais_origen) != str:
                                raise ValueError

                    except ValueError:
                        print("escrbiste mal el pais o el mismo no se encuentra dentro de la lista de paises disponibles")
                        return menu()
                    

                    #comprobar años de exp
                    try:
                        exp = int(años_experiencia)
                        if yyyy + exp  > año_actual:
                            raise ValueError("años de estudio no puede ser mayor a edad")

                    except ValueError:
                        print("la experiencia tiene q ser menor a tu edad")
                        return menu()

                    except UnboundLocalError:
                        print("tenes q poner antes la fecha de nacimiento")
                        return menu()



                    try:
                        tipo_de_dev = int(tipo_de_dev)
                        if tipo_de_dev == 1:
                            dev = Diseñador(cedula, nombre_completo, pais_origen, fecha_de_nac, años_experiencia)
                            developers.append(dev)

                        if tipo_de_dev == 2:
                            dev = Productor(cedula, nombre_completo, pais_origen, fecha_de_nac, años_experiencia)
                            developers.append(dev)

                        if tipo_de_dev == 3:
                            dev = Programador(cedula, nombre_completo, pais_origen, fecha_de_nac, años_experiencia)
                            developers.append(dev)

                        if tipo_de_dev == 4:
                            dev = Tester(cedula, nombre_completo, pais_origen, fecha_de_nac, años_experiencia)
                            developers.append(dev)


                    except ValueError:
                        print("tenes q poner un numero")
                        return menu()

                formulario()

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
                sleep(0.5)
                print("finalizando ejecucion")
                sleep(1)
                print("...")
                sleep(1)
                print("...")
                sleep(1)
                print("hasta la proxima") 
                sleep(0.5)
                break  
            

menu()

def pruea():
    for dev in developers:
        print(dev.nombre)

pruea()