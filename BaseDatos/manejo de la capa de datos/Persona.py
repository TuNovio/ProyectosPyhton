#importar loggin para realizar las pruebas de esa clase
from loggin_per import log
class Persona:
    """ 
    #Declarar el metodo constructor de la clase persona
    #nIentificacion, es la identificacion de la persona. nIdentificacion != "" && nIdentificacion != None
    #nNombre, es el nombre de la persona. nNombre != "" && nNombre != None
    #nEdad, es la edad de la persona. nEdad > 0 && nEdad != None
    #nPeso, es el peso de la persona. nPeso > 0 && nPeso != None
    #los atributos son privados por lo tanto deben inicializarce correctamente
    """
    def __init__(self, nIdentificacion, nNombre, nEdad, nPeso):
        #identificacion
        self._identificacion=nIdentificacion
        #nombre
        self._nombre=nNombre
        #edad
        self._edad=nEdad
        #peso
        self._peso=nPeso
    """ 
    #Metodo que transforma al formato str 
    #los atributos de instancia ya se encuentran inicializados
    #retorna una cadena de texto con el formato a imprimir en los mensajes que llamen a los atributos de clase
    """
    def __str__(self):
        return f'''
    Identificacion:_ {self._identificacion},
    Nombre:_ {self._nombre},
    Edad:_ {self._edad}
    Peso:_ {self._peso}
    '''
    """ 
    #metodo que retorna la identificacion de la persona 
    #el atributo persona ya se encuentra inicializado
    #retorna la identificacion de la persona
    """
    @property
    def getIdentificacion(self):
        return self._identificacion
    """ 
    #metodo que cambia el atributo de la identificacion 
    #el atributo se encuentra inicializado 
    #cambia el atributo por el que llega por parametro 
    #nIdentificacion, es la identificacion nueva. nIdentificacion > 0 && nIdentificacion != None 
    """
    @getIdentificacion.setter
    def setIdentificacion(self, nIdentificacion):
        self._identificacion=nIdentificacion
    """ 
    #Metodo que retorna el nombre de la persona 
    #el atributo nombre se encuentra inicializado
    #retorna el nombre de la persona
    """
    @property
    def getNombre(self):
        return self._nombre
    """ 
    #metodo que cambia el nombre de la persona
    #el atributo de nombre se encuentra inicializado
    #nNombre, es el nombre nuevo. nNombre != None && nNombre != ""
    """
    @getNombre.setter
    def setNombre(self, nNombre):
        self._nombre=nNombre
    """ 
    #Metodo que retorna la edad de la persona 
    #el atributo de edad ya se encuentra inicializado 
    #retorna la edad de la persona
    """
    @property
    def getEdad(self):
        return self._edad
    """ 
    #Metodo que cambia la edad de la persona
    #el atributo de edad ya se encuentra inicializado 
    #nEdad, es la edad de la persona. nEdad > 0 && nEdad != None
    """
    @getEdad.setter
    def setEdad(self, nEdad):
        self._edad=nEdad
    """ 
    #Metodo que retorna el peso de la persona
    #el atributo de peso ya se encuentra inicializado 
    #retorna el peso de la persona 
    """
    @property
    def getPeso(self):
        return self._peso
    """ 
    #Metodo que cambia el valor del peso 
    #el atributo de peso ya se encuentra inicializado 
    #nPeso, es el peso de la persona. nPeso > 0 && nPeso != None
    """
    @getPeso.setter
    def setPeso(self, nPeso):
        self._peso=nPeso
""" 
""" #realizar las pruebas
"""
if __name__ == '__main__':
    persona1=Persona(11, "Alfonso", 21, 80)
    log.debug(persona1) """