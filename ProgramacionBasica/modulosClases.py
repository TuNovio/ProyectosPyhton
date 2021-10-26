""" 
#creacion de modulos y manejo de clases en python
#se importa el modulo de la clase aritmericaClases que contiene las operaciones basicas
#de aritmetica tal como +-*/
"""
#calse importada
from aritmeticaClases import Operaciones as op
#metodo para el mensaje que da los resultados de las operaciones
def mensaje():
    print (f'''
        EL resultado de las operaciones es:_
        Suma:_{miOperacion.suma()}
        Resta:_{miOperacion.restar()}
        Multiplicacion:_{miOperacion.multiplicar()}
        Division:_{miOperacion.dividir()}''')
""" 
#dejamos que el usuario digite 2 valores para el desarrollo de las operaciones
#numero1 es el valor del primer numero a sumar, numero1>0 && numero1!=""
#numero2 es valor del segundo numero a sumar, numero2>0 && numero2!=""
#se crea un objeto de tipo op que asigne los valores a digitar
#se llama al metodo de mensajes para visualizar el resultado de las operaciones
"""
numero1=int(input("Ingrese el valor del primer numero a sumar:_"))
numero2=int(input("Ingrese el valor del segundo numero a sumar:_"))
miOperacion=op(numero1,numero2)
mensaje()