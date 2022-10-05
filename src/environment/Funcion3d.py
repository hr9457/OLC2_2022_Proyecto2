from src.environment.Simbolo3d import Simbolo3d


class Funcion3d:


    def __init__(self, fila, columna, identificador, listaParametros, instrucciones, tipo, cantidadParametros):
        self.fila = fila
        self.columna = columna
        self.identificador = identificador
        self.listaParametros = listaParametros
        self.instrucciones = instrucciones
        self.tipo = tipo
        self.cantidadParametros = cantidadParametros
        self.posicion_relativa = 0



    def traducir(self, entorno, traductor3d, cadena):
        return self