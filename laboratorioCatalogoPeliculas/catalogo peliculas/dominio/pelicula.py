""" 
#Creacion de la clase pelicula
#Nombre de la pelicula como atributo 
#Definir metodo str para mostar el mensaje 
#Definir responsabilidades este representa un objeto de tipo pelicula
"""
class Pelicula:
    """ 
    #Declaracion del metodo constructor de la clase
    #nNombre es el nombre de la pelicula a registrar. nNombre != None && nNombre != ""
    """
    def __init__(self, nNombre):
        self._nombre=nNombre
    """ 
    #metodo para que se pueda mirar el contenido en formato str 
    #no recibe parametros 
    #retorna un mensaje
    """
    def __str__(self):
        print(f"La pelicula es:_{self._nombre}")
    """ 
    #getter del nombre de la pelicula
    #nombre ya se encuentra inicializado
    #retorna el nombre
    """
    @property
    def getNombre(self):
        return self._nombre
    """ 
    #setter del nombre de la pelicula a registrar
    #nNombre, es el nombre de la pelicula a registrar. nNombre != None && nNombre != ""
    """
    @getNombre.setter
    def setNombre(self, nNombre):
        self._nombre=nNombre
  