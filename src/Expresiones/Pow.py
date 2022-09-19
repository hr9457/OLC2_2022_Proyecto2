from src.Interfaces.Expresion import Expresion
from src.Expresiones.Primitivo import Primitivo
from src.Interfaces.TipoExpresion import TipoExpresion
import math


class Pow(Expresion):

    def __init__(self, fila, columna, tipo, nodoBase, nodoExponente):
        self.fila = fila
        self.columan = columna
        self.tipo = tipo
        self.nodoBase = nodoBase
        self.nodoExponente = nodoExponente



    def ejecutar(self, entorno):
        
        # ejecucion de los nodos
        base = self.nodoBase.ejecutar(entorno)
        exponente = self.nodoExponente.ejecutar(entorno)


        if self.tipo == TipoExpresion.INTEGER:
            potencia = math.pow(base.valor, exponente.valor)
            return Primitivo(self.fila, self.columan, TipoExpresion.INTEGER, int(potencia))
        

        elif self.tipo == TipoExpresion.FLOAT:
            potencia = math.pow(base.valor, exponente.valor)
            return Primitivo(self.fila, self.columan, TipoExpresion.FLOAT, potencia)



        else: 
            return None




