from src.Interfaces.TipoExpresion import TipoExpresion


class Simbolo3d:

    
    def __init__(self, fila, columna, identificador, tipo, valor, mutabilidad, posicion, tamanio):
        self.fila = fila
        self.columna = columna
        self.identificador = identificador
        self.tipo = tipo
        self.valor = valor 
        self.mutabilidad = mutabilidad
        self.posicion = posicion 
        self.tamanio = tamanio




    def ejecutar(self,entorno):
        return self