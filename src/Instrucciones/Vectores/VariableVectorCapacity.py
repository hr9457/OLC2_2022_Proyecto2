from src.Interfaces.Instruccion import Instruccion
from src.Interfaces.TipoExpresion import TipoExpresion
from src.environment.Simbolo import Simbolo
from src.Interfaces.TipoMutable import TipoMutable


class VariableVectorCapacity:

    def __init__(self, fila, columna, identificador, tipoVector, mutabilidad, varCapacity):
        self.fila = fila
        self.columna = columna
        self.identificador = identificador
        self.tipoVector = tipoVector
        self.mutabilidad = mutabilidad
        self.varCapacity = varCapacity
        self.capacity = 0
        self.lista = []
        self.tipo = TipoExpresion.VECTOR




    def ejecutar(self, entorno):
        print('GUARANDO VECTORES EN VARIABLES')

        # EJECUTAMOS LA EXPRESION PARA SABER LA CAPACIDAD DEL VECTOR
        capacidad = self.varCapacity.ejecutar(entorno)
        self.capacity = capacidad.valor


        # agregar los elementos a la lista del vector antes de ser agregado como variable
        # for elemento in range(capacidad.valor):
        #
        #     self.lista.append(Simbolo(0,0,'',TipoExpresion.INTEGER,0,TipoMutable.MUTABLE))

        entorno.addVariable(self.identificador, self)

        return None



    
    def traducir(self, entorno, traductor3d, cadena):

        

        return None