""" 
#Clase en la que se encuentra descrita la informacion de la persona
#Identificacion de la persona
#nombre de la persona
#Edad de la persona 
#Trabajo o profesion 
#Salario segun la profesion
"""
#importar la clase Trabajo
from Trabajo import Trabajo as miTrabajo
#importar la calse Salario
from Salario import Salario as miSalario
#importar la clase Subsidio
from Subsidio import Subsidio as miSubsidio
class Persona:
    """ 
    #nIdentificacion es la identificacion del usuario nIdentificaion >0
    #nNombre es el nombre del usuario, nNombre!="" && nNombre!=Null
    #nTrabajo es la profesion del usuario, si no tiene profesion es desempleado
    #nSalario es el salario que recibe por su profesion
    """
    def __init__(self, nIdentificacion, nNombre, nEdad, nTrabajo, nSalario, nSubsidio):
        self.identificacion=nIdentificacion
        self.nombre=nNombre
        self.edad=nEdad
        self.trabajo=miTrabajo(nTrabajo).getTrabajo
        self.salario=miSalario(nSalario).getSalarios
        self.subsidio=miSubsidio(nSubsidio).getTipos
    """ 
    #getter del atributo de identificacion
    """
    def getIdentificacion(self):
        return self.identificacion
    """ 
    #getter del atributo nombre
    """
    def getNombre(self):
        return self.nombre
    """ 
    #getter del atributo edad
    """
    def getEdad(self):
        return self.edad
    """ 
    #getter del trabajo 
    """
    def getTrabajo(self):
        return self.trabajo
    """ 
    #getter del atributo de salario
    """
    def getSalario(self):
        return self.salario
    """ 
    #getter del atributo de subsidio
    """
    def getSubsidio(self):
        return self.subsidio
    """ 
    #setter del atributo identificaion 
    """
    def setIdentificacion(self, nIdentificacion):
        self.identificacion=nIdentificacion
    """
    #setter del atributo nombre
    """
    def setNombre(self, nNombre):
        self.nombre=nNombre
    """ 
    #setter del atributo edad
    """
    def setEdad(self, nEdad):
        self.edad=nEdad
        """ 
    #setter del trabajo 
    """
    def setTrabajo(self, nTrabajo):
        self.trabajo=miTrabajo(nTrabajo).setTrabajo(nTrabajo)
    """ 
    #setter del atributo de salario
    """
    def setSalario(self, nSalario):
        self.salario=miSalario(nSalario).setSalarios(nSalario)
    """ 
    #setter del atributo de subsidio
    """
    def setSubsidio(self, nSubsidio):
        self.subsidio=miSubsidio(nSubsidio).setTipos(nSubsidio)