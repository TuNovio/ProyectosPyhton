"""
#transacion es decir realizar varias consultas a la base de datos 
#selecionar, eliminar, actualizar, insertar 
#trasaccion ejecuta todas las sentencias SQL a la base de datos  
#todos los cambios u operaciones deben ser exitosos de lo contrario no se desarrolla 
"""
import psycopg2 as bd
#se realiza la lectura de los datos 
#se realiza la conexion a la base de datos en postgres
#se necesita: (usuario, contraseña, direccion ip o host, puerto, nombre de la base de datos )
#se realiza la captura de un error
try:
    conexion = bd.connect(
        user='postgres',
        password='5x5W12',
        host='localhost',
        port='5432',
        database='paraPython')
    print("Se inicializa la base de datos")
    with conexion:
        with conexion.cursor() as cursor:
            """ 
            #realizar las transaciones o sentencias sql
            """
            #crear las sentencias 
            #se seleccionan los datos dado la identificacion
            selecionar = 'select * from persona where identificacion=%s'
            #identificacion a seleccionar
            selecP=(12,)
            #se ejecuta la sentencia sql
            cursor.execute(selecionar, selecP)
            #asignar los registros a una variable
            registros=cursor.fetchall()
            #se insertan los siguientes datos en la base de datos
            insertar = 'insert into persona(identificacion, nombre, edad, peso) values (%s, %s, %s, %s)'
            #valores a insertar
            valoresInsert = (15, "Castro", 30, 90)
            #ejecutar la sentencia
            cursor.execute(insertar, valoresInsert)
            #enviar las sentencias a la base de datos 
            #conexion.commit()
            #Commit se desarrolla de manera automatica si se hace con wiht
            #mensaje para saber si se realiza la transacion 
            print(f"Se realizo la transaccion")
            #mensaje para obtener los registros
            print(f"Los datos de la busqueda son:_{registros}")
            #mensaje de alerta porque se insertaron los datos
            print("se insertaron los datos")
except Exception as e:
    #conexion.rollback()
    #el rollback se desarrolla de manera automatica si se utiliza wiht
    print(f"Error:_{e}")
finally:
    print("se cierra la base de datos")
    conexion.close()