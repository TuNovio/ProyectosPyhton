""" 
importar los archivos para la interfaz
Importar las clase de usuario y usuarioDAO
"""
#usuario
from Usuario import Usuario
#operaciones SQL
from UsuarioDAO import UsuarioDAO
""" 
contiene 5 opciones que representan la eleccion del usuario
1) Listar usuario 
2) Agregar usuario 
3) Actualizar información del usuario
4) Eliminar usuario
5) Salir de la aplicacion
"""
def menu():
    return f'''
Elije una opción segun la actividad que desees desarrollar
Seleccione la opción 1 si quiere buscar a un usuario
Selecciona la opción 2 si quiere visualizar la lista de usuarios
Selecione la opción 3 si desea registrar un nuevo usuario
Selecione la opción 4 si desea actualizar la información del usuario
Selecione la opción 5 si desea eliminar el usuario
Selecione la opción 6 si desea abandonar la aplicación
'''
""" 
Metodo que permite visualizar a todos los usuarios de la base de datos
la base de datos ya se encuentra inicializada
retorna una lista con los usuarios
"""
def listarUsuarios():
    misUsuarios=UsuarioDAO.consultarTodo()
    for miU in misUsuarios:
        print(miU)
""" 
Metodo que permite buscar un usuario en la base de datos
la base de datos se encuentra inicializada
retorna los usuarios
"""
def buscar(nIdentificacion):
    miUsuario=UsuarioDAO.consultarUsuario(nIdentificacion)
    if miUsuario != None:
        print(miUsuario)
    else:
        print ('No existe el usuario en la base de datos ')
""" 
Metodo que permite registrar un usuario en la base de datos
la base de datos se encuentra inicailizada 
se debe validar que el usuario no exista en la base de datos. si existe se debe enviar un mensaje
retorna un mensaje de validacion 
"""
def registrar(nIdentificacion, nNombre, nContraseña):
    miUsuario=Usuario(nIdentificacion, nNombre, nContraseña)
    if buscar(nIdentificacion) is None:
        UsuarioDAO.registrarUsuario(miUsuario)
        print ('Se registro el usario')
    else:
        print("El usuario ya se encuentra en la lista de usuarios")
""" 
Metodo que permite cambiar el valor de la informacion del usuario
la base de datos ya se encuentra inicializada
se debe validar que el usuario exista. si el usuario no existe se debe enviar un mensaje
retorna un mensaje de validacion
"""
def actualizar(nIdentificacion, nNombre, nContraseña):
    miUsuario=Usuario(nIdentificacion, nNombre, nContraseña)
    if buscar(nIdentificacion)!=None:
        UsuarioDAO.cambiarDatos(miUsuario)
        print('Se actualizo la informacion del usuario')
    else:
        print("El usuario no existe en la base de datos")
""" 
metodo que permite eliminar al usuario de la base de datos
la base de datos ya se encuentra inicializada
se debe validar si el usuario existe en la base de datos. si el usuario no existe se debe enviar un mensaje
retorna un mensaje de confirmacion
"""
def eliminar(nIdentificacion):
    if buscar(nIdentificacion)!=None:
        UsuarioDAO.eliminarUsuario(nIdentificacion)
        print('Se elimino el usuario de la base de datos')
    else:
        print("El usuario no existe en la base de datos")
"""
menu del usuario para interactuar con la base de datos
la base de datos se encuentra inicializada 
los metodos que interactuan con la base de datos se encuentran inicializados
opcion, es la opcion que el usuario ingresa. opcion > 0 && opcion != NaN
las obciones son de buscar usuario por el identificador, dar una lista de usuarios, registrar un usuario
actualizar la información del usuario en la base de datos, eliminar un usuario de la base de datos
"""
opcion=None
while  opcion != 6:
    try:  
        print(menu())
        opcion=int(input("Ingresa la opción:_"))
        if opcion==1:
            identificador=int(input("Ingresa la identificacion del usuario a buscar:_"))
            buscar(identificador)
        elif opcion==2:
            print(Usuario.getNombre.__doc__)
            listarUsuarios()
        elif opcion==3:
            identificador=int(input("Ingresa la identificacion del usuario:_"))
            nombre=input("Ingresa el nombre del usuario:_")
            contraseña=int(input("Ingrese la contraseña:_"))
            registrar(identificador, nombre, contraseña)
        elif  opcion==4:
            identificador=int(input("Ingresa la identificacion del usuario:_"))
            nombre=input("Ingresa el nombre del usuario:_")
            contraseña=int(input("Ingrese la contraseña:_"))
            actualizar(identificador, nombre, contraseña)
        elif opcion==5:
            identificador=int(input("Ingresa la identificacion del usuario a buscar:_"))
            eliminar(identificador)
    except Exception as e:
        print(f"Error:_{e}")
    finally:
        opcion=None
else:
    print("Gracias por utilizar nuestro programa")
