from src.Interfaces.Instruccion import Instruccion
from src.Interfaces.TipoExpresion import TipoExpresion


class Insert(Instruccion):

    def __init__(self, variable, posicion, nuevoValor):
        self.variable = variable
        self.posicion = posicion 
        self.nuevoValor = nuevoValor



    def ejecutar(self, entorno):
        
        print('INSERT ')

        # busqueda del vector
        vector = entorno.getVariable(self.variable)


        # variable para manipulacion sobre la posicion
        posicionInsert = self.posicion.ejecutar(entorno)


        # variable para el nuevo valor
        newValue = self.nuevoValor.ejecutar(entorno)



        # # nueva posicion de insert es una variable
        # if posicionInsert == TipoExpresion.ID:
        #     posicionInsert = entorno.getVariable(entorno)
        #
        #
        #
        # # nuevo valor es una variable
        if newValue.tipo == TipoExpresion.ID:
            newValue = entorno.getVariable(newValue.valor)



        # verificar que tengas elementos la lista en esa posicion



        # ******************************************************
        # obtener variable en el punto del insercion
        # valorPosicion = vector.lista[posicionInsert.valor-1]
        # valorPosicion.valor = newValue.valor


        # insertando un nuevo valor en una nueva posicion
        # vector.lista.insert(posicionInsert.valor,valorPosicion)
        # *********************************************************


        vector.lista.append(newValue)


        # actualizando variable en el entorno
        entorno.addVariable(self.variable,vector)


        return None