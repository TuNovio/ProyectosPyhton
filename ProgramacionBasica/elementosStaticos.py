class miClase:
    #variables de clase
    #se puede compartir con los objetos de la clase
    miVariableClase=12
    def __init__(self, varibleInstancia):
        self.varible=varibleInstancia
#para acceder a la variable de clase se puede utilizar la clase y no un objeto de la clase
print(miClase.miVariableClase)
#para acceder a la variable de instancia se necesita un objeto 
mio=miClase("valor de instancia")
print(mio.varible)