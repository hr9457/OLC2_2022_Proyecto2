# importacion de para Expresiones
from src.Interfaces.Expresion import Expresion
from src.Interfaces.TipoExpresion import TipoExpresion

# importaciones para manejar simbolos
from src.environment.Simbolo import Simbolo
from src.environment.Simbolo3d import Simbolo3d

# clse para manejar numero primitivos
class Primitivo(Expresion):

    def __init__(self, fila, columna, tipo, valor):
        self.fila = fila
        self.columna = columna
        self.tipo = tipo
        self.valor = valor


    # metodo abstracto
    def ejecutar(self, entorno):
        return Primitivo(
            self.fila,
            self.columna,
            self.tipo,
            self.valor
            )

    

    # retorno de tipo
    def getTipo(self):
        return self.tipo




    # retorno para traduccion en 3d
    def traducir(self, entorno, traductor3d, cadena):

        if self.tipo == TipoExpresion.STRING:
            return Simbolo3d(
                self.fila,
                self.columna,
                None,
                self.tipo,
                self.valor,
                None,
                0,
                len(self.valor)
            )
        
        else:
            return Simbolo3d(
                self.fila,
                self.columna,
                None,
                self.tipo,
                self.valor,
                None,
                0,
                0
            )



    # retorno para traduccion en 3d
    def optimizar(self, entorno, traductor3d, cadena):

        if self.tipo == TipoExpresion.STRING:
            return Simbolo3d(
                self.fila,
                self.columna,
                None,
                self.tipo,
                self.valor,
                None,
                0,
                len(self.valor)
            )
        
        else:
            return Simbolo3d(
                self.fila,
                self.columna,
                None,
                self.tipo,
                self.valor,
                None,
                0,
                0
            )