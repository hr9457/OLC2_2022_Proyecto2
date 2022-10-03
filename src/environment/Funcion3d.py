from src.environment.Simbolo3d import Simbolo3d


class Funcion3d:


    def __init__(self, fila, columna, identificador, listaParametros, instrucciones, tipo, inicioStack):
        self.fila = fila
        self.columna = columna
        self.identificador = identificador
        self.listaParametros = listaParametros
        self.instrucciones = instrucciones
        self.tipo = tipo
        self.inicioStack = inicioStack
        self.cantidadParametros = 0
        self.respuesta = None



    def traducir(self, entorno, traductor3d, cadena):
        return self