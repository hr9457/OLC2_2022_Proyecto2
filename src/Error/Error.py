from src.Interfaces.Expresion import Expresion

class Error(Expresion):

    def __init__(self, message):
        self.mensaje = message
        self.valor = message


    def ejecutar(self):
        return self.mensaje