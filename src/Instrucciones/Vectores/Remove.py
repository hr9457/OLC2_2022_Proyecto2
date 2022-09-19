from src.Interfaces.Instruccion import Instruccion
from src.Expresiones.Primitivo import Primitivo
from src.Interfaces.TipoExpresion import TipoExpresion


class Remove(Instruccion):


    def __init__(self, variable, exp_poisicion):
        self.variable = variable
        self.exp_poisicion = exp_poisicion



    def ejecutar(self, entorno):
        
        print(' REMOVE DE VECTORES ')


        varVector = self.variable.ejecutar(entorno)

        # busqueda de la variable para el remove de un valor
        vector = entorno.getVariable(varVector.valor)


        # posicion en la que se quiere remover un elemento
        # if self.exp_poisicion.tipo == TipoExpresion.ID:
        posicion = self.exp_poisicion.ejecutar(entorno)



        valor_posicion = vector.lista[posicion.valor]


        # remove del la lista del vector
        vector.lista.pop(posicion.valor)


        # entorno.addVariable()

        return Primitivo(
            None,
            None,
            TipoExpresion.RETURN,
            valor_posicion.valor
        )