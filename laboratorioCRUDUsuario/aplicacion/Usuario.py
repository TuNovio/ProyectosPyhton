from loggerBase import logg


class Usuario:
    """ 
    Declarar el metodo constructor de la clase Usuario 
    nIdentificador, es la id del usuario. nIdentificador > 0 && nIdentificador != NaN
    nNombre, es el nomnbre del usuario o de la cuenta del usuario. nNombre != None && nNombre != ""
    nContraseña, es la contraseña para la cuenta del usuario. nContraseña > 0 && nContraseña != NaN
    los atributos son privados por lo tanto se deben inicializar de manera correcta
    """

    def __init__(self, nIdentificador, nNombre, nContraseña):
        # identificador del usuario
        self._identificador = nIdentificador
        # nombre de la cuenta o usuario
        self._nombre = nNombre
        # contraseña de la cuenta o usuario
        self._contraseña = nContraseña
    """ 
    Metodo que retorna en formato mensaje los atributos de la instancia
    los atributos ya se encuentran inicializados
    retorna una cadena de caracteres
    """
    def __str__(self):
        return f'''
    Identificador:_ {self._identificador}
    Nombre:_ {self._nombre}
    Contraseña:_ {self._contraseña}
    '''

    @property
    def getIdentificador(self):
        """ 
        metodo que retorna el identificador del usuario
        el atritubo de identificador ya se encuentra inicializado
        retorna el identificador del usuario
        """
        return self._identificador

    @getIdentificador.setter
    def setIdentificador(self, nIdentificador):
        """ 
        metodo que cambia el valor del identificador del usuario
        el atributo de identificador ya se encuentra inicializado
        nIdentificador, es el identificador del usuario
        cambia el valor del identificador
        """
        self._identificador = nIdentificador

    @property
    def getNombre(self):
        """ 
        metodo que retorna el nombre de la cuenta o usuario 
        el atributo de nombre ya se encuentra inicializado
        retorna el nombre de la cuenta o  usuario
        """
        return self._nombre

    @getNombre.setter
    def setNombre(self, nNombre):
        """ 
        Metodo que cambia el valor del nombre de la cuenta o usuario
        el atributo de nombre ya se encuentra inicializado
        nNombre, es el nombre de la cueta. nNombre != None && nNombre != ""
        cambia el valor del atributo nombre por nNombre
        """
        self._nombre = nNombre
    
    @property
    def getContraseña(self):
        """ 
        Metodo que retorna la contraseña de la cuenta
        el atributo de contraseña ya se encuetra inicializado
        retorna la contraseña de la cuenta
        """
        return self._contraseña
    
    @getContraseña.setter
    def setContraseña(self, nContraseña):
        """ 
        Metodo que cambia el valor de la contraseña 
        el atributo de la contraseña ya se encuetra inicializado
        nContraseña, es la contraseña de la cuenta
        cambia el valor de la contraseña por nContraseña
        """
        self._contraseña = nContraseña


""" 
Pruebas
"""
if __name__ == '__main__':
    usu = Usuario(1, "lucas", 111)
    logg.debug(usu)
