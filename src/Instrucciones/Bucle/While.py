# from src.Interfaces.Expresion import Expresion
from src.Interfaces.Instruccion import Instruccion
from src.Interfaces.TipoExpresion import TipoExpresion
from src.environment.Environment import Environment
from src.Error.Error import Error
from src.Expresiones.Primitivo import Primitivo





class While(Instruccion):

    def __init__(self, fila, columna, tablaErrores,expresion, nodo=None):
        self.fila = fila
        self.columna = columna
        self.expresion = expresion
        self.nodo = nodo
        self.tablaErrores = tablaErrores


    def ejecutar(self, entorno):
        
        retornoWhile = ''
        
        # ejecucion y evalucacion de la expresion
        exp = self.expresion.ejecutar(entorno)

        # la exp de ejeccutada es una variable
        if exp.tipo == TipoExpresion.ID:
            exp = entorno.getVariable(exp.valor)


        # revision de la expresion sea una expresion tipo bool
        if exp.tipo == TipoExpresion.BOOL:


            # creacion de un nuevo entrono para el while
            numeroEntorno = entorno.numero + 1
            envWhile = Environment('WHILE', numeroEntorno, entorno)


            # el valor sea un valor true
            # mientras sea verdadero
            while exp.valor == 'true' and self.nodo != None:
                
                # ciclo para repetir las instrucciones
                for instruccion in self.nodo:
                    result = instruccion.ejecutar(envWhile)

                    # menejo de instrucciones break y continue
                    if isinstance(result, Primitivo) and result.tipo == TipoExpresion.BREAK:
                        # print(f'WHILE --> {result.valor}')
                        if result.valor is not None: 
                            retornoWhile += result.valor
                        return retornoWhile

                    elif isinstance(result, Primitivo) and result.tipo == TipoExpresion.CONTINUE:
                        if result.valor is not None: 
                            retornoWhile += result.valor
                        break

                    if result != None:
                        retornoWhile += result
                
                # ejecutar una vez mas la expresion
                exp = self.expresion.ejecutar(entorno)
                if exp.tipo == TipoExpresion.ID:
                    exp = entorno.getVariable(exp.valor)
                

            
            # caso contrario
            return retornoWhile


        # la expresion no sea de tipo bool
        else:
            # para reportes
            self.tablaErrores.append(['WHILE: Condicion no es tipo bool',entorno.nombre,self.fila,self.columna])
            # --------------------------------
            return Error('WHILE: Condicion no es tipo bool').ejecutar()