from src.Interfaces.Instruccion import Instruccion
from src.Interfaces.TipoMutable import TipoMutable



class Push(Instruccion):

    def __init__(self, fila, columna, identificador, exp):
        self.fila = fila
        self.columna = columna
        self.identificador = identificador
        self.exp = exp



    def ejecutar(self, entorno):
        
        print('*********** PUSH A UN VECTOR *************')


        # buscar la existencia de la variable en los entornos
        vector = entorno.getVariable(self.identificador)


        # revison de la mutabilidad del vector
        if vector.mutabilidad == TipoMutable.MUTABLE:
            # pueden puede hacer push al vector
            print('vector mutable')
            vector.lista.append(self.exp)




        elif vector.mutabilidad == TipoMutable.NOMUTABLE:
            # no se puede hacer push al vector
            print('vector no mutable')




        print('paro')


        
        return None