from src.Interfaces.Instruccion import Instruccion

from src.Interfaces.TipoExpresion import TipoExpresion

from src.Instrucciones.Vectores.VariableVector import VariableVector
from src.Interfaces.TipoMutable import TipoMutable

from src.environment.Simbolo import Simbolo


class VectorDefault(Instruccion):


    def __init__(self, expDefault, cantidad):
        self.expDefault = expDefault
        self.cantidad = cantidad



    def ejecutar(self, entorno):


        # creacion de una variable vector
        listaExpresiones = []


        cantidadExpresions = self.cantidad.ejecutar(entorno)


        for elemento in range(cantidadExpresions.valor):
            listaExpresiones.append(Simbolo(0,0,'',TipoExpresion.INTEGER,self.expDefault.valor,TipoMutable.MUTABLE))


        variableVector = VariableVector(
            0,
            0,
            '',
            TipoExpresion.INTEGER,
            TipoMutable.MUTABLE
        )

        variableVector.lista = listaExpresiones

        return variableVector