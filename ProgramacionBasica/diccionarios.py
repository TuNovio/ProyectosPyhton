#lado izquierdo lllave o key
""" diccionarios en python """
#lado derecho valor adjudicado a la llave
#ubicacion cardinal del animal [nore, sur, este, oeste]
""" atributos para la lista de lugar """
ubicacion=""
#tipo de establecimiento
tipoCasa=""
#sublista con los datos del lugar
lugar=[ubicacion, tipoCasa]
#lista que contiene los datos de la ubicacion del animal como la ubicacion cardinal y si es jaula o caseta
listaLugar=[lugar]
""" atributos para la lista de animales """
#identificacion del animal
identificacion=11
#Edad del animal
edad=30
#peso del animal
peso=50
#especie del animal
especie="vipedo"
#sublista con los datos del animal tal como la identificacion, edad, peso y especie
datosAnimal=[identificacion, edad, peso, especie]
#lista que contiene los animales del zoologico
listaAnimal=[datosAnimal]
#diccionario que tiene la lista de las caracteristicas del lugar en donde estan los animales
zona={
    "Ubicacion": listaLugar
}
#diccionario que tiene la lista con los animales del zoologico
animal={
    "datos": listaAnimal
}
#diccionario que tiene los diccionarios con la lista de los lugares y animales del zoologico
zoologico={
    "animales":animal,
    "Lugar": zona
}
#panel de obciones a realizar
print(f'''Seleccione una operacion a realizar
      1) Añadir un animal en el zoologico
      2) Buscar un animal en el zoologico
      3) Eliminar un animal del zoologico
      4) salir del programa''')
#el usuario digita la opcion que quiera y se almacena en una variable
eleccion=int(input("Ingrese la opcion que desee realizar:_"))
#se desarrolla un ciclo en donde la eleccion debe ser<4 de lo contrario se cierra el programa
while eleccion<4:
    #condicional para preguntar cuan opcion eligio
    if eleccion==1:
        #se dicen los datos que el usuario debe digitar para realzar la operacion
        print("Elige una opción que desees realizar")
        print("1) ID | 2) Edad | 3) Peso | 4) especie")
        #identificacion del animal
        idAnimal=int(input("Ingrese la ID del animal a ingresar al zoologico:_"))
        #edad del animal a ingresar al zoologico
        edadAnimal=int(input("Ingrese la edad del animal a ingresar al zoologico:_"))
        #peso del animal a ingresar al zoologico
        pesoAnimal=int(input("Ingrese el peso del animal a ingresar al zoologico:_"))
        #especie del animal a ingresar al zoologico
        especieAnimal=input("Ingrese la especie del animal a ingresar al zoologico:_")
        #se reemplazan los valores de la sublista
        #datos en la posicion 0 es id
        datosAnimal[0]=idAnimal
        #datos en la posicion 1 es edad
        datosAnimal[1]=edadAnimal
        #datos en la posicion 2 es peso
        datosAnimal[2]=pesoAnimal
        #datos en la posicion 3 es especie
        datosAnimal[3]=especieAnimal
        #visualizar la lista con los datos para verificar si los datos ingresados estan presentes
        print(datosAnimal)
    #condicional para preguntar que opcion se elige
    if eleccion==2:
        #mensaje con la informacion necesaria para realizar la operacion
        print("Para buscar al animal es necesario que digites el id del animal")
        #se toma el dato pedido y se lo almacena en una variable
        busqueda=int(input("Ingrese la identificacion del enimal que busca:_"))
        #se recorre la lista en donde estan los datos de todos los animales
        for i in listaAnimal:
            #se toma la lista con la posicion y se lo asigna a otra variable
            #se toma la identificacion
            ident=i[0]
            #se toma la edad
            tEdad=i[1]
            #se toma el peso
            tPeso=i[2]
            #se toma la especie
            tEspecie=i[3]
            #se pregunta si el dato que el usuario ingreso es igual al dato en la lista
            if busqueda==ident:
                print(f'''
                      El animal que estas buscando tiene la siguiente informacion
                      Identificacion: {ident}
                      Edad: {tEdad}
                      Peso: {tPeso}
                      Especie: {tPeso}''')
            else:
                print(f'EL animal con la identificacion {busqueda} no existe en el zoologico')
    #mensaje para verificar la opcion elegida
    if eleccion==3:
        #mensaje pra pedir al usuario la informacion necesario para realizr la operacion
        print("Para eliminar un animal en el zoologico necesito de un id:_")
    else:
        break