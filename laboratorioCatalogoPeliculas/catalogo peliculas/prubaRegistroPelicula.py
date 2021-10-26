""" 
#Clase para realizar el registro de las peliculas
#se debe importar las clases pelicula y catalogo
#se crea un menu con las isguientes obciones (agregar, listas, eliminar, salir)
"""
#importar la clase pelicula
from dominio.pelicula import Pelicula as pl
#importar la clase catalogo
from servicio.catalogo import Catalogo as cl
#menu
#se crea una varible para capturar la eleccion del usuario 
opcion=None
while  opcion != 4:
    try:  
        print("opciones")
        print("1:_ agregar peliculas")
        print("2:_ listar peliculas")
        print("3:_ eliminar catalogo de peliculas")
        print("4:_ salir")
        opcion=int(input("Ingresa la opción:_"))
        if opcion==1:
            nombre=input("Ingrese el nombre de la pelicula:_")
            miPelicula= pl(nombre)
            cl.agregarPelicula(miPelicula)
        elif opcion==2:
            cl().listarPeliculas()
        elif  opcion==3:
            cl.eliminarPelicula()
    except Exception as e:
        print(f"Error:_{e}")
    finally:
        opcion=None
else:
    print("Gracias por utilizar nuestro programa")
