from src.Interfaces.Expresion import Expresion
from src.Expresiones.Primitivo import Primitivo
from src.Interfaces.TipoExpresion import TipoExpresion


class Capacity(Expresion):

    def __init__(self, variable):
        self.variable = variable



    def ejecutar(self, entorno):


        print('CAPACITY VECTORES')


        vector = entorno.getVariable(self.variable)

        primate = Primitivo(
            0,
            0,
            TipoExpresion.INTEGER,
            vector.capacity
        )


        return primate