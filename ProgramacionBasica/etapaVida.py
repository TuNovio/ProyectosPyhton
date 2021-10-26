""" el usuario proporciona un valor y se identifica a que etapa pertenece """
#1. 0-10 infancia
#2. 10-20 muchos cambios y esfuerzo
#3. 20-30 Amor y trabajo
edad=int(input("Ingresa tu edad para establecer a que etapa perteneces:_"))
etapaInfancia="infancia increible"
etapaCambios="muchos cambios y esfuerzo"
etapaAmor="Amor y trabajo"
mensaje=None
for i in range(0, 30):
    if i==0 and i==10:
        if edad==i:
            mensaje=etapaInfancia
    elif i==10 and i==20:
        if edad==i:
            mensaje=etapaCambios
    elif i==20 and i==30:
        if edad==i:
            mensaje=etapaAmor
print(mensaje)