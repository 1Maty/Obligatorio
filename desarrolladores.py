class Desarroladores():
    def __init__(self, cedula, name, pais_origen, nacimiento, experiencia):
        self.cedula = cedula
        self.name = name
        self.pais_origen = pais_origen
        self.nacimiento = nacimiento
        self.experiencia = experiencia


class Diseñador(Desarroladores):
    def __init__(self, cedula, name, pais_origen, nacimiento, experiencia):
        super().__init__(cedula, name, pais_origen, nacimiento, experiencia)
        self.rol = "diseñador"

        @property
        def rol(self):
            return self.rol

class Programador(Desarroladores):
    def __init__(self, cedula, name, pais_origen, nacimiento, experiencia):
        super().__init__(cedula, name, pais_origen, nacimiento, experiencia)
        self.rol= "programador"

        @property
        def rol(self):
            return self.rol

class Productor(Desarroladores):
    def __init__(self, cedula, name, pais_origen, nacimiento, experiencia):
        super().__init__(cedula, name, pais_origen, nacimiento, experiencia)
        self.rol = "productor"

        @property
        def rol(self):
            return self.rol

class Tester(Desarroladores):
    def __init__(self, cedula, name, pais_origen, nacimiento, experiencia):
        super().__init__(cedula, name, pais_origen, nacimiento, experiencia)
        self.rol = "tester"

        @property
        def rol(self):
            return self.rol
