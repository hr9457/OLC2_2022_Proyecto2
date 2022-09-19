from src.Interfaces.Instruccion import Instruccion
from src.Interfaces.TipoExpresion import TipoExpresion


class PushExp(Instruccion):

    def __init__(self, variable, expression):
        self.variable = variable
        self.expression = expression



    def ejecutar(self, entorno):
    

        print('')
        vector = entorno.getVariable(self.variable)


        nuevoValor = self.expression.ejecutar(entorno)

        if nuevoValor.tipo == TipoExpresion.ID:
            nuevoValor = entorno.getVariable(nuevoValor.valor)

        vector.lista.append(nuevoValor)

        return None