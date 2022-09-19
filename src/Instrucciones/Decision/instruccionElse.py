from src.Interfaces.Expresion import Expresion
from src.Expresiones.Primitivo import Primitivo
from src.Interfaces.TipoExpresion import TipoExpresion

class InstruccionElse(Expresion):


    # constructor
    def __init__(self, fila, columna,instrucciones=None):
        self.fila = fila
        self.columna = columna
        self.instrucciones = instrucciones
        self.resultadoElse = ''
        # self.tablaErrores = tablaErrores
        


    # ejecucion del else 
    def ejecutar(self, entorno):

        for instruccion in self.instrucciones:
            
            result = instruccion.ejecutar(entorno)
            print(f'ELSE --> {result}')

            if isinstance(result, Primitivo) and result.tipo == TipoExpresion.BREAK:
                if result is not None and result.valor is not None:
                    self.resultadoElse += result.valor
                retorno = Primitivo(None, None, TipoExpresion.BREAK, self.resultadoElse )
                return retorno

            elif isinstance(result, Primitivo) and result.tipo == TipoExpresion.CONTINUE:
                if result is not None and result.valor is not None:
                    self.resultadoElse += result.valor
                retorno = Primitivo(None, None, TipoExpresion.CONTINUE, self.resultadoElse)
                return retorno

            elif isinstance(result, Primitivo) and result.tipo == TipoExpresion.RETURN:
                result = result.ejecutar(entorno)
                retorno = Primitivo(
                    None, 
                    None, 
                    TipoExpresion.RETURN, 
                    result.valor
                    )
                return retorno
            
            if result != None:
                self.resultadoElse += result


        return self.resultadoElse












    def traducir(self, entorno, traductor3d, cadena):
        
        for instruccion in self.instrucciones:
            instruccion.traducir(entorno, traductor3d, cadena)

        return None

