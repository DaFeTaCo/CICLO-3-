# BD SQL desde  Python
class BaseDatos():
    def __init__(self):
        self.__name = "cien años de soledad"
        self.__login=''
        self.__password=''

    def setLogin(self,l):
        self.__login=l
    
    def setName(self,n):
        self.__name=n

    def setPassword(self,p):
        self.__password=p

    def get_name(self):
        return self.__name
    def validaruser(self,id):
        pass