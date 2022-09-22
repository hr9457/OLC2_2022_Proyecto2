from src.Interfaces.Expresion import Expresion
from src.Interfaces.TipoExpresion import TipoExpresion
from src.Expresiones.Primitivo import Primitivo


from src.environment.Simbolo3d import Simbolo3d


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











    # -------------------------------------------------------------------------
    #                   TRADUCCION DE LA PIRNTLN A 3D
    # -------------------------------------------------------------------------
    def traducir(self, entorno, traductor3d, cadena):



        nodoUnico = self.nodo.traducir(entorno, traductor3d, cadena)


        if nodoUnico.tipo == TipoExpresion.INTEGER:
            nodoUnico.valor = -1 * int(nodoUnico.valor)
            return nodoUnico



        elif nodoUnico.tipo == TipoExpresion.FLOAT:
            nodoUnico.valor = -1.0 * float(nodoUnico.valor)
            return nodoUnico


