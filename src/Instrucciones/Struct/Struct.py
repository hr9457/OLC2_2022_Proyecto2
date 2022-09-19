from src.Interfaces.Instruccion import Instruccion
from src.environment.Environment import Environment
from src.Interfaces.TipoExpresion import TipoExpresion


class Struct(Instruccion):


    def __init__(self, fila, columna, identificador, elementos, tablaSimbolos):
        self.fila = fila
        self.columna = columna  
        self.identificador = identificador
        self.elementos = elementos
        self.tipo = TipoExpresion.STRUCT
        self.tablaSimbolos = tablaSimbolos



    def ejecutar(self, entorno):
        # agregar modelos de estructuras al entorno actual
        entorno.addStruct(self.identificador, self)


        # para reportes
        self.tablaSimbolos.append([self.identificador,'Struct',self.tipo,entorno.nombre,self.fila,self.columna])
        # -------------


        return None