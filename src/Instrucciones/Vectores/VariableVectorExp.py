from src.Interfaces.Instruccion import Instruccion
from src.Interfaces.TipoExpresion import TipoExpresion


class VariableVectorExp:

    def __init__(self, fila, columna, identificador, tipoVector, mutabilidad, listadoExp):
        self.fila = fila
        self.columna = columna
        self.identificador = identificador
        self.tipoVector = tipoVector
        self.mutabilidad = mutabilidad
        self.listadoExp = listadoExp
        self.lista = []
        self.capacity = 0
        self.tipo = TipoExpresion.VECTOR




    def ejecutar(self, entorno):
        print('GUARANDO VECTORES EN VARIABLES')

        # agregar los elementos a la lista del vector antes de ser agregado como variable
        for elemento in self.listadoExp.listadoExpresiones:

            self.lista.append(elemento)

        # guardado de la variable en el entorno
        entorno.addVariable(self.identificador, self)
        print('VEC![EXP]')

        return None