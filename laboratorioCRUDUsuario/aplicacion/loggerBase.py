#se importa la libreria que permite registrar los datos del proceso 
import logging as logg
#establecer una configuracion basica 
#el mensaje muestra la fecha, nivel, archivo, linea, y lo escribe en un documento
logg.basicConfig(level=logg.DEBUG, 
                format='%(asctime)s: %(levelname)s [%(filename)s: %(lineno)s] %(message)s', 
                datefmt='%I:%M:%S:%S', handlers=[
                    logg.FileHandler('laboratorio CRUD usuario\documentos\capaDatos.log'),
                    logg.StreamHandler()
                ])
#Crear la regla para llamar al archivo de escritura del proceso
if __name__ == '__main__':
    #mensaje para verificar el debug
    logg.debug("Mensaje al nivel debug")
    #mensaje de error
    logg.info("Mensaje de informacion")
    #mensaje de peligro
    logg.warning("Mensaje de alerta")
    #mensaje critico 
    logg.critical("mensaje critico")