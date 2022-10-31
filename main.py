from desarrolladores import Desarroladores

def formulario():
    cedula = input("pone la cedula")
    nombre_completo = input("ingresa tu nombre completo ")
    pais_origen = input("ingresa tu pais de origen ")
    fecha_de_nac = input("ingresa tu fecha de nacimiento ")
    años_experiencia = input("cuando años tenes de experiencia ")

    
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

    dev = Desarroladores(cedula, nombre_completo, pais_origen, fecha_de_nac, años_experiencia)

formulario()


