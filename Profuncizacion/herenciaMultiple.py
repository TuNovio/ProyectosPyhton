class Clase1:
    """ 
    Clase de prueba para la herencia multiple
    """
    def __init__(self):
        """ 
        metodo contructor de la clase1
        """
        print("Metodo constructor de la clase 1")
    def metodo1(self):
        """ 
        Metodo de la clase 1
        """
        print("Metood de la clase 1")
class Clase2(Clase1):
    """ 
    Clase hija de la clase 1
    """
    def __init__(self):
        """ 
        metodo constructor de la clase 2
        """
        print("Metodo constructor de la clase 2")
    def metodo1(self):
        """ 
        metodo de la clase 2
        """
class Clase3(Clase1):
    """ 
    Otra clase hija de la clase 1
    """
    def __init__(self):
        """ 
        Metodo constructor de la clase 3
        """
        print("Metodo constructor de la clase 3")
    def metodo1(self):
        """ 
        Metodo de la clase 3
        """
class Clase4(Clase2, Clase3):
    """ 
    calse con multiherencia 
    clase2 padre de la clase 4
    clase 3 padre de la clase 4
    las clases con multiherencia no tiene constructor
    """
    def metodo1(self):
        """ 
        Metodo de la calse 4
        """
        print("Metodo de la calse 4")