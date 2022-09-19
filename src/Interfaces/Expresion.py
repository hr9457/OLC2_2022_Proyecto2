from abc import ABC, abstractmethod

class Expresion(ABC):

    def __init__(self):
        pass


    @abstractmethod
    def ejecutar(self, entorno):
        pass

