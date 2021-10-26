class Trabajo:
    """ 
    #constructor de la clase
    #profesion es la profesion del usuario 
    #listaTrabajo es la lista en donde estan los trabajos
    #ListaSueldo es la lista en donde estan los pagos
    """
    def __init__(self, nTrabajo):
        self.subTrabajos=nTrabajo
    """ 
    #getter de la lista de los trabajos
    """
    def getTrabajo(self):
        trabajo=self.subTrabajos
        return trabajo
    """ 
    #setter del atributo trabajo o profesion
    """
    def setTrabajo(self, nTrabajo):
        self.subTrabajos=nTrabajo