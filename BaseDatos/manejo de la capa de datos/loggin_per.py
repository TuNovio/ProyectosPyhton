#se imnporta la libreria de login para mostrar mensajes
import logging as log
#llamar configuracion basica
#damos formato a la fecha
#mensaje que muestra la fecha, hora, nivel, documento, linea de error y almacena en un archivo.log
log.basicConfig(level=log.DEBUG, 
                format='%(asctime)s: %(levelname)s [%(filename)s: %(lineno)s] %(message)s', 
                datefmt='%I:%M:%S:%S', handlers=[
                    log.FileHandler('mi base de datos\manejo de la capa de datos\Documentos\capaDatos.log'),
                    log.StreamHandler()
                ])
if __name__ == '__main__':
    #mensaje para verificar el debug
    log.debug("Mensaje al nivel debug")
    #mensaje de error
    log.info("Mensaje de informacion")
    #mensaje de peligro
    log.warning("Mensaje de alerta")
    #mensaje critico 
    log.critical("mensaje critico")