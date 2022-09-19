from src.Interfaces.Instruccion import Instruccion
from src.Interfaces.TipoExpresion import TipoExpresion
from src.Interfaces.TipoMutable import TipoMutable



class AsignacionStruct(Instruccion):


    def __init__(self, fila, columna, variableStruct, variableCambio , newValue):
        self.fila = fila
        self.columna = columna
        self.variableStruct = variableStruct
        self.variableStructCambio = variableCambio
        self.newValue = newValue


    def ejecutar(self, entorno):


        # print('******** ALTER VALUE STRUCT **************')

        # busqueda del la variable
        var_struct = entorno.getVariable(self.variableStruct)



        # opcion si se encuentra o no la variable
        if var_struct != None and var_struct.tipo == TipoExpresion.STRUCT:


            # revision si se pueden mutar los valores
            if var_struct.mutabilidad == TipoMutable.MUTABLE:    


                # print('------- variable tipo struct -----------')

                # elemento a elemento de todos la lista de los elementos del struct
                for elemento in var_struct.elementos:

                    # ejecuto el elemento actual donde voy
                    result_elemento = elemento.ejecutar(entorno)

                    
                    if result_elemento.identificador == self.variableStructCambio:

                        # para obtener el nuevo valor
                        primitivo = self.newValue.ejecutar(entorno)
                        elemento.valor = primitivo.valor

                        # actualizar variable
                        # identificador de la variable y su contenido
                        entorno.addVariable(self.variableStruct,var_struct) 

                        return None


                print('------------------------------')
                return f'Struct --> {self.variableStruct} no contiene el atributo {self.variableStructCambio}'


            
            else: 
                return f'Variabe --> {self.variableStruct} no modificable'






        elif var_struct != None and var_struct.tipo != TipoExpresion:
            return f'Variable --> {self.variableStruct} no es de tipo struct'




        # no se encontro la variable en en los entornos
        else:            
            return f'Variable --> {self.variableStruct} no existe'
