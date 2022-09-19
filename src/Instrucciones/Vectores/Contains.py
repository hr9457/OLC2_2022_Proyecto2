from src.Interfaces.Expresion import Expresion
from src.Expresiones.Primitivo import Primitivo
from src.Interfaces.TipoExpresion import TipoExpresion

class Contains(Expresion):


    def __init__(self, variable, expresion):
        self.variable = variable
        self.expresion = expresion


    def ejecutar(self, entorno):
        
        print('EJEUCION CONTAINS EN VECTOR/ LISTA')

        variable_busqueda = self.variable.ejecutar(entorno)

        vector = entorno.getVariable(variable_busqueda.valor)

        expresion_comparacion = self.expresion.ejecutar(entorno)

        if self.expresion.tipo == TipoExpresion.ID:
            expresion_comparacion = entorno.getVariable(self.expresion.valor)

        for elemento in vector.lista:

            elemento_valor = elemento.ejecutar(entorno)

            if elemento_valor.valor == expresion_comparacion.valor:
                return Primitivo(0,0,TipoExpresion.BOOL,'true')

        return Primitivo(0,0,TipoExpresion.BOOL,'false')