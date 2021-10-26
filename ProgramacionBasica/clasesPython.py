""" clases y obtjetos en python  """
#declaracion de la clase para realizar las operaciones basicas matematicas(+-*/)
#ejemplo
""" en python hay atributos de clase y atributos de instancia o del metodo """
class personaAdulta:
    """ no hay atributos de clase """
    """ constructor de la calse """
    #metodo de tipo dunder o doble guion bajo
    #argumentos o parametros para python
    def __init__(self, nIdentificacion, nNombre, nEdad, nPeso):
        """ atributos de instancia""" 
        #identificacion de la persona
        self.identificacion=nIdentificacion
        #nombre de la persona
        self.nombre=nNombre
        #edad de la persona
        self.edad=nEdad
        #peso de la persona
        self.peso=nPeso
    def mostrarDetalle(self, nIdentificacion):
        if self.identificacion==id:
            print(f'''
                  Nombre:_ {self.nombre}
                  Edad:_ {self.edad}
                  Peso:_ {self.peso}''')
""" construccion de otro objeto o metodo """
persona1=personaAdulta(11, "alfonso", 21, 80)
persona2=personaAdulta(12, "Sebastian", 23, 90)
print(F'''
      Nombre persona 1:_{persona1.nombre}
      Nombre persona 2:_ {persona2.nombre}''')
""" buscar persona por identificacion pero del objeto 1"""
id=int(input("Ingrese el valor de la identificacion del usario a buscar:_"))
persona1.mostrarDetalle(id)