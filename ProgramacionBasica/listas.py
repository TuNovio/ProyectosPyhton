""" manejo de listas en python """
lista1=[[114, "Maria", 4.0],[115, "Juan", 3.5]]
estudiante=[]
#se quiere ingresar un nuevo estudiante
#el estudiante tiene id, nombre y nota
#se le pide al usuario los anteriores datos mensionados
identificacion=int(input("Ingrese la identificacion del estudiante:_"))
nombre=input("Ingrese el nombre del estudiante:_")
nota=float(input("Ingrese la nota del estudiante:_"))
#se crea una sublista que se añadira a la lista principal
estudiante=[identificacion, nombre, nota]
#se agrega la sublista a la lista principal
lista1.append(estudiante)
print(lista1)