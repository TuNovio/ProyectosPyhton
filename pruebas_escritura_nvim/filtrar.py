def filtrar(palabras, cont):
    mensaje = ""
    for l in palabras:
        t = len(l)
        if(t > cont):
            mensaje += f"\n {l}"
    return mensaje

lista = ["lunes", "alfonso", "martes", "jupyter", "miercoles", "hercules", "ald"]
con = 5
print(filtrar(lista, con))
 