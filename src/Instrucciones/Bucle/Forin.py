from src.Interfaces.Instruccion import Instruccion
from src.environment.Environment import Environment
from src.Expresiones.Primitivo import Primitivo
from src.environment.Simbolo import Simbolo
from src.Interfaces.TipoMutable import TipoMutable
from src.Interfaces.TipoExpresion import TipoExpresion


class Forin(Instruccion):

    def __init__(self, fila, columna, tablaErrores, variable, inicio, final, instrucciones):
        self.fila = fila
        self.columna = columna
        self.variable = variable
        self.inicio = inicio
        self.final = final
        self.instrucciones = instrucciones
        # self.retornoForin = ''
        self.tablaErrores = tablaErrores


    def ejecutar(self, entorno):


        retornoForin = ''
        # crear un nuevo entorno para el for
        numeroEntorno = entorno.numero + 1
        envFor = Environment('FOR',numeroEntorno,entorno)




                
        # tipo de ejecucion del ciclo for
        inicioFor = self.inicio.ejecutar(entorno)
        finalFor = self.final.ejecutar(entorno)

        # si son variables
        if inicioFor.tipo == TipoExpresion.ID and finalFor.tipo == TipoExpresion.ID:
            inicioFor = entorno.getVariable(inicioFor.valor)
            finalFor = entorno.getVariable(finalFor.valor)
        
        elif finalFor.tipo == TipoExpresion.ID:
            finalFor = entorno.getVariable(finalFor.valor)

        elif inicioFor.tipo == TipoExpresion.ID:
            inicioFor = entorno.getVariable(inicioFor.valor)



        # creacion variables para iteraciones
        if self.variable.tipo == TipoExpresion.ID:
            entorno.addVariable(self.variable.valor,
                        Simbolo(
                            self.fila,
                            self.columna,
                            self.variable.valor,
                            inicioFor.tipo,
                            inicioFor.valor,
                            TipoMutable.MUTABLE
                            ))
        else:
            return 'FORIN -> erorr parametros'




        if inicioFor.tipo == TipoExpresion.INTEGER and finalFor.tipo == TipoExpresion.INTEGER:           

            
            # ejecucion del ciclo for
            for i in range(inicioFor.valor, finalFor.valor):

                # ejecucion de las instrucciones que hay en el ciclo for
                for instruccion in self.instrucciones:

                    result = instruccion.ejecutar(envFor)

                    # menejo de instrucciones break y continue
                    if isinstance(result, Primitivo) and result.tipo == TipoExpresion.BREAK:
                        if result.valor is not None:
                            retornoForin += result.valor
                        return retornoForin

                    elif isinstance(result, Primitivo) and result.tipo == TipoExpresion.CONTINUE:
                        if result.valor is not None:
                            retornoForin += result.valor
                        break


                    # concatenacion del resultado del for
                    if result is not None:
                        retornoForin += result


                # actualizcion de la variable
                variableFor = envFor.getVariable(self.variable.valor)
                envFor.updateVariabe(self.variable.valor,
                    Simbolo(
                        self.fila,
                        self.columna,
                        self.variable.valor,
                        inicioFor.tipo,
                        variableFor.valor + 1,
                        TipoMutable.MUTABLE
                        ))



            return retornoForin

        else:
            # para reportes
            self.tablaErrores.append(['FORIN : error paramentros',entorno.nombre,self.fila,self.columna])
            # --------------------------------
            return 'FORIN : error paramentros'


        

