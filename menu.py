
from multiprocessing.sharedctypes import Value
from Entities.desarrolladores import Productor, Programador, Tester, Diseñador
from Entities.desarrolladores import Desarroladores
from Entities.videojuegos import Videojuegos
from datetime import date
from time import sleep

juegos=[]
developers=[]
año_actual = date.today().year
devs_en_uso=[]

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

                        """
                        if len(str(cedula)) != 8:
                            raise ValueError
                        """


                    except ValueError:
                        print("la cedula tiene q ser un numero de 8 digitos")
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
                        dd,mm,yyyy = fecha_de_nac.split("-")
                        dd = int(dd)
                        mm = int(mm)
                        yyyy = int(yyyy)
                        
                        if dd > 0 and dd <= 31 and mm > 0 and mm <= 12 and yyyy <= 2003:
                            pass

                    except ValueError:
                            print("tiene q ser dd-mm-yyyy")
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
                roles=[]
                devs_juego=[]
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

                # vincula la cedula de cada dev con el rol
                devs_un_uso_copia=devs_en_uso.copy()
                todas_validas=True
                for devs in developers:
                    rol = devs.rol
                    if devs.cedula in cedulas and devs not in devs_en_uso:
                        roles.append(rol)
                        devs_juego.append(devs)
                        devs_en_uso.append(devs)
                        
                    else:
                        print("alguna cedula no esta registrada en la alta de desarrollador")
                        todas_validas=False
                if not todas_validas:  #por si no todos funcionan :)
                    devs_en_uso=devs_un_uso_copia


                        
                print(f"los roles son {roles}")
                


                diseñadores_valido=roles.count("diseñador")
                productores_valido=roles.count("productor")
                programadores_valido=roles.count("programador")
                tester_valido=roles.count("tester")

                if diseñadores_valido >= 2 and productores_valido >= 1 and programadores_valido >= 3 and tester_valido >= 2 and todas_validas:
                    nuevo_juego=Videojuegos(nombre,categorias,devs_juego)
                    juegos.append(nuevo_juego)
                else:
                    print("Las condiciones de roles no se cumplieron o no alguna de las cedulas no fueron validas")

                                                                     


            case 3:
                print("Selecciono simular competencia")
                categoria=input("Ingrese la categoria que desee simular(1-Acción,2-Aventura,3-Estrategia, 4- Puzzle)")
                jueguitos_de_competencia=[]
                diseñadores=0
                productores=0
                testers=0
                programadores=0
                puntajes=[]
                maximos=0
                for jueguitos in juegos:
                    if categoria in jueguitos.categorias:
                        jueguitos_de_competencia.append(jueguitos)
                if len(jueguitos_de_competencia)<3:
                    print("Cantidad insuficiente de juegos con la categoria")
                else:
                    for juegos_competencia in jueguitos_de_competencia:
                        listas_devs=juegos_competencia.lista_devs
                        for devs in listas_devs:

                            if devs.rol=="diseñador":
                                diseñadores+=1
                            elif devs.rol=="productor":
                                productores+=1
                            elif devs.rol=="tester":
                                testers+=1
                            elif devs.rol=="programador":
                                programadores+=1
                        puntaje=0.2*diseñadores+0.12*productores+0.5*programadores+0.18*testers
                        puntajes.append[juegos_competencia,puntaje]
                    for juegos,notas in puntajes:
                        if notas>maximos:
                            maximo=notas
                            primer_puesto=[juegos,notas]
                    puntajes.remove(primer_puesto)
                    maximo=0
                    for juegos,notas in puntajes:
                        if notas>maximos:
                            maximo=notas
                            segundo_puesto=[juegos,notas]
                    puntajes.remove(segundo_puesto)
                    for juegos,notas in puntajes:
                        if notas>maximos:
                            maximo=notas
                            tercer_puesto=[juegos,notas]
                nueva_competencia=Competencias(categoria,(primer_puesto,segundo_puesto,tercer_puesto)) 

                    
                    



                    
                               


                                
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
    
    Videojuegos.nombre
    Videojuegos.lista_devs
    

pruea()
