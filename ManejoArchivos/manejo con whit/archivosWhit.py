""" 
#se utilizara el whit para utilizar el archivo
"""
class ManejoArchivos:
    def __init__(self, nNombre):
        self.nombre=nNombre
    def __enter__(self):
        print("Entrando al recurso:".center(50, '-'))
        self.nombre=open(self.nombre, 'r', encoding="UTF-8")
        return self.nombre
    def __exit__(self, tipoException, valorException, trazaError):
        print("Cerramos el recurso".center(50, '-'))
        if self.nombre:
            self.nombre.close()