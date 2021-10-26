""" 
#Se crean los metodos get y set
#se comprueba el funcionamiento
#se declara la clase
"""
class People:
    def __init__(self, nCantidad, nPeso):
        self._cantidad=nCantidad
        self._peso=nPeso
    """ 
    #metodo que retorna la cantidad de personas
    @property se especifica que los atributos son de la calse
    """
    @property
    def cantidad(self):
        return self._cantidad
    """ 
    #metodo que retorna el peso de las personas
    @property se especifica que los atributos son de la clase
    """
    @property
    def darPeso(self):
        return self.peso
    """ 
    metodo que sirve para obtener el valor de la cantidad de las personas
    """
    @cantidad.setter
    def cantidad1(self, cantidad):
        self._cantidad=cantidad
    """ 
    #metodo para mostrar los detalles 
    """
    def mostrar(self):
        print(f"Cantidad de personas:_{self._cantidad}")
persona1=People(20,90)
print(persona1.mostrar())