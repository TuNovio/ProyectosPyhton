"""Manejo de funciones en python"""
#declaracion de funciones
def miFuncion():
    #mensaje de comprobacion de contenido
    print("Hello word desde python utilizando funciones")
miFuncion()
""" Utilizando return en funciones de python """
#variable apra el valor a sumar
numero1=20
#varible para el valor a sumar
numero2=20
#variable que suma los valores
suma=0
#rvarible para imprimir el resultado
resultado=0
#declaracion del metodo
def sumar(a, b):
    suma=a+b
    return suma
resultado=sumar(numero1, numero2)
print(f'El resultado de sumar:_{numero1} + {numero2} es:_ {resultado}')

""" Agregar valores a una lista vacia """
#variable con el valor de la identificacion 
identificacion=0
#variable con los valores del nombre
nombre=""
#variable con los valores de la edad 
edad=0
#variable con los valores del peso
peso=0
#lista con los datos
persona=[identificacion, nombre, edad, peso]
#declaracion del metodo que permite añadir elementos a la lista
#la identificacion debe ser diferente no puede haber 2 valores iguales
#el nombre debe ser una cadena de texto no puede contener numeros 
def añadirPersona(id, nm, ed, ps):
    for i in range(0,4):
        persona[0]=id
        persona[1]=nm
        persona[2]=ed
        persona[3]=ps
        print(persona[i])
#valor de la identificain que el usuario digita
valorId=int(input("Ingrese el valor de la identificaion de la persona que quiere ingresar a la lista:_"))
#valor del nombre que el usuario digita
valorNombre=input("Ingrese el valor del nombre de la persona que quiere ingresar a la lista:_")
#valor de la edad que el usuario digita
valorEdad=int(input("Ingrese el valor de la edad de la persona que quiere ingresar a la lista:_"))
#valor del peso que el usuario digita
valorPeso=int(input("Ingrese el valor del peso de la persona que quiere ingresar a la lista:_"))
#llamar al metodo y añadir las variables necesarias 
añadirPersona(valorId, valorNombre, valorEdad, valorPeso)
#mensaje para comprobar que se ingreso la persona a la lista personas
print(f"La persona que ingreso al sistemas es:_{persona[1]}")

""" Insertar valores para diccionario """
#para ingresar terminos en la funcion se utilizan doble asterisco
def listaTerminos(**terminos):
    for llave, valor in terminos:
        print(F'''
              llave:_{llave}
              valro:_{valor}''')
listaTerminos(IDE="110", pk="Alfonso")

""" funcion que recibe una lista de elementos """
#lista
nombres=["alfonso", "carla", "guillermo"]
#declaracion del metodo para recorrer la lista de nombres
def listaNombre(nNombres):
    for i in nNombres:
        #mensaje con los nombres
        print(i)
listaNombre(nombres)