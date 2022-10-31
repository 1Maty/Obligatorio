
from desarrolladores import Productor, Programador, Tester, Diseñador
from desarrolladores import Desarroladores
from videojuegos import Videojuegos

developers=[]
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
                    años_experiencia = input("en que año arrancaste a trabajar ")
                    tipo_de_dev = input("en q rol trabajas 1-diseñador, 2-productor 3-programador 4-tester")

                    
                    print("--------------------------------")


                    #comprobacion de cedula
                    try: 
                        cedula = int(cedula)
                        print(f"tu cedula es {cedula}")


                    except ValueError:
                        print("la cedula tiene q ser un numero")
                        return formulario()



                    #comprobacion de nombre
                    try:
                        a,b = nombre_completo.split(" ")
                        print(f"tu nombre completo es {a} {b}")
                        nombre = a + b


                    except Exception:
                        print("separalo por espacios , tienen q ser 2")
                        return formulario()


                    #comprobacion fecha de nacimiento
                    try:
                        dd,mm,yyyy = fecha_de_nac.split("/")
                        dd = int(dd)
                        mm = int(mm)
                        yyyy = int(yyyy)
                        
                        if dd > 0 and dd <= 31 and mm > 0 and mm <= 12 and yyyy <= 2003:
                    
                            print(f"fecha de nacimiento: {dd}/{mm}/{yyyy}")


                    except ValueError:
                            print("tiene q ser dd/mm/yyyy")
                            return formulario()
                            

                    #comprobacion pais de nacimiento
                    try:
                        pais_origen = pais_origen.split(" ")
                        pais_origen = str(pais_origen)
                        
                        if type(pais_origen) == str:
                            print(f"tu pais de origen es es: {pais_origen}")

                        else:
                            raise ValueError("el formato de tu pais es incorrecto debe ser una cadena de texto")
                    except ValueError:
                        print("los datos son incorrectos")
                        return formulario()
                    

                    #comprobar años de exp
                    try:
                        estudios = int(años_experiencia)
                        if estudios > yyyy:
                            print("años de experiencia acorde a la edad")

                        else:
                            raise Exception("años de estudio no puede ser mayor a edad")

                    except ValueError:
                        print("tiene q ser un numero")
                        return formulario()

                    except UnboundLocalError:
                        print("tenes q poner antes la fecha de nacimiento")
                        return formulario()

                    except Exception:
                        print("fecha de nac tiene q ser mas chico q exp")
                        return formulario()


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
                        return formulario()

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
                print("Finalizar programa")    
                break  

menu()

def pruea():
    for dev in developers:
        print(dev.nombre)

pruea()