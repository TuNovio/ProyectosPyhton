""" 
#se automatiza el proceso de conexión a la base de datos 
#se necesita importar la libreria 
"""
#importar libreria
import psycopg2
#se realiza la lectura de los datos 
#se realiza la conexion a la base de datos en postgres
#se necesita: (usuario, contraseña, direccion ip o host, puerto, nombre de la base de datos )
#se realiza la captura de un error
try:
    conexion = psycopg2.connect(
        user='postgres',
        password='5x5W12',
        host='localhost',
        port='5432',
        database='paraPython')
    print("Se inicializa la base de datos")
    #se utiliza wiht para automatizar la conexion
    with conexion:
        with conexion.cursor() as cursor:
            #se crea una cadena para actualizar el dato de nombre de la tabla dado el identificador
            sentencia='update persona set nombre=%s where identificacion=%s'
            #se ejecuta la sentencias
            cursor.execute(sentencia, ("judas", 11),)
            #enviar valores o insertar valores en la base de datos
            #no es necesario crear el commit
            conexion.commit()
            print("Se actualizaron los datos")
except Exception as e:
    print(f"Error:_{e}")
finally:
    print("se cierra la base de datos")
    conexion.close()