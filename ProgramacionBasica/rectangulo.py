""" 
#crear una clase llamada rectangulo 
#se quiere un metodo para hallar el area del rectangulo 
#el usuario debe digitar los valores de base y altura del rectangulo
#Declaracion de la clase
"""
class Rectangulo:
    """ 
    #Constructor de la clase que tiene los valores del rectangulo
    #nBase es la base del rectangulo, nBase>0 && nBase!=null
    #nAltura es la altura del rectangulo, nAltura>0 && nAltura!=null
    """
    def __init__(self, nBase, nAltura):
        self.base = nBase
        self.altura=nAltura
    """ 
    #metodo que realiza la accion de hallar el area del rectangulo dado 2 valores
    #retorna el valor del area del rectangulo
    """
    def areaRectangulo(self):
        area=self.base*self.altura
        return area
""" 
#se pide al usuario los valores de la base y altura del rectangulo
#x es la base del rectangulo, x>0 && x!=null
#y es la altura del rectangulo, y>0 && y!=null
#Se ingresan los valores digitados por el usuario a la funcion del area
#se muestra en un mensaje el resultado o el area del rectangulo
"""
x=int(input("Ingrese el valor de la base del rectangulo:_"))
y=int(input("Ingrese el valor de la altura del rectangulo:_"))
miRectangulo=Rectangulo(x,y)
print(f"El area del rectangulo es:_{miRectangulo.areaRectangulo()}")