from src.Interfaces.Instruccion import Instruccion
from src.environment.Environment import Environment
from src.Expresiones.Primitivo import Primitivo
from src.Interfaces.TipoExpresion import TipoExpresion


class Loop(Instruccion):

    def __init__(self, fila, columna, nodo):
        self.fila = fila
        self.columna = columna
        self.nodo = nodo
        self.resultadoWhile = ''


    def ejecutar(self, entorno):
        

        if self.nodo != None:

            numeroEntorno = entorno.numero + 1
            envWhile = Environment('WHILE', numeroEntorno, entorno)


            while True:
                for instruccion in self.nodo:
                    result = instruccion.ejecutar(envWhile)


                    # si viene una instruccion break
                    if isinstance(result,Primitivo) and result.tipo == TipoExpresion.BREAK:
                        return self.resultadoWhile


                    # si viene una instruccion continue
                    elif isinstance(result, Primitivo) and result.tipo == TipoExpresion.CONTINUE:
                        break


                    # concatenacion
                    if result != None:
                        self.resultadoWhile += result


        else:
            return ''
