from src.Interfaces.Expresion import Expresion
from src.Interfaces.TipoExpresion import TipoExpresion
from src.Interfaces.TipoMutable import TipoMutable
from src.environment.Simbolo import Simbolo
from src.Instrucciones.Arreglos.ExpArreglo import ExpArreglo

class Len(Expresion):


    def __init__(self, variable):
        self.variable = variable


    def ejecutar(self, entorno):


        print('************* LEN de arreglos ******************')

        # primer filtro con la variable sea tipo arreglo
        if self.variable is not None and self.variable.tipo == TipoExpresion.ID:

            varrArreglo = entorno.getVariable(self.variable.valor)


            # que la variable sea tipo arreglo
            if varrArreglo.tipo == TipoExpresion.ARREGLO:

                # if isinstance(var,Simbolo):


                if isinstance(varrArreglo,ExpArreglo):
                    tamanioArreglo = len(varrArreglo.listadoExpresiones)
                else:
                    tamanioArreglo = len(varrArreglo.valor)



                return Simbolo(
                    0,
                    0,
                    None,
                    TipoExpresion.INTEGER,
                    tamanioArreglo,
                    TipoMutable.MUTABLE
                )


            elif varrArreglo is not None and varrArreglo.tipo == TipoExpresion.VECTOR:

                tamanioVector = len(varrArreglo.lista)

                return Simbolo(
                    0,
                    0,
                    None,
                    TipoExpresion.INTEGER,
                    tamanioVector,
                    TipoMutable.MUTABLE
                )


        elif self.variable is not None and self.variable.tipo == TipoExpresion.ARREGLO:

            varrArreglo = self.variable.ejecutar(entorno)

            if isinstance(varrArreglo, ExpArreglo):
                tamanioArreglo = len(varrArreglo.listadoExpresiones)
            else:
                tamanioArreglo = len(varrArreglo.valor)

            return Simbolo(
                0,0,None,TipoExpresion.INTEGER,tamanioArreglo,TipoMutable.MUTABLE
            )

            print('para obligatorio')




        return f'eror en la funcion len del arreglo'






