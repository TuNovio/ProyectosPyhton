""" 
Un decorador es una función para extender la funcionalidad 
"""
def funcionDecoradorA(funcionDecoradorB):
    def funcionDecoradoraC():
        funcionDecoradorB()
    return funcionDecoradoraC
     
@funcionDecoradorA
def monstrarMensaje():
    print("Hola desde la funcion mostrar mensaje")
    
monstrarMensaje()
