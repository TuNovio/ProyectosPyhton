"""Funciones importadas desde otros archivos"""
#Argumentos para funciones o prametros
#variable para ingresar el primer valor a sumar
num1=0
num1=int(input("Ingrese el valor del primer valor a sumar:_"))
#vbariable para ingresar el segundo valor a sumar
num2=0
num2=int(input("Ingrese el valor del segundo valor a sumar:_"))
#vavialbe para sumar
suma=0
#declaracion de la funcion
def funcionParametro(numero1, numero2):
    suma=numero1+numero2
    print(suma)
funcionParametro(num1, num2)
