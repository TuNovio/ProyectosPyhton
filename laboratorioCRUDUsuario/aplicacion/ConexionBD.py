# importar la libreria para manejar datos sql
import psycopg2 as py
# importar la clase loggin_per para probar
from loggerBase import logg
# importar el finalizador del programa
import sys

class Conexion:
    # usuario de la base de datos
    _user = 'postgres'
    # contraseña de la base de datos
    _pasword = '5x5W12'
    # host de la base de datos
    _host = 'localhost'
    # puerto por el cual se conecta
    _puerto = '5432'
    # nombre de la base de datos a la que se apunta
    _baseDatos = 'paraPython'
    # _conexionBD con la base de datos
    _conexionBD = None
    # _cursorBD para escribir o enviar las sentencias SQL
    _cursorBD = None

    @classmethod
    def darConexion(cls):
        """ 
        Metodo que establece la _conexionBD
        los atributos de clase necesarios ya se encuentran inicializados 
        retorna la _conexionBD con la base de datos 
        """
        if cls._conexionBD == None:
            try:
                cls._conexionBD = py.connect(
                    user=cls._user,
                    password=cls._pasword,
                    host=cls._host,
                    port=cls._puerto,
                    database=cls._baseDatos
                )
                logg.debug(f"Conexión exitosa:_ {cls._conexionBD}")
                return cls._conexionBD
            except Exception as e:
                print(f"Error:_ {e}")
                logg.error(
                    f"Ocurrio un error al obtener el conector:_{cls._conexionBD}")
                sys.exit
        else:
            return cls._conexionBD
    @classmethod
    def darCursor(cls):
        """ 
        Metodo que retorna el _cursorBD 
        los atributos necesarios para crear el _cursorBD ya estan inicializados
        retorna el _cursorBD
        """
        if cls._cursorBD == None:
            try:
                cls._cursorBD = cls.darConexion().cursor()
                logg.debug(
                    f"Se inicio correctamente el cursor:_ {cls._cursorBD}")
                return cls._cursorBD
            except Exception as e:
                print(f"Error:_ {e}")
                logg.error(
                    f"Ocurrio un error al obtener el _cursorBD:_{cls._cursorBD}")
                sys.exit
        else:
            return cls._cursorBD
