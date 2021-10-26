""" determinar la estacion del año segun el mes que el usuario proporcione """
mes = int(input("Ingrese el mes del año que desees (1-12):_"))
estacion = ""
if mes==1 or mes ==12 or mes==2:
    estacion="invierno"
elif mes==3 or mes==4 or mes==5:
    estacion="Verano"
else:
    estacion="otoño"
print(f'La estacion para el mes:_ {mes} es:_ {estacion}')


