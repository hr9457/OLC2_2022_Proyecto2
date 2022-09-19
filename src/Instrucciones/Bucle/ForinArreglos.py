from src.Interfaces.Instruccion import Instruccion
from src.Interfaces.TipoExpresion import TipoExpresion
from src.Interfaces.TipoMutable import TipoMutable
from src.environment.Environment import Environment
from src.environment.Environment import Simbolo
from src.Expresiones.Primitivo import Primitivo
from src.Instrucciones.Struct.SimboloStruct import SimboloStruct
from src.Instrucciones.Struct.PrimateStruct import PrimateStruct




class ForinArreglos(Instruccion):

    def __init__(self,fila, columna, pivote, variable, instrucciones):
        self.fila = fila
        self.columna = columna
        self.pivote = pivote
        self.variable = variable
        self.instrucciones = instrucciones


    def ejecutar(self, entorno):

        retornoForinArreglos = ''



        # primer filtro verificacion del pivote
        if self.pivote is not None and self.pivote.tipo == TipoExpresion.ID:

            
            # agregro variable en el entorno afuera del for
            entorno.addVariable(self.pivote.valor,
                        Simbolo(
                            self.fila,
                            self.columna,
                            self.pivote.valor, # identificador
                            self.pivote.tipo,
                            '',
                            TipoMutable.MUTABLE
                            ))
            
            
            
            
            # creacion de un nuevo entorno para el for
            numeroEntorno = entorno.numero + 1
            envForIn = Environment('FOR',numeroEntorno,entorno)


            # ejecucion del la expresion para recorrer
            exp = self.variable.ejecutar(entorno)
            variablePivote = self.pivote.ejecutar(entorno)


            # si la expresion resulta ser una variable
            if exp.tipo == TipoExpresion.ID:
                exp = entorno.getVariable(exp.valor)



            # si la expresion es un arreglo que poder recorrer
            if exp.tipo == TipoExpresion.ARREGLO:


                if isinstance(exp,Simbolo):
                    return self.recorrerArreglo(exp.valor, entorno, envForIn, retornoForinArreglos)

                else:
                    return self.recorrerArreglo(exp.listadoExpresiones, entorno, envForIn, retornoForinArreglos)



            # si en el for in llega un vector
            elif exp.tipo == TipoExpresion.VECTOR:

                for elementoVector in exp.lista:


                    elemento = elementoVector[0].ejecutar(envForIn)



                    # nueva asigancion a la variable pivote con el valor del arreglo
                    # actualizacon de la variable pivote con su nuevo valor
                    varPivote = entorno.getVariable(self.pivote.valor)

                    elementoValor = []
                    elementoValor.append(Simbolo(0,0,elemento.identificador,elemento.primate.nodo.tipo, elemento.primate.nodo.valor, elemento.primate.nodo.tipo))



                    p = PrimateStruct(elementoValor,varPivote.mutabilidad)
                    entorno.addVariable(varPivote.identificador,p)
                    



                    # EJECUTAR LAS INSTRUCCIONES QUE SE ENCUENTRE DENTRO DEL VECTOR
                    for instruccion in self.instrucciones:

                        result = instruccion.ejecutar(envForIn)
                        print(result)


                        # menejo de instrucciones break y continue
                        if isinstance(result, Primitivo) and result.tipo == TipoExpresion.BREAK:
                            if result.valor is not None:
                                retornoForinArreglos += result.valor
                            return retornoForinArreglos

                        elif isinstance(result, Primitivo) and result.tipo == TipoExpresion.CONTINUE:
                            if result.valor is not None:
                                retornoForinArreglos += result.valor
                            break


                        # concatenacion del resultado del for
                        if result is not None:
                            retornoForinArreglos += result



                    # limpieza del pivote
                    entorno.addVariable(self.pivote.valor,
                                        Simbolo(
                                            self.fila,
                                            self.columna,
                                            self.pivote.valor,  # identificador
                                            self.pivote.tipo,
                                            '',

                                            TipoMutable.MUTABLE
                                        ))


                # return retornoForinArreglos
                return retornoForinArreglos







        else:
            return f'var {self.pivote.valor} no es un ID'









    # funcion para recorre los arreglos en ciclo en for in
    def recorrerArreglo(self, listado, entorno, envForIn, retornoForinArreglos):

        # for para recorrer el arreglo y su contenido
        for elementoArreglo in listado:

            # listado del valor del arreglo
            elemento = elementoArreglo.ejecutar(entorno)

            # nueva asigancion a la variable pivote con el valor del arreglo
            # actualizacon de la variable pivote con su nuevo valor
            varPivote = entorno.getVariable(self.pivote.valor)
            varPivote.valor = elemento.valor
            varPivote.tipo = elemento.tipo
            entorno.addVariable(self.pivote.valor, varPivote)

            for instruccion in self.instrucciones:

                result = instruccion.ejecutar(envForIn)

                # menejo de instrucciones break y continue
                if isinstance(result, Primitivo) and result.tipo == TipoExpresion.BREAK:
                    if result.valor is not None:
                        retornoForinArreglos += result.valor
                    return retornoForinArreglos

                elif isinstance(result, Primitivo) and result.tipo == TipoExpresion.CONTINUE:
                    if result.valor is not None:
                        retornoForinArreglos += result.valor
                    break

                # concatenacion del resultado del for
                if result is not None:
                    retornoForinArreglos += result

        return retornoForinArreglos
