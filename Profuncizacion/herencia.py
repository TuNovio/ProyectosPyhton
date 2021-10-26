""" 
desde aqui se categoriza como herencia simple
"""
class ListaSimple:
    """ 
    Clase padre de una lista en la que se agregan elementos de tipo numerico
    las operaciones deben ser inicializadas asi como el constructor o __init__
    """
    def __init__(self, elemento):   
        """ 
        Metodo constructor para inicializar la lista de parametros
        elementos, son los elementos de la lista a crear, elemento != None && elemento != ""
        asigna los elementos a la lista creada
        """
        self._elementos=list(elemento)
    def agregarElemento(self, elemento):
        """ 
        Método que permite agrefar a la lista un elemento nuevo que se recibe por parametro 
        elemento, es el elemento a agregar a la lista. elemento != None && elemneto != ""
        agregar el elemento a la lista creada
        """
        self._elementos.append(elemento)
        
    def __getitem__(self, indice):
        """ 
        Método que permite buscar un elemento de la lista por su indice
        la lista de elementos ya se encuentra inicializada
        elemento, es el elemento a buscar en la lista. elemnto != None && elemento != ""
        retorna el elemento dado el indice
        """
        return self._elementos[indice]
    
    def ordernarElementos(self):
        """ 
        Método que permite ordenar los elementos de la lista
        la lista de elementos ya se encuentra inicializada 
        retorna la lista de elementos ordenada
        """
        self._elementos.sort()
        
    def __len__(self):
        """ 
        Método que permite visualizar la cantidad de elementos dentro de la lista
        la lista de elementos ya se encuentra inicializada
        retornar la cantidad de elementos dentro de la lista
        """
        return len(self._elementos)
    
    def __repr__(self):
        """ 
        Metodo que retorna un mensaje con la informacion de los elementos dentro de la lista
        la lista de elementos ya se encuentra inicializada
        retorna un mensaje con la información de los elementos 
        """
        return f'{self.__class__.__name__}({self._elementos!r})'

class listaOrdenada(ListaSimple):
    """ 
    Clase hija de la clase lista simple
    la clase padre se encuentra inicializada 
    en esta clase se ordenaran los elementos eredados de la clase padre
    """
    def __init__(self, elementos=[]):
        """ 
        Método constructor de la clase
        la clase padre se encuentra inicializada
        elementos, son los elementos heredados de la clase pradre. elementos != None && elementos != ""
        se ordenan los elementos heredados
        """
        super().__init__(elementos)
        self.ordernarElementos()
        
    def agregarElemento(self, elemento):
        """ 
        Método que permite agregar elementos a la lista heredada de la clase padre este metodo sobreescribe el metodo de la clase padre
        la clase padre se encuentra inicializada
        la lista de elementos se encuentra inicializada
        elemento, es el elementos a agregar a la lista heredada. elemento != None && elemento != ""
        agregar el elemento que llega por parametro a la lista de elementos y ordenarlos
        """
        super().agregarElemento(elemento)
        self.ordernarElementos()

class listaEnteros(ListaSimple):
    """ 
    clase hija de la lista simple 
    la clase padre ya se encuentra inicializada
    en esta clase solo se reciben numeros enteros como elementos de la lista 
    validar si los elementos de la lista padre son enteros. si son enteros se los agrega de lo contratio nop
    """
    def __init__(self, elementos=[]):
        for elemento in elementos:
            self._validarElemento(elemento)
            super().__init__(elementos)    
    def _validarElemento(self, elemento):
        """ 
        Método que permite validar los elementos de la lista heredada
        la clase padre se encuentra inicializada
        la lista heredada se encuentra inicializada
        elemento, es el elemento a validar. elemento != None && elemento != ""
        validar si el resultado del elemento es entero 
        """
        if not isinstance(elemento, int):
            raise ValueError(f'no es un valor entero:_ {elemento}')
    def agregarElemento(self, elemento):
        """ 
        Método que permite agregar un elemento a la clase padre. este metodo sobreescribe el metodo de la clase padre
        la calse padre se encuentra inicializada
        la lista heredada se encuentr inicializada 
        elemento, es el elemento a agregar a la lista heredada. elemento != None && elemento != ""
        validar que el elemtno sea entero para agregarlo a la lista heredada
        """
        self._validarElemento(elemento)
        super().agregarElemento(elemento)
""" 
Desde aqui se categoriza como herencia multiple
"""
class listaEnterosOrdenada(listaEnteros, listaOrdenada):
    """ 
    clase de ejemplo para realiar la herencia multiple
    la clase de lista enteros se encuentra inicializada y es la que tiene prioridad por eso esta de primera o a la izquierda
    la clase lista ordenada se encuentra inicializada y tiene prioridad baja por eso se encuentra de segunada o a la derecha
    esta clase hereda todos los metodos de las clases padre
    ordenar los elementos de la clase lista enteros con la clase lista ordenada
    """
    pass
""" 
Crear el objeto que permite insertar un nuevo elemento dentro de la lista
probar con este objeto los metodos anteriormente creados 
"""
miLista=ListaSimple([5, 3, 6, 8])
print (miLista)
""" 
Crear el objeto de la clase padre listaSImple hija listaOrdenada 
probar con este objeto hijo los metodos de la clase padre y la clase hijo
"""
miHijaListaOrdenada=listaOrdenada([-1, 20, 9, 8, 7 , 10])
print (miHijaListaOrdenada)
""" 
crear el objeto de la clase padre listaSimple hija listaEnteros 
probar con este objeto hijo los metodos de la clase padre e hijo
"""
miHijaListaEnteros=listaEnteros([5, 1, 2, 3])
print(miHijaListaEnteros)
""" 
crear e objeto de la clase hija listaEnterosOrdenada para comprobar la herencia multiple
probar con este objeto hijo los metodos de la clase padre e hijos 
"""
miListaEnterosOrdenada=listaEnterosOrdenada([1, -4, 5, 6])
print(miListaEnterosOrdenada)
""" 
para saber el orden de las clases que se ejecutan con la herencia se utiliza lo siguiente
termino MRO o metodo de resolucion de orden 
"""
print(listaEnterosOrdenada.__mro__)