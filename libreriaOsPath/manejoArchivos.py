import os
from pathlib import Path, PurePath
from typing import Pattern

#1. nombre de la ruta en la que se trabaja
#print(os.getcwd())
#rint(Path.cwd())
#2. listar las carpetas o archivos dentro de la carpeta
#print(os.listdir())
#print(list(Path().iterdir()))
#print(list(Path("mi base de datos").iterdir()))
#3. crear carpetas
#os.mkdir("pruebaOS")
#Path("pruebaOS").mkdir()
#4. crear carpetas dentro de carpetas
#os.mkdirs(os.path.join("primera", "dentroPrimera"))
#PurePath.joinpath(Path.cwd(), "primera", "dentroPrimera").mkdir(parents=True)
#5. renombrar
#os.rename("carpeta", "nombreCambiado")
""" PathActual=Path("nombre")
PathObjetivo=Path("nombreCamio")
Path.rename(PathActual, PathObjetivo) """