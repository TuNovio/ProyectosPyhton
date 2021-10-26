#importar la libreria para manejar datos sql
import psycopg2 as bd
#importar la clase loggin_per para probar
from loggin_per import log
#importar el finalizador del programa
import sys
class  Conexion:
    #usuario de la base de datos
    user='postgres'
    #contraseña de la base de datos
    pasword='5x5W12'
    #host de la base de datos
    host='localhost'
    #puerto por el cual se conecta
    puerto='5432'
    #nombre de la base de datos a la que se apunta
    baseDatos='paraPython'
    #conexion con la base de datos 
    conexion=None
    #cursor para escribir o enviar las sentencias SQL
    cursor=None
    """ 
    #Metodo que establece la conexion
    #los atributos de clase necesarios ya se encuentran inicializados 
    #retorna la conexion con la base de datos 
    """
    @classmethod
    def obtenerConexion(cls):
        if cls.conexion==None:
            try:
                cls.conexion=bd.connect(
                    user=cls.user,
                    password=cls.pasword,
                    host=cls.host,
                    port=cls.puerto,
                    database=cls.baseDatos
                )
                log.debug(f"Conexión exitosa:_ {cls.conexion}")
                return cls.conexion
            except Exception as e:
                print(f"Error:_ {e}")
                log.error(f"Ocurrio un error al obtener el conector:_{cls.conexion}")
                sys.exit
        else:
            return cls.conexion
    """ 
    #Metodo que retorna el cursor 
    #los atributos necesarios para crear el cursor ya estan inicializados
    #retorna el cursor
    """
    @classmethod
    def obtenerCursor(cls):
        if cls.cursor==None:
            try:
                cls.cursor = cls.obtenerConexion().cursor()
                log.debug(f"Se inicio correctamente el cursor:_ {cls.cursor}")
                return cls.cursor
            except Exception as e:
                print(f"Error:_ {e}")
                log.error(f"Ocurrio un error al obtener el cursor:_{cls.cursor}")
                sys.exit
        else:
            return cls.cursor
#pruebas para la conexion 
""" if __name__ == '__main__':
    Conexion.obtenerConexion()
    Conexion.obtenerCursor() """