"""
#realizar las operaciones aritmeticas usando clases y funciones
#declarar clase
"""
class Operaciones:
    """ 
    #calse aritmetica para realizar las operaciones +-*/
    #solo se necesitan 2 numeros para realiar las operaciones
    """
    def __init__(self, num1, num2):
        self.numero1=num1
        self.numero2=num2
    """ 
    #metodo que realiza la operacion de sumar
    #retorna el valor de la suma de los 2 numeros
    """
    def suma(self):
        sumar=self.numero1 + self.numero2
        return sumar
    """ 
    #metodo que realiza la operacion de restar
    #retorna el valor de la resta de los 2 numeros
    """
    def restar(self):
        resta=self.numero1-self.numero2
        return resta
    """ 
    #metodo que realiza la operacion de multiplicar
    #retorna el valor de la multiplicacion
    """
    def multiplicar(self):
        resta=self.numero1*self.numero2
        return resta
    """ 
    #metodo que realiza la operaicon de dividir
    #retorna el valor de la division 
    """
    def dividir(self):
        resta=self.numero1/self.numero2
        return resta