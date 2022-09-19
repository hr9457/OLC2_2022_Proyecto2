from src.Interfaces.Expresion import Expresion
from src.Interfaces.TipoExpresion import TipoExpresion
from src.Expresiones.Primitivo import Primitivo

class Negativo(Expresion):
    
    def __init__(self, fila, columna, nodo):
        self.fila = fila
        self.columna = columna
        self.nodo = nodo
        self.tipo = None

    def ejecutar(self, entorno):
        
        # primitivo
        nodoUnico = self.nodo.ejecutar(entorno)

        if self.nodo.tipo == TipoExpresion.INTEGER:
            self.tipo = TipoExpresion.INTEGER
            return Primitivo(self.fila, self.columna, TipoExpresion.INTEGER, (-1 * int(nodoUnico.valor)))
            
    
        elif self.nodo.tipo == TipoExpresion.FLOAT:
            self.tipo = TipoExpresion.FLOAT
            return Primitivo(self.fila, self.columna, TipoExpresion.FLOAT, (-1.0 * float(nodoUnico.valor)))    

        else:
            return None