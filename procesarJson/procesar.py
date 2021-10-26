""" 
Leer archivos de tipo json desde python
"""
import json
import urllib.request
""" 
variable que se le asigna la url en donde se aloja el archivo json
"""
respuesta=urllib.request.urlopen('http://globalmentoring.com.mx/api/personas.json')
""" 
Mensaje con la información del archivo 
"""
print(respuesta)
""" 
varible con la informacion ordenada del archivo json
"""
cuerpo = respuesta.read()
""" 
Mensaje con la información del archivo json
"""
print(cuerpo)
"""
decodificacion del archivo json
"""
decodificar=json.loads(cuerpo.decode("utf-8"))
""" 
mensaje con la información del archivo decodificada
"""
print(decodificar)