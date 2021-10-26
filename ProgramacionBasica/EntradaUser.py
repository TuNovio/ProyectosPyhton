""" se solicita al usuario para que proporcione el valor """
num1=int(input("Ingrese el primer numero a sumar: "))
num2=int(input("Ingrese el segundo numero a sumar: "))
suma=0
if num1>0 and num2>0:
    suma=num1+num2
    print("se sumaron los numero y el resultado es: ", suma)
else:
    print("Los valores no se han digitado")
