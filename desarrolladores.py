class Desarroladores():
    def __init__(self, cedula, name, pais_origen, nacimiento, experiencia):
        self._cedula = cedula
        self._name = name
        self._pais_origen = pais_origen
        self._nacimiento = nacimiento
        self._experiencia = experiencia

    @property
    def name(self):
        return self._name

    @property
    def cedula(self):
        return self._cedula

    @property
    def experiencia(self):
        return self._experiencia

    @property
    def nacimiento(self):
        return self._nacimiento

    @property
    def pais(self):
        return self._pais_origen

    def __eq__(self, otro):
        return self.cedula == otro.cedula


    def __gt__(self,otro):
        return self.experiencia > otro.experiencia


class Diseñador(Desarroladores):
    def __init__(self, cedula, name, pais_origen, nacimiento, experiencia):
        super().__init__(cedula, name, pais_origen, nacimiento, experiencia)
        self._rol = "diseñador"

    @property
    def rol(self):
        return self._rol
    
    @property
    def cedula(self):
        return self._cedula

class Programador(Desarroladores):
    def __init__(self, cedula, name, pais_origen, nacimiento, experiencia):
        super().__init__(cedula, name, pais_origen, nacimiento, experiencia)
        self._rol= "programador"

    @property
    def rol(self):
        return self._rol
    
    @property
    def cedula(self):
        return self._cedula

class Productor(Desarroladores):
    def __init__(self, cedula, name, pais_origen, nacimiento, experiencia):
        super().__init__(cedula, name, pais_origen, nacimiento, experiencia)
        self._rol = "productor"

    @property
    def rol(self):
        return self._rol
    
    @property
    def cedula(self):
        return self._cedula

class Tester(Desarroladores):
    def __init__(self, cedula, name, pais_origen, nacimiento, experiencia):
        super().__init__(cedula, name, pais_origen, nacimiento, experiencia)
        self._rol = "tester"

    @property
    def rol(self):
        return self._rol
    
    @property
    def cedula(self):
        return self._cedula