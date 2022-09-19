from Modelo import BaseDatos
from Vista import Vista
class Coordinator(object):
    def __init__(self, vista, modelo):
        self.__mi_vista=vista
        self.__mi_modelo=modelo

    def validarIngreso(self,id):
        pass
    
def main():
    
    modelo = BaseDatos()
    #modelo.setName("Dan") 
    modelo.get_name()
    print(modelo.get_name())   
if __name__ == "__main__":
    main()