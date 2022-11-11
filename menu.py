from Entities.desarrolladores import Productor, Programador, Tester, Diseñador
from Entities.desarrolladores import Desarroladores
from Entities.competencias import Competencias
from Entities.videojuegos import Videojuegos
from Excepciones.NoValido import NoValido
from datetime import date
from time import sleep

developers=[]
def menu():
    juegos=[]
    año_actual = date.today().year
    devs_en_uso=[]
    while True:

        print(" Seleccione la opcion del menu")
        print(" 1.Alta de desarrollador","\n","2.Alta de videojuego","\n","3.Simular competencia","\n","4.Realizar consultas","\n","5.Finalizar programa")
        print("-------------------------------------------------")
        seleccion=int(input("Seleccione un numero: "))
        match seleccion:
            case 1:
                def formulario():
                    cedula = input("pone la cedula: ")
                    nombre_completo = input("ingresa tu nombre completo: ")
                    pais_origen = input("ingresa tu pais de origen: ")
                    fecha_de_nac = input("ingresa tu fecha de nacimiento: ")
                    años_experiencia = input("cuantos años de exp tenes: ")
                    tipo_de_dev = input("en q rol trabajas 1-diseñador, 2-productor 3-programador 4-tester \n")

                    
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
                            if dev in developers:
                                raise NoValido(100, "el dev ya esta registrado")
                            else:
                                developers.append(dev)
 
                        if tipo_de_dev == 2:
                            dev = Productor(cedula, nombre_completo, pais_origen, fecha_de_nac, años_experiencia)
                            if dev in developers:
                                raise NoValido(100, "el dev ya esta registrado")
                            else:
                                developers.append(dev)

                        if tipo_de_dev == 3:
                            dev = Programador(cedula, nombre_completo, pais_origen, fecha_de_nac, años_experiencia)
                            if dev in developers:
                                raise NoValido(100, "el dev ya esta registrado")
                            else:
                                developers.append(dev)

                        if tipo_de_dev == 4:
                            dev = Tester(cedula, nombre_completo, pais_origen, fecha_de_nac, años_experiencia)
                            if dev in developers:
                                raise NoValido(100, "el dev ya esta registrado")
                            else:
                                developers.append(dev)


                    except ValueError:
                        print("tenes q poner un numero")
                        return menu()

                formulario() #reusamos este codigo del practico 9.4

            case 2:
                categorias=[]
                dev_del_juego=[]
                roles=[]
                dev_en_uso2 = devs_en_uso.copy()
                contador_dev_encontrados = 0
                contador_dev_que_me_dan = 0

                print("Selecciono alta de Videojuego")
                nombre=input("Ingrese el nombre del juego:")
                categorias_in=input("Ingrese las categorias del videojuegoo(1: Acción, 2: Aventura, 3: Estrategia, 4: Puzzle, ingresandolo sin comas por ejemplo 123 seria un juego de accion aventura y estrategia:")

                for numeros in categorias_in:
                    categorias.append(numeros)
                    
                while True:
                    cedula_dev=int(input("Ingrese las cedulas completo, cuando haya puesto todas ingrese 0:"))
                    if cedula_dev==0:
                        break
                    contador_dev_que_me_dan += 1

                    dev_temp = Desarroladores(cedula_dev, "no importa", "Uruguay", "02-12-2002", 3)
                    for dev in developers:
                        if dev == dev_temp and dev not in devs_en_uso:
                            dev_del_juego.append(dev)
                            devs_en_uso.append(dev)
                            contador_dev_encontrados += 1

                if contador_dev_que_me_dan == contador_dev_encontrados:
                    print("todo piola")
                    se_pudo = True
                    for devs in dev_del_juego:
                        rol = devs.rol
                        roles.append(rol)

                else:
                    devs_en_uso=dev_en_uso2
                    se_pudo = False
                    print(contador_dev_encontrados)
                    print(contador_dev_que_me_dan)


                print(dev_del_juego,categorias)
                        
                print(f"los roles son {roles}")
                


                diseñadores_valido=roles.count("diseñador")
                productores_valido=roles.count("productor")
                programadores_valido=roles.count("programador")
                tester_valido=roles.count("tester")

                if diseñadores_valido >= 2 and productores_valido >= 1 and programadores_valido >= 3 and tester_valido >= 2 and se_pudo == True:
                    nuevo_juego=Videojuegos(nombre,categorias,dev_del_juego)
                    juegos.append(nuevo_juego)
                    print(juegos)
                else:
                    print("Las condiciones de roles no se cumplieron")

                                                                     

            case 3:
                print("Selecciono simular competencia")
                categoria=input("Ingrese la categoria que desee simular(1-Acción, 2-Aventura, 3-Estrategia, 4- Puzzle)")
                jueguitos_de_competencia=[]
                diseñadores=0
                productores=0
                testers=0
                programadores=0
                puntajes=[]
                maximos=0
                años_de_exp_diseñador = 0
                años_de_exp_productor = 0
                años_de_exp_tester = 0
                años_de_exp_programador = 0
                nombre_juegos = []

                for jueguitos in juegos:
                    if categoria in jueguitos.categorias:
                        jueguitos_de_competencia.append(jueguitos)
                if len(jueguitos_de_competencia) == 0:
                    print("Cantidad insuficiente de juegos con la categoria")
                else:
                    for juegos_competencia in jueguitos_de_competencia:
                        listas_devs=juegos_competencia.lista_devs
                    
                        for devis in listas_devs:
                            if devis.rol=="diseñador":
                                diseñadores+=1
                                años_de_exp_diseñador += int(devis.experiencia)

                            elif devis.rol=="productor":
                                productores+=1
                                años_de_exp_productor += int(devis.experiencia)

                            elif devis.rol=="tester":
                                testers+=1
                                años_de_exp_tester += int(devis.experiencia)

                            elif devis.rol=="programador":
                                programadores+=1
                                años_de_exp_programador += int(devis.experiencia)


                        #promedios
                        prom_diseñador = años_de_exp_diseñador/diseñadores
                        prom_productor = años_de_exp_productor/productores
                        prom_tester = años_de_exp_tester/testers
                        prom_programador = años_de_exp_programador/programadores

                        puntaje = 0.2*prom_diseñador + 0.12*prom_productor + 0.5*prom_programador + 0.18*prom_tester

                        puntajes.append(round(puntaje, 3)) #hacerle el round
                        nombre_juegos.append(juegos_competencia.nombre)


                    def encontrar_y_sacar():
                        posicion = puntajes.index(max(puntajes))
                        primero = [nombre_juegos[posicion], puntajes[posicion]]
                        puntajes.remove(puntajes[posicion])
                        nombre_juegos.remove(nombre_juegos[posicion])
                        return primero


                    primero = encontrar_y_sacar()
                    print("El primero es:",primero)

                    if len(nombre_juegos) != 0:
                        segundo = encontrar_y_sacar()
                        print("El segundo es:",segundo)

                    if len(nombre_juegos) != 0:
                        tercero = encontrar_y_sacar()
                        print("El tercero es:",tercero)


                                
            case 4:
                print("Selecciono realizar consultas")
                consulta = int(input("10 mejores devs-1; 5 mejores program-2; los 7 viejos-3; devs uruguayos-4: "))
                

                match consulta:

                    case 1:
                        devs_consulta=developers.copy()
                        devs_consulta.sort(reverse=True)
                        contador = 0

                        dict_consulta={}
                        for index in range(len(devs_consulta)):
                            contador += 1
                            if contador == 11:
                                break
                            dict_consulta[index+1] = {"exp" : devs_consulta[index].experiencia, "nombre": devs_consulta[index].name}


                        print(dict_consulta)


                    case 2:
                        devs_consulta_prog = []
                        contador_prog = 0


                        for devs in developers:
                            if isinstance(devs, Programador):
                                devs_consulta_prog.append(devs)
                        
                        devs_consulta_prog.sort(reverse=True)
                        print(devs_consulta_prog)
                        
                        dict_consulta_prog={}
                        for index in range(len(devs_consulta_prog)):
                            contador_prog += 1
                            if contador_prog == 6:
                                break
                            dict_consulta_prog[index+1] = {"exp" : devs_consulta_prog[index].experiencia, "nombre": devs_consulta_prog[index].name}


                        print(dict_consulta_prog)


                    case 3: 
                        pass

                    case 4:
                        pass
            



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

