""" 
#clase de subsidio en donde se establece la persona con sus datos
#Se vincula la persona con el trabajo y el salario
#se debe importar las clases Trabajo y Salario
"""
#se crea la clase Subsidio
class Subsidio:
    """ 
    #Constructor de la calse
    #la lista de subsidios ya esta inicializada
    #se inicializa el valor del tipo de subsidio con la lista de subsidios
    """
    def __init__(self, nTipos):
        self.tipos=nTipos
    """ 
    #getter del atributo subsidio
    """
    def getTipos(self):
        return self.tipos
    """ 
    #setter del atributo subsidio
    """        
    def setTipos(self, nTipos):
        self.tipos=nTipos