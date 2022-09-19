from src.Interfaces.TipoExpresion import TipoExpresion
from src.Interfaces.TipoMutable import TipoMutable	


class PrimateStruct:

    # lista de elementos y tipo 
    def __init__(self, elementos, mutabilidad=None):
        self.elementos = elementos
        self.tipo = TipoExpresion.STRUCT
        self.mutabilidad = mutabilidad



    def ejecutar(self, entorno):
        return self



        