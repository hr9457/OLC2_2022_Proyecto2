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


        # traduccion del nodo al cual se le va aplicar una nativa
        nodo3d = self.nodo.traducir(entorno, traductor3d, cadena)



        

        # NATIVA TOSTRING
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





        # NATIVA ABS
        # traduccion para la nativa abs
        elif self.tipo == TipoNativas.ABS:


            # si la funcion nativa se le va aplicar a una variable
            if nodo3d.tipo == TipoExpresion.ID:

                # contador del simbolo -
                valor_negativo = nodo3d.valor.count('-')

                nodo3d = entorno.getVariable3d(nodo3d.valor)



                # traduccion si esta en una variable
                cadenaTraduccion3d += '\n'
                cadenaTraduccion3d += '\n'
                cadenaTraduccion3d += '\n'
                cadenaTraduccion3d += '/*-- NATIVA ABS() --*/\n'

                
                
                # hago uso de un temporal para la variable
                temporalActual = traductor3d.getTemporal()
                traductor3d.aumentarTemporal()



                cadenaTraduccion3d += f't{temporalActual} = {nodo3d.valor};\n'



                # saber si un numero es negativo
                etiqueta_actual = traductor3d.getEtiqueta()
                traductor3d.aumentarEtiqueta()


                etiqueta_salida = traductor3d.getEtiqueta()
                traductor3d.aumentarEtiqueta()


                # if condicional para saber si el valor es negativo
                cadenaTraduccion3d += f'if (t{temporalActual} < 0) goto L{etiqueta_actual};\n'
                cadenaTraduccion3d += f'goto L{etiqueta_salida};\n'
                
                # si es un valor menor que 0 multiplica por -1
                cadenaTraduccion3d += f'L{etiqueta_actual}:\n'
                cadenaTraduccion3d += f't{temporalActual} = t{temporalActual} * -1;\n\n'


                # si no es un valor menor a 0 se queda igual
                cadenaTraduccion3d += f'L{etiqueta_salida}:\n'


                # agregacion de la traduccion
                traductor3d.addCadenaTemporal(cadenaTraduccion3d)
                return Simbolo3d(
                    self.fila,
                    self.columna,
                    None,
                    nodo3d.tipo,
                    f't{temporalActual}',
                    None,
                    0,
                    0
                )

                




            else:
                cadenaTraduccion3d += '\n'
                cadenaTraduccion3d += '\n'
                cadenaTraduccion3d += '\n'
                cadenaTraduccion3d += '/*-- NATIVA ABS() --*/\n'



                # saber si un numero es negativo
                etiqueta_actual = traductor3d.getEtiqueta()
                traductor3d.aumentarEtiqueta()


                etiqueta_salida = traductor3d.getEtiqueta()
                traductor3d.aumentarEtiqueta()



                # if condicional para saber si el valor es negativo
                cadenaTraduccion3d += f'if (t{nodo3d.valor} < 0) goto L{etiqueta_actual};\n'
                cadenaTraduccion3d += f'goto L{etiqueta_salida};\n'
                
                # si es un valor menor que 0 multiplica por -1
                cadenaTraduccion3d += f'L{etiqueta_actual}:\n'
                cadenaTraduccion3d += f'{nodo3d.valor} = {nodo3d.valor} * -1;\n\n'

                cadenaTraduccion3d += f'L {etiqueta_salida};\n\n'

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





        # NATIVA SQRT()
        # exp.sqrt()
        elif self.tipo == TipoNativas.SQRT:


            if nodo3d.tipo == TipoExpresion.ID:
                nodo3d = entorno.getVariable3d(nodo3d.valor)


            termporal_actual = traductor3d.getTemporal()
            traductor3d.aumentarTemporal()

            cadenaTraduccion3d += f'\n'
            cadenaTraduccion3d += f'\n'
            cadenaTraduccion3d += f'\n'
            cadenaTraduccion3d += f'/*-- NATIVA SQRT() --*/\n'
            cadenaTraduccion3d += f't{termporal_actual} = {nodo3d.valor};\n'
            cadenaTraduccion3d += f't5 = t{termporal_actual};\n'
            cadenaTraduccion3d += f'funcionSqrt();\n'

            # agregando traduccion
            traductor3d.addCadenaTemporal(cadenaTraduccion3d)


            return Simbolo3d(
                self.fila,
                self.columna,
                None,
                nodo3d.tipo,
                f't6',
                None,
                0,
                0
            )










        return -1