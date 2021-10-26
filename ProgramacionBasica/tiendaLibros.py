""" tienda de libros"""
#nombre del libro
nombre=input("Ingrese el nombre del libro que desea comprar:_")
#id del libro
id=int(input("Ingrese el ID del libro que desea comprar:_"))
#precio del libro
precio=float(input("Ingrese el valor del libro que desea comprar:_"))
#indicar si el envio es gratuito false true
envio=input("Digite si el envio fue gratuito o no; utilize True/False")
if envio=="True":
    envio=True
elif envio=="False":
    envio=False
else:
    print("Digite un valor entre True/False")
print(f'''
Nombre:_ {nombre}
Id:_ {id}
Precio:_{precio}
envio:_{envio}
      ''')
