class Padre:
    def __init__(self):
        print("Incialización de la calse padre")

    def metodo(self):
        print("Metodo de la clase padre")


class Hijo(Padre):
    """ 
    si se utiliza un constructor para la clase hijo si se quiere llamar a la clase padre es necesario utilizar el termino super() para llamar al padre
    """
    def __init__(self):
        # inicializador de la clase padre
        super().__init__()
        # inicializador de la clase hijo
        print("Inicializar la clase hijo")


""" 
Como hijo hereda todos los metodos de la clase padre si no se especifica el metodo a llamar se imprime el constructor de padre
solo y cuando la clase hijo no posea un método constructor
Si se esta utilizando el termino super entonces se imprime el inicializador de la clase hijo y de la clase padre
"""
miHijo = Hijo()
