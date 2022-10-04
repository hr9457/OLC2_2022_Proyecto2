from unittest import result
from src.Interfaces.Instruccion import Instruccion
from src.environment.Environment import Environment
from src.Interfaces.TipoExpresion import TipoExpresion
from src.Error.Error import Error
from src.Expresiones.Primitivo import Primitivo
from src.Instrucciones.Funciones import GetFuncion
from src.Instrucciones.Struct.PrimateStruct import PrimateStruct
from src.environment.Simbolo import Simbolo


# clase para manejar la instruccion println 
class Imprimir(Instruccion):

    def __init__(self, contenido, lista=None):
        self.contenido = contenido
        self.lista = lista

    # metodo para ejecutar el imprimir
    def ejecutar(self, entorno):


        # primitivo
        variables = '{}'
        countNodoDerecho = 0 

        


        # ejecucion de los nodos que trae
        result = self.contenido.ejecutar(entorno)

        


        # nodo derecho
        if self.lista is not None:
            countNodoDerecho = len(self.lista)


        if isinstance(result, Error):
            # print('es una clase error')
            return result.ejecutar()


        else:

            tempLista = []
            # contar cuantos elementos trae el nodo derecho
            if countNodoDerecho >= 1 and countNodoDerecho == result.valor.count(variables):

                # print('cantidad de {} == cantidad de elementos en lista')

            

                for instruccion in self.lista:


                    # print(type(instruccion))
                    resultadoInstruccion = instruccion.ejecutar(entorno)

                    # viene errores
                    if isinstance(resultadoInstruccion, str):
                        tempLista.append(resultadoInstruccion)


                    elif resultadoInstruccion.tipo == TipoExpresion.VECTOR:
                        cadenaVector = '['
                        tempLista.append(self.imprimiVector(resultadoInstruccion.valor, cadenaVector, entorno))


                    else:

                        # tipo para impresiones sea variables
                        if resultadoInstruccion.tipo == TipoExpresion.ID:
                            result_evn = entorno.getVariable(resultadoInstruccion.valor)
                            print(result_evn)

                            if result_evn.tipo == TipoExpresion.ARREGLO and result_evn is not None:

                                cadenaArray = '['

                                tempLista.append(self.imprimirArreglo(result_evn, entorno, cadenaArray))


                            elif result_evn.tipo == TipoExpresion.VECTOR and result_evn is not None:

                                cadenaVector = '['
                                tempLista.append(self.imprimiVector(result_evn.lista,cadenaVector,entorno))


                            else:

                                tempLista.append(result_evn.valor)



                        # para cuando la imporesion sea una estructura
                        elif resultadoInstruccion.tipo == TipoExpresion.STRUCT:

                            var_struct = entorno.getVariable(resultadoInstruccion.identificador)

                            # buscar elemento el que se quiere imprimir
                            banderaStruct = False


                            for elemento in var_struct.elementos:

                                respuesta = elemento.ejecutar(entorno)

                                if respuesta.identificador == resultadoInstruccion.valor[0]:


                                    # print(respuesta.valor)
                                    # struct is struct
                                    # -----------------------------------------------------
                                    if isinstance(respuesta.valor,PrimateStruct):

                                        print('struct is struct')

                                        for elementSturct in respuesta.valor.elementos:
                                            elementSturct = elementSturct.ejecutar(entorno)
                                            print(elementSturct)

                                            if len(resultadoInstruccion.valor) >1:

                                                if elementSturct.identificador == resultadoInstruccion.valor[1]:
                                                    print(elementSturct.valor)
                                                    tempLista.append(elementSturct.valor)
                                                else:
                                                    tempLista.append(respuesta.valor)

                                            else:
                                                tempLista.append(respuesta.valor)
                                    # ---------------------------------------------------------


                                    # tiene que haber un proceso de struct is struct
                                    tempLista.append(respuesta.valor)
                                    banderaStruct= True


                            if banderaStruct == False:
                                return 'elemento en Struct no existe'




                        # impresiones de arreglos
                        elif resultadoInstruccion.tipo == TipoExpresion.ARREGLO:


                            concatenacionArreglo = '['
                            tempLista.append(self.imprimirArreglo(resultadoInstruccion,entorno, concatenacionArreglo))
                            concatenacionArreglo = ''

                        # elif result_evn.tipo == TipoExpresion.ARREGLO and result_evn is not None:
                        #
                        #     cadenaArray = '['
                        #
                        #     tempLista.append(self.imprimirArreglo(result_evn, entorno, cadenaArray))


                        # impresionsea valores primitivos
                        else:
                            tempLista.append(resultadoInstruccion.valor)




                print(tempLista)
                result.valor =  result.valor.format(*tempLista)
                return str(result.valor)+'\n'
            

            else:
                if result.tipo == TipoExpresion.ID:
                    result_env = entorno.getVariable(result.valor)
                    return str(result_env.valor) +'\n'

                else:
                    print(f'IMPRIMIR --> {result.tipo}')
                    print(f'IMPRIMIR --> {result.valor}')
                    return str(result.valor)+'\n'


                    




    # funcion para la impresion variables tipo arreglo
    def imprimirArreglo(self, arreglo, entorno, concatenacionArreglo):


        # concatenacionArreglo = '['


        if isinstance(arreglo, Simbolo):

            for v in arreglo.valor:

                if v.tipo != TipoExpresion.ARREGLO:
                    concatenacionArreglo += str(v.ejecutar(entorno).valor) + ', '

                else:
                    concatenacionArreglo += self.imprimirArreglo(v,entorno,concatenacionArreglo)

        else: 

            for v in arreglo.valor:

                if v.tipo != TipoExpresion.ARREGLO:
                    concatenacionArreglo += str(v.ejecutar(entorno).valor) + ', '
                else:
                    concatenacionArreglo += self.imprimirArreglo(v,entorno,concatenacionArreglo)


        concatenacionArreglo += ' ]'

        return concatenacionArreglo



    def imprimiVector(self, lista, cadenaVector, entorno):

        for elementoLista in lista:

            if elementoLista.tipo == TipoExpresion.VECTOR:
                cadenaVector += self.imprimiVector(elementoLista.lista, cadenaVector, entorno)


            else:
                elemento = elementoLista.ejecutar(entorno)

                cadenaVector += str(elemento.valor)

            cadenaVector += ','

        cadenaVector += ']'

        return cadenaVector





























    # -------------------------------------------------------------------------
    #                   TRADUCCION DE LA PIRNTLN A 3D
    # -------------------------------------------------------------------------
    # traduccion a 3d
    def traducir(self, entorno, traductor3d, cadena):
        # traduccion a 3d
        cadenaTraduccion3d = ''


        # si la impresion es simple 
        if self.lista == None:
            resultado = self.contenido.traducir(entorno, traductor3d, cadena)
            cadenaTraduccion3d += self.impresionSimple(resultado, entorno, traductor3d, cadena)
            cadenaTraduccion3d += '//SALTO DE LINEA\n'  
            cadenaTraduccion3d += 'printf("%c", (int)10);\n'
            cadenaTraduccion3d += '\n'
            cadenaTraduccion3d += '\n'
            cadenaTraduccion3d += '\n' 
            # *********************************************
            traductor3d.addCadenaTemporal(cadenaTraduccion3d)
            # *********************************************         


        # si la impresion es multiple o con {}
        else:           
            # si la impresion es simple 
            traductor3d.addCadenaTemporal(self.impresionMultiple(entorno, traductor3d, cadena))

        return None



















    # PARA EL MANEJO DE UNA EXPRESION SIMPLE
    def impresionSimple(self, resultado ,entorno, traductor3d, cadena):
        # traduccion a 3d
        cadenaTraduccion3d = ''
        # -------------------------------------------------------------------------
        #                 IMPRESION DE EXPRESIONES DE SIMBOLOS
        # -------------------------------------------------------------------------


        # obtener el contenido que va imprimir
        # tien que retornar un Simbolo
        # resultado = contenido.traducir(entorno, traductor3d)


        # impresion de expresiones tipo integer y tipo float
        if resultado.tipo == TipoExpresion.INTEGER:
            # ************ traduccion ******************
            cadenaTraduccion3d += self.imprimirInteger3d(resultado.valor)
            return cadenaTraduccion3d
            # ******************************************




        # impresion de expresiones tipo  float
        elif resultado.tipo == TipoExpresion.FLOAT:
            # ************ traduccion ******************
            cadenaTraduccion3d += self.imprimirFloat3d(resultado.valor)
            return cadenaTraduccion3d
            # ******************************************



        elif resultado.tipo == TipoExpresion.CHAR:
            # ************ traduccion ******************
            cadenaTraduccion3d += self.imprimirChar3d(resultado.valor)
            return cadenaTraduccion3d
            # ******************************************


        # impresion de expresiones tipo  booleanos
        elif resultado.tipo == TipoExpresion.BOOL:
            
            if resultado.valor == '1':
                # ************ traduccion ******************
                cadenaTraduccion3d += self.imprimirTrue3d()
                return cadenaTraduccion3d
                # ******************************************

            elif resultado.valor == '0':
                # ************ traduccion ******************
                cadenaTraduccion3d += self.imprimirFalse3d()
                return cadenaTraduccion3d
                # ******************************************



        # impiresion de expresiones tipo string
        elif resultado.tipo == TipoExpresion.STRING:

            # ************ traduccion ******************
            cadenaTraduccion3d += self.imprimirString3d(traductor3d, resultado.valor)
            return cadenaTraduccion3d              
            # ******************************************





        # -----------------------------------------------
        #           imppresion para variables
        # -----------------------------------------------
        elif resultado.tipo == TipoExpresion.ID:

            # buscar variables en el entorno 
            variable3d = entorno.getVariable3d(resultado.valor)
            

            # ************ traduccion ******************

            # variable es de tipo INTEGER
            if variable3d.tipo == TipoExpresion.INTEGER:
                temporalActual = traductor3d.getTemporal()
                # colocar posicion en una termporal
                cadenaTraduccion3d += '\n'
                cadenaTraduccion3d += '/*------ IMPRESION VARIABLE --------*/\n'
                cadenaTraduccion3d += f't{temporalActual} = {variable3d.posicion};\n'
                traductor3d.aumentarTemporal()

                # buscar el valor en esa possicion
                cadenaTraduccion3d += f't{temporalActual+1} = stack[(int) t{temporalActual}];\n'
                traductor3d.aumentarTemporal()
                cadenaTraduccion3d += self.imprimirInteger3d(f't{temporalActual+1}')


            # variable es de tipo FLOAT
            elif variable3d.tipo == TipoExpresion.FLOAT:
                temporalActual = traductor3d.getTemporal()
                # colocar posicion en una termporal
                cadenaTraduccion3d += '\n'
                cadenaTraduccion3d += '/*------ IMPRESION VARIABLE --------*/\n'
                cadenaTraduccion3d += f't{temporalActual} = {variable3d.posicion};\n'
                traductor3d.aumentarTemporal()

                # buscar el valor en esa possicion
                cadenaTraduccion3d += f't{temporalActual+1} = stack[(int) t{temporalActual}];\n'
                traductor3d.aumentarTemporal()
                cadenaTraduccion3d += self.imprimirFloat3d(f't{temporalActual+1}')




            elif variable3d.tipo == TipoExpresion.CHAR:
                temporalActual = traductor3d.getTemporal()
                # colocar posicion en una temporal
                cadenaTraduccion3d += '\n'
                cadenaTraduccion3d += '\n'
                cadenaTraduccion3d += '/*------- IMPRESION DE UNA VARIABLE -------*/\n'
                cadenaTraduccion3d += f't{temporalActual} = {variable3d.posicion};\n'
                traductor3d.aumentarTemporal()


                # buscar el valor en esa posicion
                cadenaTraduccion3d += f't{temporalActual+1} =  stack[(int) t{temporalActual}];\n'
                traductor3d.aumentarTemporal()
                cadenaTraduccion3d += self.imprimirChar3d(f't{temporalActual+1}')




            # variable es de tipo BOOL
            elif variable3d.tipo == TipoExpresion.BOOL:
                if variable3d.valor == '1':
                    # ************ traduccion ******************
                    cadenaTraduccion3d += self.imprimirTrue3d()
                    # ******************************************

                elif variable3d.valor == '0':
                    # ************ traduccion ******************
                    cadenaTraduccion3d += self.imprimirFalse3d()
                    # ******************************************            
            



            # variable es de tipo STRING
            elif variable3d.tipo == TipoExpresion.STRING:
                temporalActual = traductor3d.getTemporal()
                # colocar posicion de la variable en una temporal
                cadenaTraduccion3d += '\n'
                cadenaTraduccion3d += '/*------ IMPRESION VARIABLE --------*/\n'
                cadenaTraduccion3d += f't{temporalActual} = {variable3d.posicion};\n'
                traductor3d.aumentarTemporal()

                # obtengo la possicion en el heap donde esta esta el string
                temporalActual = traductor3d.getTemporal()
                cadenaTraduccion3d += f't{temporalActual} = stack[(int) t{temporalActual-1}];\n'
                

                # posiciono en el heap segun el temporal
                # primera posicion me dice cual es el tamanio del arreglo -> t0
                # segunda posicion es donde inicial el arreglo -> t2
                cadenaTraduccion3d += f't0 = heap[(int)t{temporalActual}];\n'
                cadenaTraduccion3d += f't2 = t{temporalActual} + 1;\n'

                traductor3d.aumentarTemporal()
                cadenaTraduccion3d += '\n'
                cadenaTraduccion3d += '/*--------- IMPRESION DE UN STRING -----------*/\n'
                cadenaTraduccion3d += 'printString();\n'
                cadenaTraduccion3d += '\n'  
                cadenaTraduccion3d += 'printf("%c", (int)10);\n'  
            


            # *********************************************
            return cadenaTraduccion3d
            # *********************************************















    # PARA MENEJO DE IMPRESIONES MULTIPLES EN 3D
    # LISTADO DE EXPRESIONES
    def impresionMultiple(self, entorno, traductor3d, cadena):
        # primitivo
        countNodoDerecho = 0
        # traduccion a 3d
        cadenaTraduccion3d = ''
        # -------------------------------------------------------------------------
        #                 IMPRESION DE EXPRESIONES DE SIMBOLOS
        # -------------------------------------------------------------------------


        # obtener el contenido que va imprimir
        # tien que retornar un Simbolo
        resultado = self.contenido.traducir(entorno, traductor3d, cadena)


        # impiresion de expresiones tipo string
        if resultado.tipo == TipoExpresion.STRING:
            # haciendo split de la cadena


            llaves_iniciales = 0
            cantidad_llaves = resultado.valor.count('{}')

            stringDividido = resultado.valor.split('{}')
            
            # stringDividido.pop()


            for elementoString in stringDividido:
                # ************ traduccion ******************
                # guardo va iniciar el arreglo en el stack
                cadenaTraduccion3d += '\n'
                cadenaTraduccion3d += '/*--------- MOVIMIENTOS PARA UN STRING ------------*/\n'
                cadenaTraduccion3d += f'stack[(int){traductor3d.getStack()}] = H;\n'
                # cadenaTraduccion3d += 'P = P + 1;\n'
                traductor3d.aumentarStack()


                # guardo el tambio del arreglo en la primera posicion del heap
                cadenaTraduccion3d += f'heap[(int)H] = {len(elementoString)};\n'
                cadenaTraduccion3d += 'H = H + 1;\n'
                traductor3d.aumentarHeap()


                # guardo el tamanio del arreglo en t0
                cadenaTraduccion3d += f't0 = {len(elementoString)};\n'

                # guardo donde inicio el arreglo
                cadenaTraduccion3d += f't2 = H;\n'


                # for para todo el string
                # for para recorrer caracter a caracter el string
                for letra in elementoString:
                    cadenaTraduccion3d += f'heap[(int)H] = {ord(letra)};\n'
                    cadenaTraduccion3d += f'H = H + 1;\n'
                    traductor3d.aumentarHeap()


                cadenaTraduccion3d += '\n'
                cadenaTraduccion3d += '/*--------- IMPRESION DE UN STRING -----------*/\n'
                cadenaTraduccion3d += 'printString();\n'
                cadenaTraduccion3d += '\n' 


                # IMPRIMIR LA EXPRESION DESPUES DEL {}
                if llaves_iniciales < cantidad_llaves:
                    expresion = self.lista[countNodoDerecho]
                    expresion3d = expresion.traducir(entorno, traductor3d, cadena)
                    countNodoDerecho += 1
                    llaves_iniciales += 1
                

                    # IMPRESION DE LA EXPRESION SIMPLE
                    cadenaTraduccion3d += self.impresionSimple(expresion3d, entorno, traductor3d, cadena)

            cadenaTraduccion3d += '\n'
            cadenaTraduccion3d += '//SALTO DE LINEA\n'  
            cadenaTraduccion3d += 'printf("%c", (int)10);\n'        

        # *********************************************
        return cadenaTraduccion3d
        # *********************************************



    














    # ----------------------------------------------------------------
    #             MANEJO DE DIFERENTES TIPO DE  IMPRESIONES
    # ----------------------------------------------------------------

    # metodo para hacer impresiones de valores enteros
    def imprimirInteger3d(self, resultado):
        cadenaTraduccion3d = ''
        # ************ traduccion ******************
        cadenaTraduccion3d += '\n'
        cadenaTraduccion3d += '/*--------- PRINT ------------*/\n'
        cadenaTraduccion3d += f'printf("%d", (int){resultado}); \n'
        cadenaTraduccion3d += '\n'
        cadenaTraduccion3d += '\n'
        cadenaTraduccion3d += '\n'
        # cadenaTraduccion3d += 'printf("%c", (int)10);\n'
        return cadenaTraduccion3d
        # ******************************************



    # metodo para hacer impresion de valores float
    def imprimirFloat3d(self, resultado):
        cadenaTraduccion3d = ''
        # ************ traduccion ******************
        cadenaTraduccion3d += '\n'
        cadenaTraduccion3d += '/*--------- PRINT ------------*/\n'
        cadenaTraduccion3d += f'printf("%f", {resultado}); \n'
        cadenaTraduccion3d += '\n'
        cadenaTraduccion3d += '\n'
        cadenaTraduccion3d += '\n'
        # cadenaTraduccion3d += 'printf("%c", (int)10);\n'
        return cadenaTraduccion3d
        # ******************************************



    # metodo para hacer impresion de un valro char
    def imprimirChar3d(self, resultado):
        cadenaTraduccion3d = ''
        # ************ traduccion ******************
        cadenaTraduccion3d += '\n'
        cadenaTraduccion3d += '/*--------- PRINT ------------*/\n'
        cadenaTraduccion3d += f'printf("%c", (int){resultado}); \n'
        cadenaTraduccion3d += '\n'
        cadenaTraduccion3d += '\n'
        cadenaTraduccion3d += '\n'
        # cadenaTraduccion3d += 'printf("%c", (int)10);\n'
        return cadenaTraduccion3d
        # ******************************************



    def imprimirTrue3d(self):
        cadenaTraduccion3d = ''
        # ************ traduccion ******************
        cadenaTraduccion3d += '\n'
        cadenaTraduccion3d += '/*--------- PRINT ------------*/\n'
        cadenaTraduccion3d += 'printf("%c", (int)116);\n'
        cadenaTraduccion3d += 'printf("%c", (int)114);\n'
        cadenaTraduccion3d += 'printf("%c", (int)117);\n'
        cadenaTraduccion3d += 'printf("%c", (int)101);\n'
        cadenaTraduccion3d += '\n'
        cadenaTraduccion3d += '\n'
        cadenaTraduccion3d += '\n'
        return cadenaTraduccion3d
        # ******************************************


    def imprimirFalse3d(self):
        cadenaTraduccion3d = ''
        # ************ traduccion ******************
        cadenaTraduccion3d += '\n'
        cadenaTraduccion3d += '/*--------- PRINT ------------*/\n'
        cadenaTraduccion3d += 'printf("%c", (int)102);\n'
        cadenaTraduccion3d += 'printf("%c", (int)97);\n'
        cadenaTraduccion3d += 'printf("%c", (int)108);\n'
        cadenaTraduccion3d += 'printf("%c", (int)115);\n'
        cadenaTraduccion3d += 'printf("%c", (int)101);\n'
        cadenaTraduccion3d += 'printf("%c", (int)10);\n'
        cadenaTraduccion3d += 'printf("%c", (int)13);\n'
        cadenaTraduccion3d += '\n'
        cadenaTraduccion3d += '\n'
        cadenaTraduccion3d += '\n'
        return cadenaTraduccion3d
        # ******************************************



    def imprimirString3d(self, traductor3d, resultado):
        cadenaTraduccion3d = ''
        # ************ traduccion ******************
        # guardo va iniciar el arreglo en el stack
        cadenaTraduccion3d += '\n'
        cadenaTraduccion3d += '/*--------- MOVIMIENTOS PARA UN STRING ------------*/\n'
        cadenaTraduccion3d += f'stack[(int){traductor3d.getStack()}] = H;\n'
        # cadenaTraduccion3d += 'P = P + 1;\n'
        traductor3d.aumentarStack()


        # guardo el tambio del arreglo en la primera posicion del heap
        cadenaTraduccion3d += f'heap[(int)H] = {len(resultado)};\n'
        cadenaTraduccion3d += 'H = H + 1;\n'
        traductor3d.aumentarHeap()


        # guardo el tamanio del arreglo en t0
        cadenaTraduccion3d += f't0 = {len(resultado)};\n'

        # guardo donde inicio el arreglo
        cadenaTraduccion3d += f't2 = H;\n'

        # for para recorrer caracter a caracter el string
        for letra in resultado:
            cadenaTraduccion3d += f'heap[(int)H] = {ord(letra)};\n'
            cadenaTraduccion3d += f'H = H + 1;\n'
            traductor3d.aumentarHeap()


        cadenaTraduccion3d += '\n'
        cadenaTraduccion3d += '/*--------- IMPRESION DE UN STRING -----------*/\n'
        cadenaTraduccion3d += 'printString();\n'
        cadenaTraduccion3d += '\n'
        cadenaTraduccion3d += '\n'
        cadenaTraduccion3d += '\n'
        # cadenaTraduccion3d += '//SALTO DE LINEA'  
        # cadenaTraduccion3d += 'printf("%c", (int)10);\n'

        return cadenaTraduccion3d           
        # ******************************************