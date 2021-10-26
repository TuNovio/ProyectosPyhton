""" 
#Importar la clase registro para poder hacer la correspondiente inicializacion de los datos
"""
"clase registro"
from Registro import Registro as miRegistro
"lista con las personas registradas"
listaRegistros=[]
""" 
#se registraran los datos en la calse para comprobar
#Identificacion, es la identificacion a ingresar por el usuario
#Nombre, es el nombre a ingresar por el usuario
#Edad, es la edad a ingresar por el usuario
#Profesion, es la profesion de la persona ingresada por el usuario
#Salario, es el salario de la persona ingresada por el usuario
#Tipo de subsidio, es el tipo de subsidio de la persona ingresada por el usuario
#se debe imprimir un mensaje con la operacion de registro y los nuevos datos
"""
def registrarDatos(nIdentificacion, nNombre, nEdad, nProfesion, nSalario, nSubsidio):
    persona1=miRegistro().registrarPersona(nIdentificacion, nNombre, nEdad, nProfesion, nSalario, nSubsidio)
    listaRegistros.append(persona1)
    valor=len(listaRegistros)
    print(f"Hay:_ {valor} registros realizados")

""" 
#formulario para el ingreso de datos a traves del usuario o la interfaz grafica
#los datos deben ser digitados correctamente y con los respectivos tipos 
#nIdentificacion es la identificacion de la persona a registrar por el usuario. nIdentificacion > 0 && nIdentificacion != None
#nNombre es el nombre de la persona a registrar por el usuario. nNombre != None && nNombre != ""
#nEdad es la edad de la persona a registrar por el usuario. nEdad > 0 && nEdad != None
#nProfesion es el trabajo de la persona a registrar por el usuario nTrabajo != None && nTrabajo != ""
#nSalario es el salario recibido por la persona a registrar por el usuario. nSalario > 0 && nSalario != None
#nSubsidio es el subsidio recibido por la persona a registrar por el usuario. nSubsidio != None && nSubsidio != ""
#si el trabajo no es digitado eso quiere decir que la persona esta desempleada por lo tanto no tiene un salario
#si no se digita el valor del subsidio eso quiere decir que la persona no esta asegurada y por lo tanto se despliega un mensaje de alerta 
#se debe mostrar en pantalla los registros realizados y los datos de las personas registradas 
"""
"identificacion de la persona a registrar"
nIdentificacion=int(input("Ingrese el número de identificacion de la persona a registrar:_"))
"nombre de la persona a registrar"
nNombre=input("Ingrese el nombre de la persona a registrar:_")
"edad de la persona e registrar"
nEdad=int(input("Ingrese la edad de la persona a registar:_"))
"profesión de la persona a registrar"
nProfesion=input("Ingrese la profesión de la persona a registrar:_")
"salario de la persona a registrar"
nSalaraio = int(input("Ingrese el valor del salario de la persona a registrar:_"))
"subsidio de la persona a registrar "
nSubsidio=input("Ingrese el subsidio al que pertenece la persona a registrar:_")
registrarDatos(nIdentificacion, nNombre, nEdad, nProfesion, nSalaraio, nSubsidio)

