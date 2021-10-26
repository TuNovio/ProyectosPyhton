""" 
#lectura de archivos 
#se debe leer el archivo existente 
#si no existe se debe crear
"""
try:
    #Se especifican los acentos o algo parecido utilizando encoding
    archivo=open('Manejo de archivos\Primera actividad\doc.txt', "w", encoding="UTF-8")
    archivo.write("Agregamos información al archivo de alfonso \n")
    archivo.write("Adios")
except Exception as e:
    print(f"Error:_ {e}")
finally:
    print("Se cierra el archivo")
    archivo.close()
""" 
#leer el archivo ya existente
"""
try:
    archivo=open('Manejo de archivos\Primera actividad\ll.txt', "r", encoding="UTF-8")
    #leer solo por caracteres se da como parametro el numero del caracter
    #print (archivo.read(3))
    #leer lineas completas 
    #print (archivo.readline())
    #iterar las lines para hallar solo un valor o un caracter
    """ for i in archivo:
        print (i) """
    #acceder solo a una linea de la lista
    #print (archivo.readlines()[0])
    #anexar informacion al archivo
    """ archivo2=open('Manejo de archivos\Primera actividad\copia.txt', 'a')
    archivo2.write(archivo.read()) """
except  Exception as e:
    print(f"Error:_{e}")
finally:
    print("Se cierra el archivo")
    archivo.close()
    #archivo2.close()