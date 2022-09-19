from src.Interfaces.Instruccion import Instruccion

class InsertVector(Instruccion):

    def __int__(self, variable):
        self.variable = variable
        # self.posicion = posicion
        # self.newValue = newValue
        


    def ejecutar(self, entorno):

        print('metodo insert')

        # busqueda de la variables
        # getVariable = entorno.getVariable(self.variable.identificador)


        return None