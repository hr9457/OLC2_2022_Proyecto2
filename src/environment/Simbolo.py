from src.Interfaces.TipoExpresion import TipoExpresion



from src.environment.Simbolo3d import Simbolo3d



class Simbolo:

    
    def __init__(self, fila, columna, identificador, tipo, valor, mutabilidad):
        self.fila = fila
        self.columna = columna
        self.identificador = identificador
        self.tipo = tipo
        self.valor = valor 
        self.mutabilidad = mutabilidad 




    def ejecutar(self,entorno):
        return Simbolo(
            self.fila,
            self.columna,
            self.identificador,
            self.tipo,
            self.valor,
            self.mutabilidad
        )




    # para traduccion en 3d
    def traducir(self, entorno, traductor3d):
        return Simbolo3d(
            self.fila,
            self.columna,
            self.identificador,
            self.tipo,
            self.valor,
            self.mutabilidad,
            0,
            0
        )