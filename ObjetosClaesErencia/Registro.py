""" 
#Clase en la cual se unen las demas clase en Persona
#Las clase se deben importar
"""
#se importa la clase Persona
from Persona import Persona as miPersona
#importar la clase Trabajo
from Trabajo import Trabajo as miTrabajo
#importar la calse Salario
from Salario import Salario as miSalario
#importar la clase Subsidio
from Subsidio import Subsidio as miSubsidio
""" 
#declarar la clase y sus metodos
"""
class Registro:
    """ 
    #se inicializn las listas de la clase
    """
    #lista que contiene los trabajos de las personas
    listaTrabajos=["Docente"]
    #lista que contiene los salarios de las personas
    listaSalarios=[100]
    #lista que contiene los subsidios de las personas
    listaSubsidios=["Contributivo"]
    """ 
    #metodo para recorrer la lista de trabajos y encontrar el que se busca
    #la lista de trabajos ya esta inicializada
    #retornar el trabajo
    #si el trabajo no esta en la lista se lo debe agregar
    """
    def darTrabajo(self, nTrabajo):
        mio=None
        miLista=self.listaTrabajos
        cont=0
        for i in miLista:
            if miLista[cont]==nTrabajo:
                mio=nTrabajo
                miTrabajo(mio).setTrabajo(mio)
                print(f"EL trabajo es:_ {miLista[cont]}")
                cont+=1
            else:
                print("El trabajo no se encuentra registrado se procedera a registrarlo")
                miLista.append(nTrabajo)
                mio=nTrabajo
                miTrabajo(mio).setTrabajo(mio)
            break
        return mio
    """ 
    #Metodo para recorrer la lista de salarios y encontrar el que se busca
    #la lista de salarios ya esta inicializada
    #retornar el salario
    #si el salario no esta en la lista se lo debe agregar
    """
    def darSalario(self, nSalario):
        miPago=None
        miLista=self.listaSalarios
        cont=0
        for i in miLista:
            if miLista[cont]==nSalario:
                miPago=nSalario
                miSalario(miPago).setSalarios(miPago)
                print(f"EL salario es:_ {miLista[cont]}")
                cont+=1
            else:
                print("El salario no se encuentra registrado se procedera a registrarlo")
                miLista.append(nSalario)
                miPago=nSalario
                miSalario(miPago).setSalarios(miPago)
            break
        return miPago
    """ 
    #metodo que recorre la lista de subsidios y encuentra el que se busca
    #la lista de subsidios ya esta incializada
    #retorna el subsidio al que pertenece
    #si el subsidio no se encuentra en la lista se lo debe agregar
    """
    def darSubsidio(self, nSubsidio):
        miSeguro=None
        miLista=self.listaSubsidios
        cont=0
        for i in miLista:
            if miLista[cont]==nSubsidio:
                miSeguro=nSubsidio
                miSubsidio(miSeguro).setTipos(miSeguro)
                print(f"EL Subsidio es:_ {miLista[cont]}")
                cont+=1
            else:
                print("El Subsidio no se encuentra registrado se procedera a registrarlo")
                miLista.append(nSubsidio)
                miSeguro=nSubsidio
                miSubsidio(miSeguro).setTipos(miSeguro)
            break
        return miSeguro
    """
    #se decalara la funcion para crear una persona dada la informacion
    #la lista de trabajos ya esta inicializada
    #la lista de salarios ya esta inicializada
    #la lista de subsidios ya esta inicializada
    #nIdentificacion, es la identificacion de la persona a registrar. nIdentificacion > 0 && nIdentificacion != null
    #nNombre, es el nombre de la persona a registrar. nNombre != "" && nNombre != null
    #nEdad, es la edad de la persona a registrar. nEdad > 0 && nEdad != null
    #nTrabajo, es la profesion de la persona a registrar. nTrabajo != "" && nTrabajo != null
    #nSalario, es el pago por el trabajo a realizar. nSalario > 0 && nSalario != null
    #nSubsidio, es el tipo de subsidio que la persona posee. nSubsidio != "" nSubsidio != null
    #Debe retornar un mensaje conformando que la persona se registro con exito
    #Capturar las excepciones que se puedan generar
    """
    def registrarPersona(self,nIdentificacion, nNombre, nEdad, nTrabajo, nSalario, nSubsidio):
        if nIdentificacion==0 or nNombre=="" or nEdad==0 or nTrabajo=="" or nSalario==0 or nSubsidio=="":
            print(f''' Los siguientes valores deben tener un dato si el dato es 0 o None realice el registro nuevamente 
                  Identificaicon:_ {nIdentificacion}
                  Nombre:_ {nNombre}
                  Edad:_ {nEdad}
                  Profesion:_ {nTrabajo}
                  Salario:_ {nSalario}
                  Subsidio:_ {nSubsidio}
                  ''')
        else:
            miPersona(nIdentificacion, nNombre, nEdad, self.darTrabajo(nTrabajo), self.darSalario(nSalario), self.darSubsidio(nSubsidio))
            #miPersona(nIdentificacion, nNombre, nEdad, nTrabajo, nSalario, nSubsidio)
            print(f''' Se registraron los siguientes valores 
                Identificaicon:_ {nIdentificacion}
                Nombre:_ {nNombre}
                Edad:_ {nEdad}
                Profesion:_ {nTrabajo}
                Salario:_ {nSalario}
                Subsidio:_ {nSubsidio}
                ''')