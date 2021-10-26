""" 
#clase en la cual se regitran las peliculas y se realizan las operaciones 
#la clase tiene una lista de peliculas 
#se deben crear metodos (eliminar, agregar, buscar)
#la lista se crea en el catalogo 
#se debe crear un archivo.txt en donde se almacenen los datos de la pelicula
#se importa os para la funcionalidad de eliminacion
"""
import os
class Catalogo:
    """
    #ruta del archivo en el que se guarda la informacion de las peliculas
    #si el archivo no existe se debe crear uno 
    #@static
    """
    rutaArchivo="laboratorio catalogo de peliculas\documentos\peliculas.txt"
    """ 
    #Metodo que permite agregar las peliculas en el documento.txt
    #la ruta del archivo ya se encuentra inicializada
    #se deben capturar los errores que se puedan presentar
    """
    @classmethod
    def agregarPelicula(cls, pelicula):
        try:
            escribir=open(cls.rutaArchivo, 'a', encoding='utf-8')
            escribir.write(f'Titulo: {pelicula.setNombre}\n')
        except Exception as e:
            print(f"Error:_ {e}")
        finally:
            print("Fin del proceso escritura")
            escribir.close()
    """ 
    #metodo que permite visualizar las peliculas registradas
    #la ruta del archivo.txt ya se encuentra inicializada 
    #se deben capturar los errores que se prensenten
    """
    def listarPeliculas(cls):
        ler=None
        try:
            escribir=open(cls.rutaArchivo, 'r', encoding='utf-8')
            ler=escribir.readlines()
            print (ler)
        except Exception as e:
            print(f"Error:_{e}")
        finally:
            print("Fin del proceso de lectura")
            escribir.close()
        return ler
    """ 
    #metodo que permite eliminar el catalogo completo de las peliculas 
    #el archivo.txt de las peliculas debe estar inicializado 
    """
    def eliminarPelicula(cls):
        os.remove(cls.rutaArchivo)
        print("Archivo eliminado")

""" mio=Catalogo()
mio.agregarPelicula("Mariana")
mio.agregarPelicula("jesus")
mio.agregarPelicula("batman")
mio.listarPeliculas() """