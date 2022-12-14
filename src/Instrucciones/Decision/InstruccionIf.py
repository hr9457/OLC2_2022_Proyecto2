from src.Interfaces.Instruccion import Instruccion
from src.Interfaces.TipoExpresion import TipoExpresion
from src.Expresiones.Primitivo import Primitivo
from src.Instrucciones.Imprimir import Imprimir
from src.Instrucciones.Decision import instruccionElse
from src.environment.Environment import Environment
from src.Error.Error import Error



# para traduccion en 3d
from src.environment.Simbolo3d import Simbolo3d




class InstruccionIf(Instruccion):

    def __init__(self, fila, columna, expresion, instruccionesIF=None, nodo=None):
        self.fila = fila
        self.columna = columna
        self.expresion = expresion
        self.instruccionesIF = instruccionesIF
        self.nodo = nodo
        self.resultadoIf = ''
        self.resultadoElse = ''
        # self.tablaErrores = tablaErrores

    def ejecutar(self, entorno):

        print('DENTRO DE LA INSTRUCCION IF')
        

        # retorna un primitivo
        exp = self.expresion.ejecutar(entorno)

        # la exp de ejeccutada es una variable
        if exp.tipo == TipoExpresion.ID:
            exp = entorno.getVariable(exp.valor)

        # verifica que la expresion se de tipo boolean
        if exp.tipo == TipoExpresion.BOOL:

            # verificacion del valor de la expresion true o false
            if exp.valor == 'true':

                if self.instruccionesIF != None:

                    # creacion de un nuevo entrono para el manejo del if
                    numeroEntorno = entorno.numero + 1
                    envIf = Environment('IF', numeroEntorno, entorno)
                    self.resultadoIf = ''

                    for instruccion in self.instruccionesIF:

                        result = instruccion.ejecutar(envIf)
                        print(f'IF --> {result}')


                        # manejo para break y continue
                        if isinstance(result, Primitivo) and result.tipo == TipoExpresion.BREAK:
                            if result is not None and result.valor is not None:
                                self.resultadoIf += result.valor
                            retorno = Primitivo(None, None, TipoExpresion.BREAK, self.resultadoIf)
                            return retorno

                        elif isinstance(result, Primitivo) and result.tipo == TipoExpresion.CONTINUE:
                            if result is not None and result.valor is not None:
                                self.resultadoIf += result.valor
                            retorno = Primitivo(None, None, TipoExpresion.CONTINUE, self.resultadoIf)
                            return retorno


                        elif isinstance(result, Primitivo) and result.tipo == TipoExpresion.RETURN:
                            result = result.ejecutar(envIf)
                            retorno = Primitivo(
                                None, 
                                None, 
                                TipoExpresion.RETURN, 
                                result.valor
                                )
                            return retorno

                        
                        if result != None:
                            self.resultadoIf += result


                    return self.resultadoIf


                else:
                    return self.resultadoIf



            else:

                if self.nodo != None:
                    # creacion de un nuevo entrono para el manejo de else y else if
                    numeroEntorno = entorno.numero + 1
                    envElse = Environment('ELSE/ELSE IF', numeroEntorno, entorno)
                    # self.resultadoElse = ''
                    return self.nodo.ejecutar(envElse)


                else:
                    return self.resultadoElse



        else:
            # para reportes
            # self.tablaErrores.append(['IF: Condicion no es de tipo bool',entorno.nombre,self.fila,self.columna])
            # --------------------------------
            return 'IF: Condicion no es de tipo bool'
















    

    # -------------------------------------------------------------------------
    #                   TRADUCCION DE LA PIRNTLN A 3D
    # -------------------------------------------------------------------------
    def traducir(self, entorno, traductor3d, cadena):

        cadenaTraduccion3d = ''


        # creacion de un nuevo entrono para el manejo del if
        numeroEntorno = entorno.numero + 1
        envIf = Environment('IF', numeroEntorno, entorno)



        expresion3d = self.expresion.traducir(entorno, traductor3d, cadena)



        if expresion3d.valor == '1' or expresion3d.valor == '0':

            
            if expresion3d.valor == '1':
                # cuando la expresion sea if salta donde mismo
                cadenaTraduccion3d += '\n'
                cadenaTraduccion3d += '\n'
                cadenaTraduccion3d += '/*------- IF -------- */\n'
                cadenaTraduccion3d += f'/*---- {expresion3d.valor} ---*/\n'
                etiquetaIf = traductor3d.getEtiqueta()
                cadenaTraduccion3d += f'goto L{etiquetaIf};\n'
                traductor3d.aumentarEtiqueta()
                cadenaTraduccion3d += f'L{etiquetaIf}:\n'
            
                # TRADUCCION
                traductor3d.addCadenaTemporal(cadenaTraduccion3d)


                # generacion de las instrucciones del if
                for instruccion in self.instruccionesIF:
                    instruccion.traducir(envIf, traductor3d, cadena)


                # salida del if si se llega a cumplir la condicionesw
                salidaIf = traductor3d.getEtiqueta()
                traductor3d.addCadenaTemporal(f'\n')
                traductor3d.addCadenaTemporal(f'\n')
                traductor3d.addCadenaTemporal(f'/*-- SALIDA DEL IF --*/\n')
                traductor3d.addCadenaTemporal(f'goto L{salidaIf};\n')
                traductor3d.aumentarEtiqueta()



                # si los procesos logicos generaron etiquetas temporales de salida
                # para saltar al else
                traductor3d.addCadenaTemporal(traductor3d.getSaltosTemporales())
                traductor3d.clearSaltosTemporales()
                

                # revison si viene una else en la ejecucion
                if self.nodo != None:
                    cadenaTraduccion3d = ''
                    # salto para el else
                    etiquetaElse = traductor3d.getEtiqueta()
                    traductor3d.aumentarEtiqueta()
                    cadenaTraduccion3d += f'L{etiquetaElse}:\n'
                    traductor3d.addCadenaTemporal(cadenaTraduccion3d)

                    self.nodo.traducir(envIf, traductor3d, cadena)

                
                # salida del todo si entra al if
                traductor3d.addCadenaTemporal(f'L{salidaIf}:\n')


                return None




            #  cuando la expresion sea false
            elif expresion3d.valor == '0':
                # cuando la expresion sea if salta donde mismo
                cadenaTraduccion3d += '\n'
                cadenaTraduccion3d += '\n'
                cadenaTraduccion3d += '/*------- IF -------- */\n'
                cadenaTraduccion3d += f'/*---- {expresion3d.valor} ---*/\n'
                etiquetaIf = traductor3d.getEtiqueta()
                cadenaTraduccion3d += f'goto L{etiquetaIf};\n'
                traductor3d.aumentarEtiqueta()
                
                # cadenaTraduccion3d += f'L{etiquetaIf}:\n'
                traductor3d.addSaltoTemporal(f'L{etiquetaIf}:\n')
            
                # TRADUCCION
                traductor3d.addCadenaTemporal(cadenaTraduccion3d)


                # generacion de las instrucciones del if
                for instruccion in self.instruccionesIF:
                    instruccion.traducir(entorno, traductor3d, cadena)


                # salida del if si se llega a cumplir la condicionesw
                salidaIf = traductor3d.getEtiqueta()
                traductor3d.addCadenaTemporal(f'\n')
                traductor3d.addCadenaTemporal(f'\n')
                traductor3d.addCadenaTemporal(f'/*-- SALIDA DEL IF --*/\n')
                traductor3d.addCadenaTemporal(f'goto L{salidaIf};\n')
                traductor3d.aumentarEtiqueta()



                # si los procesos logicos generaron etiquetas temporales de salida
                # para saltar al else
                traductor3d.addCadenaTemporal(traductor3d.getSaltosTemporales())
                traductor3d.clearSaltosTemporales()
                

                # revison si viene una else en la ejecucion
                if self.nodo != None:
                    cadenaTraduccion3d = ''
                    # salto para el else
                    etiquetaElse = traductor3d.getEtiqueta()
                    traductor3d.aumentarEtiqueta()
                    cadenaTraduccion3d += f'L{etiquetaElse}:\n'
                    traductor3d.addCadenaTemporal(cadenaTraduccion3d)

                    # creacion de un nuevo entrono para el manejo de else y else if
                    numeroEntorno = entorno.numero + 1
                    envElse = Environment('ELSE/ELSE IF', numeroEntorno, entorno)

                    self.nodo.traducir(envElse, traductor3d, cadena)

                
                # salida del todo si entra al if
                traductor3d.addCadenaTemporal(f'L{salidaIf}:\n')


                return None















        else:            
            cadenaTraduccion3d += '\n'
            cadenaTraduccion3d += '\n'
            cadenaTraduccion3d += traductor3d.getSaltoLogicoTrue()
            traductor3d.clearSaltoLogicoTrue()
            cadenaTraduccion3d += '/*------- IF -------- */\n'
            etiquetaIf = traductor3d.getEtiqueta()
            cadenaTraduccion3d += f'if ( {expresion3d.valor} ) goto L{etiquetaIf};\n'
            traductor3d.aumentarEtiqueta()

            # salto para el else
            etiquetaElse = traductor3d.getEtiqueta()
            cadenaTraduccion3d += f'goto L{etiquetaElse};\n'
            traductor3d.aumentarEtiqueta()


            # salto para ejecucion de las intrucciones del if
            cadenaTraduccion3d += f'L{etiquetaIf}:\n'
            traductor3d.addCadenaTemporal(cadenaTraduccion3d)
            # **********************************************



            #  traduce las instrucciones del if ---------
            # generacion de las instrucciones del if
            for instruccion in self.instruccionesIF:


                instruccion.traducir(entorno, traductor3d, cadena)


                
                # saber si hay un break
                if isinstance(instruccion, Primitivo) and instruccion.tipo == TipoExpresion.BREAK:
                    cadena_break = ''
                    salto_break = traductor3d.getEtiqueta()
                    traductor3d.aumentarEtiqueta()

                    cadena_break += '\n'
                    cadena_break += '/*-- BREAK --*/\n'
                    cadena_break += f'goto L{salto_break};\n\n\n'
                    traductor3d.addCadenaTemporal(cadena_break)
                    traductor3d.addSaltoBreak(f'L{salto_break}:\n')


                # saber si hay un continue
                if isinstance(instruccion, Primitivo) and instruccion.tipo == TipoExpresion.CONTINUE:
                    cadena_continue = ''
                    salto_continue = traductor3d.getEtiqueta()
                    traductor3d.aumentarEtiqueta()

                    cadena_continue += '\n'
                    cadena_continue += '/*-- CONTINUE --*/\n'
                    cadena_continue += f'goto L{salto_continue};\n'
                    traductor3d.addSaltoContinue(f'L{salto_continue}:\n')
                    traductor3d.addCadenaTemporal(cadena_continue)

                




            
            # salida del if si se llega a cumplir la condicionesw
            salidaIf = traductor3d.getEtiqueta()
            traductor3d.addCadenaTemporal(f'goto L{salidaIf};\n')
            traductor3d.aumentarEtiqueta()




            # salto condicional para el else
            traductor3d.addCadenaTemporal(f'\n')
            traductor3d.addCadenaTemporal(f'\n')
            traductor3d.addCadenaTemporal(f'L{etiquetaElse}:\n')


            
            # si los procesos logicos generaron etiquetas temporales de salida
            # para saltar al else
            traductor3d.addCadenaTemporal(traductor3d.getSaltosTemporales())
            traductor3d.clearSaltosTemporales()



            # traduccion de las instrucciones del else
            traductor3d.addCadenaTemporal(f'\n')
            traductor3d.addCadenaTemporal(f'\n')
            traductor3d.addCadenaTemporal(f'\n')
            traductor3d.addCadenaTemporal(f'\n')
            traductor3d.addCadenaTemporal(f'/*-- ELSE --*/\n')

            if self.nodo != None:

                # traduccion de las instrucciones del else\
                self.nodo.traducir(entorno, traductor3d, cadena)
                



            # salida del todo si entra al if
            traductor3d.addCadenaTemporal(f'L{salidaIf}:\n')


            

            return None









    

    # -------------------------------------------------------------------------
    #                   TRADUCCION DE LA PIRNTLN A 3D
    # -------------------------------------------------------------------------
    def optimizar(self, entorno, traductor3d, cadena):

        cadenaTraduccion3d = ''


        # creacion de un nuevo entrono para el manejo del if
        numeroEntorno = entorno.numero + 1
        envIf = Environment('IF', numeroEntorno, entorno)



        expresion3d = self.expresion.optimizar(entorno, traductor3d, cadena)



        if expresion3d.valor == '1' or expresion3d.valor == '0':

            
            if expresion3d.valor == '1':
                # cuando la expresion sea if salta donde mismo
                cadenaTraduccion3d += '\n'
                cadenaTraduccion3d += '\n'
                cadenaTraduccion3d += '/*------- IF -------- */\n'
                cadenaTraduccion3d += f'/*---- {expresion3d.valor} ---*/\n'
                etiquetaIf = traductor3d.getEtiqueta()
                cadenaTraduccion3d += f'goto L{etiquetaIf};\n'
                traductor3d.aumentarEtiqueta()
                cadenaTraduccion3d += f'L{etiquetaIf}:\n'
            
                # TRADUCCION
                traductor3d.addCadenaTemporal(cadenaTraduccion3d)


                # generacion de las instrucciones del if
                for instruccion in self.instruccionesIF:
                    instruccion.optimizar(envIf, traductor3d, cadena)


                # salida del if si se llega a cumplir la condicionesw
                salidaIf = traductor3d.getEtiqueta()
                traductor3d.addCadenaTemporal(f'\n')
                traductor3d.addCadenaTemporal(f'\n')
                traductor3d.addCadenaTemporal(f'/*-- SALIDA DEL IF --*/\n')
                traductor3d.addCadenaTemporal(f'goto L{salidaIf};\n')
                traductor3d.aumentarEtiqueta()



                # si los procesos logicos generaron etiquetas temporales de salida
                # para saltar al else
                traductor3d.addCadenaTemporal(traductor3d.getSaltosTemporales())
                traductor3d.clearSaltosTemporales()
                

                # revison si viene una else en la ejecucion
                if self.nodo != None:
                    cadenaTraduccion3d = ''
                    # salto para el else
                    etiquetaElse = traductor3d.getEtiqueta()
                    traductor3d.aumentarEtiqueta()
                    cadenaTraduccion3d += f'L{etiquetaElse}:\n'
                    traductor3d.addCadenaTemporal(cadenaTraduccion3d)

                    self.nodo.optimizar(envIf, traductor3d, cadena)

                
                # salida del todo si entra al if
                traductor3d.addCadenaTemporal(f'L{salidaIf}:\n')


                return None




            #  cuando la expresion sea false
            elif expresion3d.valor == '0':
                # cuando la expresion sea if salta donde mismo
                cadenaTraduccion3d += '\n'
                cadenaTraduccion3d += '\n'
                cadenaTraduccion3d += '/*------- IF -------- */\n'
                cadenaTraduccion3d += f'/*---- {expresion3d.valor} ---*/\n'
                etiquetaIf = traductor3d.getEtiqueta()
                cadenaTraduccion3d += f'goto L{etiquetaIf};\n'
                traductor3d.aumentarEtiqueta()
                
                # cadenaTraduccion3d += f'L{etiquetaIf}:\n'
                traductor3d.addSaltoTemporal(f'L{etiquetaIf}:\n')
            
                # TRADUCCION
                traductor3d.addCadenaTemporal(cadenaTraduccion3d)


                # generacion de las instrucciones del if
                for instruccion in self.instruccionesIF:
                    instruccion.optimizar(entorno, traductor3d, cadena)


                # salida del if si se llega a cumplir la condicionesw
                salidaIf = traductor3d.getEtiqueta()
                traductor3d.addCadenaTemporal(f'\n')
                traductor3d.addCadenaTemporal(f'\n')
                traductor3d.addCadenaTemporal(f'/*-- SALIDA DEL IF --*/\n')
                traductor3d.addCadenaTemporal(f'goto L{salidaIf};\n')
                traductor3d.aumentarEtiqueta()



                # si los procesos logicos generaron etiquetas temporales de salida
                # para saltar al else
                traductor3d.addCadenaTemporal(traductor3d.getSaltosTemporales())
                traductor3d.clearSaltosTemporales()
                

                # revison si viene una else en la ejecucion
                if self.nodo != None:
                    cadenaTraduccion3d = ''
                    # salto para el else
                    etiquetaElse = traductor3d.getEtiqueta()
                    traductor3d.aumentarEtiqueta()
                    cadenaTraduccion3d += f'L{etiquetaElse}:\n'
                    traductor3d.addCadenaTemporal(cadenaTraduccion3d)

                    # creacion de un nuevo entrono para el manejo de else y else if
                    numeroEntorno = entorno.numero + 1
                    envElse = Environment('ELSE/ELSE IF', numeroEntorno, entorno)

                    self.nodo.optimizar(envElse, traductor3d, cadena)

                
                # salida del todo si entra al if
                traductor3d.addCadenaTemporal(f'L{salidaIf}:\n')


                return None















        else:            
            cadenaTraduccion3d += '\n'
            cadenaTraduccion3d += '\n'
            cadenaTraduccion3d += traductor3d.getSaltoLogicoTrue()
            traductor3d.clearSaltoLogicoTrue()
            cadenaTraduccion3d += '/*------- IF -------- */\n'
            etiquetaIf = traductor3d.getEtiqueta()
            cadenaTraduccion3d += f'if ( {expresion3d.valor} ) goto L{etiquetaIf};\n'
            traductor3d.aumentarEtiqueta()

            # salto para el else
            etiquetaElse = traductor3d.getEtiqueta()
            cadenaTraduccion3d += f'goto L{etiquetaElse};\n'
            traductor3d.aumentarEtiqueta()


            # salto para ejecucion de las intrucciones del if
            cadenaTraduccion3d += f'L{etiquetaIf}:\n'
            traductor3d.addCadenaTemporal(cadenaTraduccion3d)
            # **********************************************



            #  traduce las instrucciones del if ---------
            # generacion de las instrucciones del if
            for instruccion in self.instruccionesIF:


                instruccion.optimizar(entorno, traductor3d, cadena)


                
                # saber si hay un break
                if isinstance(instruccion, Primitivo) and instruccion.tipo == TipoExpresion.BREAK:
                    cadena_break = ''
                    salto_break = traductor3d.getEtiqueta()
                    traductor3d.aumentarEtiqueta()

                    cadena_break += '\n'
                    cadena_break += '/*-- BREAK --*/\n'
                    cadena_break += f'goto L{salto_break};\n\n\n'
                    traductor3d.addCadenaTemporal(cadena_break)
                    traductor3d.addSaltoBreak(f'L{salto_break}:\n')


                # saber si hay un continue
                if isinstance(instruccion, Primitivo) and instruccion.tipo == TipoExpresion.CONTINUE:
                    cadena_continue = ''
                    salto_continue = traductor3d.getEtiqueta()
                    traductor3d.aumentarEtiqueta()

                    cadena_continue += '\n'
                    cadena_continue += '/*-- CONTINUE --*/\n'
                    cadena_continue += f'goto L{salto_continue};\n'
                    traductor3d.addSaltoContinue(f'L{salto_continue}:\n')
                    traductor3d.addCadenaTemporal(cadena_continue)

                




            
            # salida del if si se llega a cumplir la condicionesw
            salidaIf = traductor3d.getEtiqueta()
            traductor3d.addCadenaTemporal(f'goto L{salidaIf};\n')
            traductor3d.aumentarEtiqueta()




            # salto condicional para el else
            traductor3d.addCadenaTemporal(f'\n')
            traductor3d.addCadenaTemporal(f'\n')
            traductor3d.addCadenaTemporal(f'L{etiquetaElse}:\n')


            
            # si los procesos logicos generaron etiquetas temporales de salida
            # para saltar al else
            traductor3d.addCadenaTemporal(traductor3d.getSaltosTemporales())
            traductor3d.clearSaltosTemporales()



            # traduccion de las instrucciones del else
            traductor3d.addCadenaTemporal(f'\n')
            traductor3d.addCadenaTemporal(f'\n')
            traductor3d.addCadenaTemporal(f'\n')
            traductor3d.addCadenaTemporal(f'\n')
            traductor3d.addCadenaTemporal(f'/*-- ELSE --*/\n')

            if self.nodo != None:

                # traduccion de las instrucciones del else\
                self.nodo.optimizar(entorno, traductor3d, cadena)
                



            # salida del todo si entra al if
            traductor3d.addCadenaTemporal(f'L{salidaIf}:\n')


            

            return None