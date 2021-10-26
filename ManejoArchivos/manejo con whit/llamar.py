""" 
#se lee el archivo y se lo manda a la clase creada para manejar archivos
#Se importa la clase que tiene el procedimiento de lectura de archivos
#se le conoce como administrador de recursos
"""
from archivosWhit import ManejoArchivos as lector
""" 
#se procede a leer el archivo y enviarlo a la clase que posee el procedimiento
"""
with lector('Manejo de archivos\manejo con whit\lectura.txt') as archivo:
    print (archivo.read())