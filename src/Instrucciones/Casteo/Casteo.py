from src.Interfaces.Instruccion import Instruccion
from src.Interfaces.TipoExpresion import TipoExpresion
from src.environment.Simbolo import Simbolo
from src.Expresiones.Primitivo import Primitivo
from src.Error.Error import Error


class Casteo(Instruccion):


    def __init__(self,fila, columna, expresion, tipo):
        self.fila = fila
        self.columna = columna
        self.expresion = expresion
        self.tipo = tipo




    def ejecutar(self,entorno):

        # ejecucion del nodo para subir sus valores
        nodoIzquierdo = self.expresion.ejecutar(entorno)

        # print(f'CASTEO {nodoIzquierdo.tipo}')
        # print(f'CASTEO {self.tipo}')


        print(f'CASTEO: {nodoIzquierdo.tipo}')

        if nodoIzquierdo.tipo == TipoExpresion.ID:
            print('es un identificador')
            print(nodoIzquierdo.valor)
            nodoIzquierdo = entorno.getVariable(nodoIzquierdo.valor)


        # caso de casteo para tipos integer
        if nodoIzquierdo.tipo == TipoExpresion.INTEGER:
            

            # solo con los tipo que se puede castear
            if self.tipo == TipoExpresion.INTEGER:
                return Primitivo(
                    self.fila,
                    self.columna,
                    TipoExpresion.INTEGER,
                    nodoIzquierdo.valor
                )


            elif self.tipo == TipoExpresion.FLOAT:
                return Primitivo(
                    self.fila,
                    self.columna,
                    TipoExpresion.FLOAT,
                    int(nodoIzquierdo.valor)
                )

            else:
                return Error('CASTEO: Error de casteo')


        # caso de casteo para tipos float
        elif nodoIzquierdo.tipo == TipoExpresion.FLOAT:
            
            # solo con los tipo que se puede castear
            if self.tipo == TipoExpresion.INTEGER:
                return Primitivo(
                    self.fila,
                    self.columna,
                    TipoExpresion.INTEGER,
                    int(nodoIzquierdo.valor)
                )


            elif self.tipo == TipoExpresion.FLOAT:
                return Primitivo(
                    self.fila,
                    self.columna,
                    TipoExpresion.FLOAT,
                    nodoIzquierdo.valor
                )

            else:
                return Error('CASTEO: Error de casteo')




        # caso para casteo de tipo char
        elif nodoIzquierdo.tipo == TipoExpresion.CHAR:


            # solo con los tipo que se puede castear
            if self.tipo == TipoExpresion.INTEGER:
                return Primitivo(
                    self.fila,
                    self.columna,
                    TipoExpresion.INTEGER,
                    ord(nodoIzquierdo.valor)
                )

            else:
                return Error('CASTEO: Error de casteo')






        else:
            return Error('CASTEO: Error de casteo')
    










    # -------------------------------------------------------------------------
    #                   TRADUCCION DE LA PIRNTLN A 3D
    # -------------------------------------------------------------------------
    def traducir(self, entorno, traductor3d, cadena):

        expresion3d = self.expresion.traducir(entorno, traductor3d, cadena)



        if expresion3d.tipo == TipoExpresion.ID:
            expresion3d = entorno.getVariable3d(expresion3d.valor)


        


        pass