""" 
#Creacion de bases de datos o manejo de imformacion
#manejo de informacion dentro de una base de datos
#instalar el modulo de mysql para conectar python
"""
#se importa el conector de postgres para python
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
    #se crea un cursor para enviar las sentencias sql
    cursor=conexion.cursor()
    #se crea una cadena para seleccionar todos los objetos de la tabla
    sentencia='select identificacion, nombre from persona'
    #se ejecuta la sentencias
    cursor.execute(sentencia)
    #se realiza la recuperacion de los registros
    registros=cursor.fetchall()
    print (registros)
except Exception as e:
    print(f"Error:_{e}")
finally:
    print("se cierra la base de datos")
    conexion.close()
    cursor.close()