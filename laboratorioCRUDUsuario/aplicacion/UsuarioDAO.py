# importar la libreria para el manejo de la base de datos
# DAO data acces object
from logging import log
#importar la libreria para la base de datos en postgres
import psycopg2 as pd
# importar la clase conexion
from ConexionBD import Conexion
# importar la clase persona
from Usuario import Usuario
# importar el loggin-per para las pruebas
from loggerBase import logg


class UsuarioDAO:
    """
    Se crean las sentencias SQL como atributos de clase
    SELECCIONAR, es la sentencia SQL que permite consultar datos del usuario
    INSERTAR, es la sentencia SQL que permite registrar datos del usuario
    ACTUALIZAR, es la sentencia SQL que permite realizar cambios a los datos del usuario
    ELIMINAR, es la sentencia SQL que permite eliminar al usuario de la base de datos
    """
    # selecionar todos los usuarios de la base de datos
    _TODO = 'select * from usuario order by identificador'
    # seleccionar un usuario dado la identificacion
    _SELECCIONARDATO = 'select nombre, pasword from usuario where identificador = %s'
    # registrar un usuario en la base de datos
    _INSERTAR = 'insert into usuario (identificador, nombre, pasword) values(%s, %s, %s)'
    # cambiar la informacion del usuario
    _ACTUALIZAR = 'update usuario set nombre=%s, pasword=%s where identificador=%s'
    # eliminar un usuario de la base de datos
    _ELIMINAR = 'delete from usuario where identificador=%s'
    
    @classmethod
    def consultarTodo(cls):
        """
        Metodo que permite listar los usuarios de la base de datos
        la sentencia SQL que permite listar los datos ya se encuentra inicializada
        la conexión con la base de datos ya se encuentra establecida
        retornar la lista de usuarios de la base de datos
        """
        try:
            cursor = Conexion.darCursor()
            cursor.execute(cls._TODO)
            registro = cursor.fetchall()
            listaUsuario = []
            for record in registro:
                miUs = Usuario(record[0], record[1], record[2])
                listaUsuario.append(miUs)
            return listaUsuario
        except Exception as e:
            print(f"Error\u261E{e}")
            log.error(
                f"Error al momento de realizar la consulta de datos\u261E{e}")
        finally:
            return listaUsuario

    @classmethod
    def consultarUsuario(cls, nIdentificador):
        """
        Metodo que permite realizar la consulta de los datos de un usuario dando su identificacion
        la sentencia que permite realizar la consulta ya se encuentra inicializada
        la conexión con la base de datos ya se establcio
        nIdentificador, es el identificador del usuario. nIdentificador > 0 && nIdentificador != NaN
        retorna los datos del usuario
        """
        try:
            cursor = Conexion.darCursor()
            cursor.execute(cls._SELECCIONARDATO, (nIdentificador,))
            registro1 = cursor.fetchone()
            usuarios = []
            if registro1 != None:
                usuarios.append(registro1)
                logg.debug(registro1)
                return f'El usuario es:\u261E {registro1}'
            else:
                print(f"No existe el usuario \u261E {nIdentificador}en la base de datos")
        except Exception as e:
            print(f"Error\u261E{e}")
            logg.error(f"Error al momento de consultar los datos\u261E{e}")
        finally:
            return f'\u261E {registro1}'
    
    @classmethod
    def registrarUsuario(cls, usuario):
        """
        metodo que permite realizar el registro de la informacion del usuario
        la sentencia que permite realizar el registro ya se establacio
        la conexión con la base de datos ya se establecio
        usuario, es el objeto de usaurio que contiene el nombre y contraseña
        retorna un mensaje de validacion
        """
        try:
            with Conexion.darConexion():
                with Conexion.darCursor() as cr:
                    # valores a ingresar de la persona
                    valores = (usuario.getIdentificador,
                               usuario.getNombre, usuario.getContraseña)
                    cr.execute(cls._INSERTAR, valores)
                    logg.debug(f"Usuario registrado\u261E{usuario}")
                    return cr.rowcount
        except Exception as e:
            print(f"Error:_ {e}")
            logg.error(f"Error al registrar lo informacion\u261E{e}")
        finally:
            print("\u261E exito")
    
    @classmethod
    def cambiarDatos(cls, usuario):
        """
        Metodo que permite cambiar la informacion del usuario
        la sentencia que permite realizar el cambio ya se encuentra inicializada
        la conexión con la base de datos ya se encuentra inicializada
        usuario, el objeto de tipo Usuario que contiene el nombre y contraseña
        retorna un mensaje de validacion
        """
        try:
            with Conexion.darConexion():
                with Conexion.darCursor() as cr:
                    # valores a ingresar de la persona
                    valores = (usuario.getIdentificador,
                               usuario.getNombre, usuario.getContraseña)
                    cr.execute(cls._ACTUALIZAR, valores)
                    logg.debug(f"Informacion actualizada\u261E{usuario}")
                    return cr.rowcount
        except Exception as e:
            print(f"Error\u261E{e}")
            logg.error(f"Error al actualizar lo informacion\u261E{e}")
        finally:
            print("Se cirra la sentencia de actualizar datos ")
    
    @classmethod
    def eliminarUsuario(cls, nIdentificacion):
        """
        Metodo que permite eliminar la informacion del usuario
        la sentencia que permite realizar la eliminación del usuario ya se encuentra inicializada
        usuario, es el objeto de tipo usuario que contiene el nombre y la contraseña
        retorna el mensaje en donde se especifique la eliminacion del usuario
        """
        try:
            with Conexion.darConexion():
                with Conexion.darCursor() as cursor:
                    # identificador del usuario a eliminar
                    cursor.execute(cls._ELIMINAR, (nIdentificacion,))
                    logg.debug(f"Usuario eliminado:_{nIdentificacion}")
                    return cursor.rowcount
        except Exception as e:
            print(f"Error:_ {e}")
            logg.error(
                f"Error al momento de eliminar a un usuario con identificacion:_ {nIdentificacion}")
        finally:
            print("Fin del proceso eliminarUsuario")


"""
comprobacion del funcionamiento de las sentencias
"""
""" if __name__ == '__main__':
    mius = Usuario(1, "falsa", 192)
    registrarus=UsuarioDAO.registrarUsuario(mius)
 """
