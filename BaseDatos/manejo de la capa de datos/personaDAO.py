#importar la libreria para el manejo de la base de datos
#DAO data acces object
import psycopg2 as pd
#importar la clase conexion
from Conexion import Conexion
#importar la clase persona
from Persona import Persona
#importar el loggin-per para las pruebas
from loggin_per import log
class PersonaDAO:
    """ 
    DAO data acces object
    CRUD crear leer actualizar eliminar
    """
    #sentencia que consulta a la base de datos
    _SELECIONAR='select * from persona order by identificacion'
    #sentencia que ingresa datos a la base de datos
    _INSERTAR='insert into persona (identificacion, nombre, edad, peso) values(%s, %s, %s, %s)'
    #sentencia que actualiza los datos de una persona dado la identificacion
    _ACTUALIZAR='update persona set nombre=%s, edad=%s, peso=%s where identificacion=%s'
    #sentencia que elimina a una persona dada la identificacion 
    _ELIMINAR='delete from persona where identificacion=%s'
    
    """ 
    metodo que permite realizar consultar hacia la base de datos
    la sentencia para consultar ya se encuentra inicializada
    retorna el valor de los campos consultados
    """
    @classmethod
    def consultar(cls):
        try:
            with Conexion.obtenerCursor() as cursor:
                cursor.execute(cls._SELECIONAR)
                registro=cursor.fetchall()
                personas=[]
                for record in registro:
                    persona = Persona(record[0], record[1], record[2], record[3])
                    personas.append(persona)
                return personas
        except Exception as e:
            print(f"Error:_ {e}")
            log.error(f"Error al momento de realizar la consulta de datos:_ {e}")
        finally:
            return personas
    """ 
    metodo que permite realizar el envio o insertar información en la base de datos 
    la sentencia que permite insertar datos ya se encuentra incializada
    persona, es el objeto creado de la clase Persona y contiene identificacion, nombre, edad, peso
    validar si la persona ya existe en la base de datos; si la persona existe no se insertan los datos si existe se registra
    retorna un mensaje verificando que los datos si se enviaron en caso contrario capturar el error
    """
    @classmethod
    def insertar(cls, persona):
        try:
            with Conexion.obtenerConexion():
                with Conexion.obtenerCursor() as cr:
                    #valores a ingresar de la persona
                    valores=(persona._identificacion, persona._nombre, persona._edad, persona._peso)
                    cr.execute(cls._INSERTAR, valores)
                    log.debug(f"Persona insertada:_ {persona}")
                    return cr.rowcount
        except Exception as e:
            print (f"Error:_ {e}")
            log.error(f"Error al insertar lo informacion:_ {e}")
        finally:
            print("Se cirra la sentencia de insertar datos ")
    """ 
    metodo que permite realizar la actualizacion de los datos de una persona registrada en el sistema
    la sentencia que permite realizar la actualizacion de los datos ya se encuentra inicializada
    persona, es el objeto creado de la clase Persona y contiene identificacion, nombre, edad, peso
    validar si la persona existe en la base de datos; si la persona no existe se debe registrar
    retornar un mensaje de verificacion
    """
    @classmethod
    def actualizar(cls, persona):
        try:
            with Conexion.obtenerConexion():
                with Conexion.obtenerCursor() as cr:
                    #valores a ingresar de la persona
                    valores=(persona._identificacion, persona._nombre, persona._edad, persona._peso)
                    cr.execute(cls._ACTUALIZAR, valores)
                    log.debug(f"Informacion actualizada:_ {persona}")
                    return cr.rowcount
        except Exception as e:
            print (f"Error:_ {e}")
            log.error(f"Error al actualizar lo informacion:_ {e}")
        finally:
            print("Se cirra la sentencia de actualizar datos ")
    """ 
    metodo que permite eliminar a una persona de la base de datos dado el id de
    la sentencia que permite elminar a la persona ya se encuentra inicializada
    persona, es la persona a eliminar. Contiene identificacion, nombre, edad, peso
    validar si la persona existe en la base de datos; si la persona no existe se debe registrar
    """
    def eliminar(cls, nIdentificacion):
        try:
            with Conexion.obtenerConexion():
                with Conexion.obtenerCursor() as cr:
                    #valores a ingresar de la persona
                    valores=(nIdentificacion)
                    cr.execute(cls._ELIMINAR, (valores,))
                    log.debug(f"Persona eliminada:_ {nIdentificacion}")
                    return cr.rowcount
        except Exception as e:
            print (f"Error:_ {e}")
            log.error(f"Error al eliminar la informacion:_ {e}")
        finally:
            print("Se cirra la sentencia de eliminar a la persona ")

""" 
comprobar el funcionamiento con las pruebas
"""
""" if __name__ == '__main__':
    #eliminar a una persona de la base de datos 
    miPersona = Persona(15, "Carlos", 30, 90)
    personaEliminada=PersonaDAO().eliminar("15")
    log.debug(f"Personas eliminadas:_ {personaEliminada}")
    
#Actualizar la informacion de la persona 
    miPersona = Persona("Carlos", 30, 90, 15)
    personaActualizada = PersonaDAO.actualizar(miPersona)
    log.debug(f'Personas atualizadas:_ {personaActualizada}')
    
#registro de la informacion de la persona en la base de datos 
    miPersona= Persona(16, "Eliza", 50, 70)
    #insertar persona 
    registroPersona=PersonaDAO.insertar(miPersona)
    log.debug(f"Personas insertadas:_ {miPersona}")
    
    #consulta de datos de los registros de persona
    personas = PersonaDAO.consultar()
    for person in personas:
        log.debug(person) """