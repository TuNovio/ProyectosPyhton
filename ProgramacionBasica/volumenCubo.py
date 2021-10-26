""" 
#crear una clase llamada cubo 
#se quiere un metodo para hallar el volumen del cubo 
#el usuario debe digitar los valores de profundidad, ancho y altura del cubo
#Declaracion de la clase
"""
class Cubo:
    """ 
    #Constructor de la clase que tiene los valores del cubo
    #nprofunco es la profundidad del cubo, nBase>0 && nBase!=null
    #nAltura es la altura del cubo, nAltura>0 && nAltura!=null
    #nAncho es el ancho del cubo, nCubo>0 && nCubo!=null
    """
    def __init__(self, nAncho, nProfundo, nAltura):
        self.ancho=nAncho
        self.profundo=nProfundo
        self.altura=nAltura
    """ 
    #metodo que realiza la accion de hallar el volumen del cubo dado 3 valores
    #retorna el valor del volumen del cubo
    """
    def volumenCubo(self):
        area=self.profundo*self.altura*self.ancho
        return area
""" 
#se pide al usuario los valores de la profundidad, altura y ancho del cubo
#x es la profundidad del cubo, x>0 && x!=null
#y es la altura del cubo, y>0 && y!=null
#z es el ancho del cubo, z>0 && z!=null
#Se ingresan los valores digitados por el usuario a la funcion del volume
#se muestra en un mensaje el resultado o el volumen del cubo
"""
x=int(input("Ingrese el valor de la profundidad del cubo:_"))
y=int(input("Ingrese el valor de la altura del cubo:_"))
z=int(input("Ingrese el valor del ancho del cubo:_"))
micubo=Cubo(x,y,z)
print(f"El volumen del cubo es:_{micubo.volumenCubo()}")