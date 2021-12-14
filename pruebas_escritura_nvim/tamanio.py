def mas_larga(palabra):
    letra = ""
    for l in palabra: 
        mayor = len(palabra[0])
        t = len(l)
        if(t > mayor):
            letra = l
        else:
            letra = palabra[0]
    return letra

print(mas_larga(["domingo", "jueves", "lunes", "martes", "miercoles"]))