import random
#se establecen las combinaciones para generar la contrasenia con las siguientes variables
#palabras en minuscula
lower = "abcdefghijklmnopqrstyvwxyz"
#palabras en mayuscula
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#numeros de 0 a 10 
numeros = "0123456789"
#simbolos que encierran llavas corchetes, etc
simbolos = "[]{}()*;/,._-"
#se combinan las variables para generar una clave
combinar = lower + upper + numeros + simbolos
#se da una extension a la clave en este caso de 16 digitos
extension = 16
#se genera la contrasenia
contrasenia = "".join(random.sample(combinar, extension))
#visualizar el valor de la contrasenia generada
print(contrasenia)
