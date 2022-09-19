from src.Interfaces.Instruccion import Instruccion
from src.Interfaces.TipoExpresion import TipoExpresion
from src.Instrucciones.Struct.Struct import Struct
from src.Instrucciones.Struct.PrimateStruct import PrimateStruct
from src.environment.Simbolo import Simbolo
from src.Interfaces.TipoMutable import TipoMutable


# clase para para hacerun build partiendo de un struct

class BuildStruct(Instruccion):


    def __init__(self, fila, columna, modeloStruct, listadoParametros=None):
        self.fila = fila 
        self.columna = columna
        self.modeloStruc = modeloStruct
        self.listadoParametros = listadoParametros



    def ejecutar(self,entorno):

        
        # ========================================
        # busqueda y traer el modelo del struct
        # ========================================
        struct = entorno.getStruct(self.modeloStruc)
        if struct is not None:
            listaElementosModelo = struct.elementos

        elif struct is None:
            return f' Struct --> {self.modeloStruc} no encontrado '





        

        # ==============================================
        # limintacion de cantidad de elementos del struct
        # =============================================== 
        listaBuild = []
        if listaElementosModelo is not None and len(listaElementosModelo) == len(self.listadoParametros):
            



            contadorParametro = 0


            print('*************** BUILD A PARTIR DE UN STRUCT *************************')


            # listadoElementos la estructura base
            for elementoModelo in listaElementosModelo:


                # ejecucion elementoModelo a elmento del listado recibido
                # elementos o parametros recibidos cuando se quiere contruir un struct
                # recibe una exp tine que retornar un primitivo
                parametro = self.listadoParametros[contadorParametro].ejecutar(entorno)


                # comparacion de tipo de los elementos a asignar
                if elementoModelo.identificador == parametro.identificador:

                    
                    # se econtro el mismo identificador
                    # ejecuto para sacar el valor que se tiene que agregar al struct
                    # primate tiene un identificador y un primate

                    primate = parametro.primate.ejecutar(entorno)

                    print('paro obligatorio')
                    

                    # comparacion de tipos para poder ser asignado
                    if elementoModelo.tipo == primate.tipo:


                        if primate.tipo == TipoExpresion.STRUCT:
                            
                            symbol = Simbolo(
                                0,
                                0,
                                elementoModelo.identificador,
                                elementoModelo.tipo,
                                primate,
                                TipoMutable.MUTABLE
                            )
                            listaBuild.append(symbol)


                        else:
                            
                            symbol = Simbolo(
                                        0,
                                        0,
                                        elementoModelo.identificador,
                                        elementoModelo.tipo,
                                        primate.valor,
                                        TipoMutable.MUTABLE
                                        )
                            listaBuild.append(symbol)



                else:
                    return f'Struct {self.modeloStruc} parametro {parametro.identificador} no econtrado'

                contadorParametro += 1


            

            # solo lista de elementos
            p = PrimateStruct(listaBuild)

            return p





        #  eeror cantidad de tipos no coinciden
        elif listaElementosModelo is not None and len(listaElementosModelo) != len(self.listadoParametros):
            return f'Struct --> {self.modeloStruc} error de parametros '


