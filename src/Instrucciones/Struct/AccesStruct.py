from src.Interfaces.Instruccion import Instruccion
from src.Interfaces.TipoExpresion import TipoExpresion


class AccesStruct(Instruccion):


    def __init__(self, identificador):
        self.identificador = identificador
        self.tipo = TipoExpresion.STRUCT
        



    def ejecutar(self,entorno):
        return self