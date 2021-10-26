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
            #se crea una cadena para seleccionar todos los objetos de la tabla
            #sentencia='select * from persona where identificacion in (11,12)'
            sentenciaSQL='select * from persona where identificacion in %s'
            #se crea una varible para convertirla en tupla
            entrada=input("Ingrese las identificaciones de los usuarios separadas por comas:_")
            #se convierte en tupla
            llaves=(tuple(entrada.split(',')),)
            #se ejecuta la sentencias
            cursor.execute(sentenciaSQL, llaves)
            #se realiza la recuperacion de los registros
            registros=cursor.fetchall()
            for i in registros:
                print (i)
except Exception as e:
    print(f"Error:_{e}")
finally:
    print("se cierra la base de datos")
    conexion.close()