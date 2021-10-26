"""
#manejo de mensajes de error 
#postgres no muestra los mensajes 
#crear los errores para mostrar el error en pantalla 
"""
""" 
#se modifica un archivo en postgres llamado postgres.config
#se cambia el idima que enseña los errores a ingles 
"""
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
            sentencia='select nombre from persona where identificacion = %s'
            ide= int(input("Ingresa la identificacion de la persona:_"))
            #se ejecuta la sentencias
            cursor.execute(sentencia, (ide,))
            #se realiza la recuperacion de los registros
            registros=cursor.fetchall()
            print (registros)
except Exception as e:
    print(f"Error:_{e}")
finally:
    print("se cierra la base de datos")
    conexion.close()
