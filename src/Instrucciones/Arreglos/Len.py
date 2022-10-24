from src.Interfaces.Expresion import Expresion
from src.Interfaces.TipoExpresion import TipoExpresion
from src.Interfaces.TipoMutable import TipoMutable
from src.environment.Simbolo import Simbolo
from src.Instrucciones.Arreglos.ExpArreglo import ExpArreglo


from src.environment.Simbolo3d import Simbolo3d




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










    # -------------------------------------------------------------------------
    #                   TRADUCCION PARA EL TAMANIO DE UN ARREGLO
    # -------------------------------------------------------------------------
    def traducir(self, entorno, traductor3d, cadena):

        cadenaTraduccion3d = ''

        arreglo = entorno.getVariable3d(self.variable.valor)

        temporal_arreglo = traductor3d.getTemporal()
        traductor3d.aumentarTemporal()

        temporal_heap = traductor3d.getTemporal()
        traductor3d.aumentarTemporal()

        cadenaTraduccion3d += f'\n'
        cadenaTraduccion3d += f'\n'
        cadenaTraduccion3d += f'/*---- LEN DE UN ARREGLO ----*/\n'
        cadenaTraduccion3d += f't{temporal_arreglo} = {arreglo.posicion}; \n'
        cadenaTraduccion3d += f'\n'
        cadenaTraduccion3d += f't{temporal_heap} = heap[(int) t{temporal_arreglo}];\n'
        cadenaTraduccion3d += f'\n'
        cadenaTraduccion3d += f'\n'
        cadenaTraduccion3d += f'\n'
        cadenaTraduccion3d += f'\n'


        # **********************************************
        #               TRADUCCION     
        traductor3d.addCadenaTemporal(cadenaTraduccion3d)

        len_arreglo = Simbolo3d(
            0,
            0,
            None,
            TipoExpresion.INTEGER,
            f't{temporal_heap}',
            None,
            0,
            0           
        )




        return len_arreglo











    # -------------------------------------------------------------------------
    #                   TRADUCCION PARA EL TAMANIO DE UN ARREGLO
    # -------------------------------------------------------------------------
    def optimizar(self, entorno, traductor3d, cadena):

        cadenaTraduccion3d = ''

        arreglo = entorno.getVariable3d(self.variable.valor)

        temporal_arreglo = traductor3d.getTemporal()
        traductor3d.aumentarTemporal()

        temporal_heap = traductor3d.getTemporal()
        traductor3d.aumentarTemporal()

        cadenaTraduccion3d += f'\n'
        cadenaTraduccion3d += f'\n'
        cadenaTraduccion3d += f'/*---- LEN DE UN ARREGLO ----*/\n'
        cadenaTraduccion3d += f't{temporal_arreglo} = {arreglo.posicion}; \n'
        cadenaTraduccion3d += f'\n'
        cadenaTraduccion3d += f't{temporal_heap} = heap[(int) t{temporal_arreglo}];\n'
        cadenaTraduccion3d += f'\n'
        cadenaTraduccion3d += f'\n'
        cadenaTraduccion3d += f'\n'
        cadenaTraduccion3d += f'\n'


        # **********************************************
        #               TRADUCCION     
        traductor3d.addCadenaTemporal(cadenaTraduccion3d)

        len_arreglo = Simbolo3d(
            0,
            0,
            None,
            TipoExpresion.INTEGER,
            f't{temporal_heap}',
            None,
            0,
            0           
        )




        return len_arreglo