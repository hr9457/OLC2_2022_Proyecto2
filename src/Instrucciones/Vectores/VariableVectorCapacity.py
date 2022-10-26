from src.Interfaces.Instruccion import Instruccion
from src.Interfaces.TipoExpresion import TipoExpresion
from src.environment.Simbolo import Simbolo
from src.Interfaces.TipoMutable import TipoMutable


from src.environment.vector3d import Vector3d


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


    # -------------------------------------------------------------------------
    #                   TRADUCCION DE LA PIRNTLN A 3D
    # -------------------------------------------------------------------------
    def traducir(self, entorno, traductor3d, cadena):

        cadena3d = ''

        posicion_stack = traductor3d.getStack()
        traductor3d.aumentarStack()

        posicion_heap = traductor3d.getHeap()
        traductor3d.aumentarHeap()

        capacidad = self.varCapacity.traducir(entorno, traductor3d, cadena)
        print(capacidad.valor)

        vector = Vector3d(
            self.fila,
            self.columna,
            self.identificador,
            TipoExpresion.VECTOR,
            0,
            None,
            posicion_stack
            )

        entorno.addVariable3d(self.identificador, vector)


        cadena3d += f'\n'
        cadena3d += f'\n'
        cadena3d += f'/*----  DECLARARCION DE UN VECTOR ----*/\n'
        cadena3d += f'stack[(int) {posicion_stack}] = H;\n'
        cadena3d += f'heap[(int) {posicion_heap}] = 0;\n'
        cadena3d += f'\n'
        traductor3d.addCadenaTemporal(cadena3d)

        return None