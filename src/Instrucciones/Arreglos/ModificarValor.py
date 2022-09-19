
from src.Interfaces.Instruccion import Instruccion
from src.Interfaces.TipoExpresion import TipoExpresion
from src.Interfaces.TipoMutable import TipoMutable
from src.environment.Simbolo import Simbolo


class ModificarValorArreglo(Instruccion):

    def __init__(self, fila, columna, tablaErrores, variable, exp, newValue):
        self.fila = fila
        self.columna = columna
        self.tablaErrores = tablaErrores
        self.variable = variable
        self.exp = exp
        self.newValue = newValue


    def ejecutar(self, entorno):

        print('************ MODIFICANDO VALOR DE UN ARREGLO **************')
        posicion_acceso_arreglo = 0


        # primer filtro saber si la variable tiene existencia
        # solo me viene el identificador de la variable

        var = entorno.getVariable(self.variable)


        # filtro para entender que la variable tiene existencia en el entorno y que sea tipo arreglo
        if var.tipo == TipoExpresion.ARREGLO and var is not None:
            

            # verificacion de la mutabilidad del arreglo
            if var.mutabilidad == TipoMutable.MUTABLE:



                # tamanio actual del arreglo
                tamanioArreglo = len(var.valor) - 1


                # saber cual la cantidad que tengo que bajar en el vector para el acceso
                cantidad_accesos = len(self.exp)



                # si el nuevo valores es una variable hay que buscarla
                nuevoValor = self.newValue.ejecutar(entorno)
                if nuevoValor.tipo == TipoExpresion.ID:
                    nuevoValor = entorno.getVariable(nuevoValor.valor)











                # repetira la n  -1 del tamanio de acceso al arreglo
                # for i in range(cantidad_accesos):
                #
                #     # revision si el index si es una variable
                #     if self.exp[posicion_acceso_arreglo].tipo == TipoExpresion.ID:
                #         varIndex = entorno.getVariable(self.exp[posicion_acceso_arreglo].ejecutar(entorno).valor)
                #         index = varIndex.valor
                #     else:
                #         index = self.exp[posicion_acceso_arreglo].ejecutar(entorno).valor
                #
                #
                #
                #     arreglo = var.valor[index].ejecutar(entorno)
                #     posicion_acceso_arreglo += 1


                if cantidad_accesos > 1:
                    self.modidificarValorArreglo(var, posicion_acceso_arreglo, nuevoValor, entorno)






                # actualizacion del arreglo con los nuevos valores
                entorno.addVariable(self.variable,var)


                print('paro')





            else:
                # para reportes
                self.tablaErrores.append([f'variable {self.variable} no es mutable', entorno.nombre, self.fila, self.columna])
                # --------------------------------
                return f'variable {self.variable} no es mutable'






        else:
            # para reportes
            self.tablaErrores.append([f'variable {self.variable} no es de tipo arreglo', entorno.nombre, self.fila, self.columna])
            # --------------------------------
            return f'variable {self.variable} no es de tipo arreglo'


        return None






    # funcion recursiva cambiar el varlor del arreglo
    def modidificarValorArreglo(self, var, posicion_acceso_arreglo, nuevoValor, entorno):

        # ******************************************
        # revision si el index si es una variable
        if self.exp[posicion_acceso_arreglo].tipo == TipoExpresion.ID:
            varIndex = entorno.getVariable(self.exp[posicion_acceso_arreglo].ejecutar(entorno).valor)
            index = varIndex.valor
        else:
            index = self.exp[posicion_acceso_arreglo].ejecutar(entorno).valor

        # *********************************************


        # print(f'------------------------------------------>{type(var)}')
        if isinstance(var,Simbolo):
            var.valor[index].ejecutar(entorno)

            posicion_acceso_arreglo += 1

            if var.valor[index].tipo == TipoExpresion.ARREGLO:
                self.modidificarValorArreglo(var.valor[index], posicion_acceso_arreglo, nuevoValor, entorno)

            else:
                var.valor[index].valor = nuevoValor.valor
        else:
            var.listadoExpresiones[index].ejecutar(entorno)

            posicion_acceso_arreglo += 1

            if var.listadoExpresiones[index].tipo == TipoExpresion.ARREGLO:
                self.modidificarValorArreglo(var.listadoExpresiones[index], posicion_acceso_arreglo, nuevoValor, entorno)

            else:
                var.listadoExpresiones[index].valor = nuevoValor.valor
