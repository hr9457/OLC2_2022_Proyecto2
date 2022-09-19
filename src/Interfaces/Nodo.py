from abc import ABC, abstractmethod

class Nodo(ABC):

    def __init__(self, token):
        self.tipo = token.type
        self.nombre = token.type
        self.valor = token.value
        self.hojas = []

    # abstractclassmethod para todas la clases hijas
    @abstractmethod
    def ejecutar(self):
        pass