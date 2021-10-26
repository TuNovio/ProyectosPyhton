""" 
#Manejo de los distintos tipos de errores 
#existendistintos tipos y aqui se mirara como manejar los mas conocidos
"""
#division entre 0
from _typeshed import IdentityFunction


try:
    error1=10/0
except Exception as e:
    print (f"Error:_ {e}")
finally:
    print("Digite un valor valido")
#division entre int/string
try:
    error1=10/"g"
except Exception as e:
    print (f"Error:_ {e}")
finally:
    print("Digite un valor valido")
""" 
#error personalizado es decir nosotros elegimos cuando sucede el error
#debemos crear una clase para realizar la operacion
#la clase debe ser unicamente para el tipo de error que nosotros generemos
"""
class NumerosIdenticosException(Exception):
    def __init__(self, mensaje):
        self.mensaje=mensaje
try:
    a=1
    ab=1
    if a==ab:
        raise NumerosIdenticosException("NumerosIdenticos")
except Exception as e:
    print (f"Error:_ {e}")
finally:
    print("Digite un valor valido")