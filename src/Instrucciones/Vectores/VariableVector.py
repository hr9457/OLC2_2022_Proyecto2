from src.Interfaces.Instruccion import Instruccion
from src.Interfaces.TipoExpresion import TipoExpresion



class VariableVector:

    def __init__(self, fila, columna, identificador, tipoVector, mutabilidad):
        self.fila = fila
        self.columna = columna
        self.identificador = identificador
        self.tipoVector = tipoVector
        self.mutabilidad = mutabilidad
        self.lista = []
        self.capacity = 0
        self.tipo = TipoExpresion.VECTOR


    def ejecutar(self, entorno):

        print('VECTOR CON WITH CAPACITY')
        # filtro de pregunta por si no existe el struct
        

        # guardado de la variable en el entorno
        entorno.addVariable(self.identificador,self)

        
        return None