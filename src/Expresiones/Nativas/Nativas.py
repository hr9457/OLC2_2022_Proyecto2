from src.Interfaces.Instruccion import Instruccion
from src.Interfaces.TipoNativas import TipoNativas
from src.Expresiones.Primitivo import Primitivo
from src.Interfaces.TipoExpresion import TipoExpresion
import math




from src.environment.Simbolo3d import Simbolo3d




class Nativas(Instruccion):

    def __init__(self, fila, columna, nodo, tipo):
        self.fila = fila
        self.columna = columna
        self.nodo = nodo
        self.tipo = tipo
        


    def ejecutar(self, entorno):
        
        # retonro de un primitivo
        result = self.nodo.ejecutar(entorno)


        # comprobacion si es una variable
        if result.tipo == TipoExpresion.ID:
            result = entorno.getVariable(result.valor)
            



        # verficacionde los tipos 
        if self.tipo == TipoNativas.TOSTRING:
            return Primitivo(
                self.fila,
                self.columna,
                TipoExpresion.STRING,
                result.valor
            )



        elif self.tipo == TipoNativas.ABS:

            if result.tipo == TipoExpresion.INTEGER or result.tipo == TipoExpresion.FLOAT:
                return Primitivo(
                    self.fila,
                    self.columna,
                    result.tipo,
                    abs(result.valor)
                )
            else:
                print('NATIVAS --> eror conversion abs')
                return None



        elif self.tipo == TipoNativas.SQRT:

            if result.tipo == TipoExpresion.FLOAT:
                print(math.sqrt(float(result.valor)))
                return Primitivo(
                    self.fila,
                    self.columna,
                    result.tipo,
                    math.sqrt(float(result.valor))
                )
            
            else:
                print('NATIVAS --> eror conversion sqrt')
                return None

        


        elif self.tipo == TipoNativas.CLONE:

            return Primitivo(
                self.fila,
                self.columna,
                result.tipo,
                result.valor
            )











    # -------------------------------------------------------------------------
    #                   TRADUCCION DE LA PIRNTLN A 3D
    # -------------------------------------------------------------------------
    def traducir(self, entorno, traductor3d, cadena):
        # traduccion a 3d
        cadenaTraduccion3d = ''


        nodo3d = self.nodo.traducir(entorno, traductor3d, cadena)



        if nodo3d.tipo == TipoExpresion.ID:
            nodo3d = entorno.getVariable3d(nodo3d.valor)


        if self.tipo == TipoNativas.TOSTRING:
            
            
            print('paro en tostring')
            return Simbolo3d(
                self.fila,
                self.columna,
                None,
                TipoExpresion.STRING,
                nodo3d.valor,
                None,
                0,
                0
            )



        # traduccion para la nativa abs
        elif self.tipo == TipoNativas.ABS:
            cadenaTraduccion3d += '\n'
            cadenaTraduccion3d += '\n'
            cadenaTraduccion3d += '\n'
            cadenaTraduccion3d += '/*-- NATIVA ABS() --*/\n'
            cadenaTraduccion3d += f'{nodo3d.valor} = {nodo3d.valor} * -1;\n\n'

            # agregacion de traduccion
            traductor3d.addCadenaTemporal(cadenaTraduccion3d)

            
            return Simbolo3d(
                self.fila,
                self.columna,
                None,
                nodo3d.tipo,
                nodo3d.valor,
                None,
                0,
                0
            )




        return -1