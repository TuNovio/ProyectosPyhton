""" llamar el valor de una funcion dentro de otra """
""" se utiliza una funcion aleatoria """
#lista
nombres=["alfonso", "carla", "guillermo"]
#valor minimo lista
mn=min(nombres)
#valor mximo lista
mx=max(nombres)
#declaracion del metodo para recorrer la lista de nombres
def listaNombre(nNombres):
    for i in nNombres:
        #mensaje con los nombres
        print(i)
def añadirNombre(name1):
    #lista con mas nombres
    subNombre=[name1]
    listaNombre(subNombre)
    print(nombres)
listaNombre(nombres)
add1=input("Ingresa el nombre de la persona a registrar:_")
añadirNombre(add1)