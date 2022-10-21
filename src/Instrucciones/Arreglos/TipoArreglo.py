from src.Interfaces.Expresion import Expresion
from src.Interfaces.TipoExpresion import TipoExpresion


class TipoArreglo(Expresion):

    def __init__(self, fila, columna, tipo, exp):
        self.fila = fila
        self.columna = columna
        self.tipo = TipoExpresion.ARREGLO
        self.tipoArreglo = tipo
        self.exp = exp
        self.mutabilidad = None
        self.tamanioMaxArreglo = None
        self.tipoExpArreglo = None



    def ejecutar(self, entorno):

        valueExp = self.exp.ejecutar(entorno)
        self.tamanioMaxArreglo = valueExp.valor
        self.tipoExpArreglo = valueExp.tipo
        return self





    def optimizar(self, entorno):

        valueExp = self.exp.optimizar(entorno)
        self.tamanioMaxArreglo = valueExp.valor
        self.tipoExpArreglo = valueExp.tipo
        return self