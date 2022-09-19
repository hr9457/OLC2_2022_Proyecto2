from src.Interfaces.TipoExpresion import TipoExpresion


class SimboloStruct:

    def __init__(self, identificador, primate):
        self.identificador = identificador 
        self.primate = primate


    def ejecutar(self, entorno):
        return self