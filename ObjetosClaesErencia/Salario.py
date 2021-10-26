class Salario:
    """ 
    #constructor de la clase
    #profesion es la profesion del usuario 
    #listaTrabajo es la lista en donde estan los trabajos
    #ListaSueldo es la lista en donde estan los pagos
    """
    def __init__(self, nSalario):
        self.salario=nSalario
    """ 
    #getter de la lista de los trabajos
    """
    def getSalarios(self):
        return self.salario
    """ 
    #setter del atributo trabajo o profesion
    """
    def setSalarios(self, nSalario):
        self.salario=nSalario