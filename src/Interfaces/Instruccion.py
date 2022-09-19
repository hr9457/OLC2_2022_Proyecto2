from abc import ABC, abstractmethod


# clase abstrct para instrucciones
class Instruccion(ABC):

    def __init__(self):
        pass


    @abstractmethod
    def ejecutar(self, entorno):
        pass
