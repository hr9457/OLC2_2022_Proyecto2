from src.Interfaces.Instruccion import Instruccion
from src.Interfaces.TipoExpresion import TipoExpresion
from src.environment.Simbolo import Simbolo
from src.Error.Error import Error
from src.Instrucciones.Struct.Struct import Struct
from src.Instrucciones.Arreglos.ExpArreglo import ExpArreglo
from src.Instrucciones.Arreglos.TipoArreglo import TipoArreglo


from src.environment.Simbolo3d import Simbolo3d


class Declaracion(Instruccion):

    # constructor
    def __init__(self, fila, columna, identificador, tipo, valor, mutabilidad, tablaSimbolos, tablaErrores):
        self.fila = fila
        self.columna = columna
        self.identificador = identificador
        self.tipo = tipo
        self.valor = valor
        self.mutabilidad = mutabilidad
        self.tablaSimbolos = tablaSimbolos
        self.tablaErrores = tablaErrores


    # metodo ejecutar
    def ejecutar(self, entorno):


        

        # verificacion de tipos
        # con tipo y el tipo del primitivo
        # esta linea altera el struct
        primitivo = self.valor.ejecutar(entorno)


        # variabel
        # TIPO == None  es una variable sin tipo
        # VARIABLES DONDE NO SE LE ESPECIFICA EL TIPO DE LA VARIABLE
        if self.tipo == None:

            print(f'DECLARACION: {primitivo.tipo}')
            print(f'DECLARACION: {self.valor}')


            if primitivo.tipo == TipoExpresion.STRUCT:

                value_struct = self.valor.ejecutar(entorno)
                value_struct.mutabilidad = self.mutabilidad
                entorno.addVariable(self.identificador,value_struct)

                # para reportes
                self.tablaSimbolos.append([self.identificador,'Variable',primitivo.tipo,entorno.nombre,self.fila,self.columna])
                # -------------


                return None



            elif primitivo.tipo == TipoExpresion.ARREGLO:

                # aca estantodo el listado de los elementos del arreglo
                # print(primitivo.listadoExpresiones)
                primitivo.mutabilidad = self.mutabilidad
                entorno.addVariable(self.identificador,primitivo)

                # para reportes
                self.tablaSimbolos.append([self.identificador,'Variable',primitivo.tipo,entorno.nombre,self.fila,self.columna])
                # -------------

                return None


            else:
                entorno.addVariable(self.identificador, 
                                    Simbolo(
                                        primitivo.fila, 
                                        primitivo.columna, 
                                        self.identificador, 
                                        primitivo.tipo, 
                                        primitivo.valor, 
                                        self.mutabilidad) )

                # para reportes
                self.tablaSimbolos.append([self.identificador,'Variable',primitivo.tipo,entorno.nombre,self.fila,self.columna])
                # -------------
                
                return None

        


        # la variable si tiene algun tipo
        elif self.tipo != None:


            # REVISION DE LOS TIPOS DE DATOS PAR ARREGLOS
            if isinstance(self.tipo,TipoArreglo):
                print('TIPO DE DECLARACION ES DE TIPO ARREGLO')
                type = self.tipo.ejecutar(entorno)

                if type.tipo == primitivo.tipo:
                    print('ARREGLO SON DEL MISMO TIPO')

                    primitivo.mutabilidad = self.mutabilidad
                    entorno.addVariable(self.identificador,
                                        Simbolo(
                                         primitivo.fila,
                                         primitivo.columna,
                                         self.identificador,
                                         primitivo.tipo,
                                         primitivo.listadoExpresiones,
                                         self.mutabilidad
                                        ))
                    # antes mandaba el primitivo Arreglo directo

                    # para reportes
                    self.tablaSimbolos.append([self.identificador,'Variable',primitivo.tipo,entorno.nombre,self.fila,self.columna])
                    # -------------

                    return None
                    




            if primitivo.tipo == TipoExpresion.ARREGLO:
                print('ARREGLO SON DEL MISMO TIPO')

                primitivo.mutabilidad = self.mutabilidad
                entorno.addVariable(self.identificador,
                                    Simbolo(
                                        primitivo.fila,
                                        primitivo.columna,
                                        self.identificador,
                                        primitivo.tipo,
                                        primitivo.listadoExpresiones,
                                        self.mutabilidad
                                    ))
                # antes mandaba el primitivo Arreglo directo

                # para reportes
                self.tablaSimbolos.append([self.identificador,'Variable',primitivo.tipo,entorno.nombre,self.fila,self.columna])
                # -------------

                return None


            elif primitivo.tipo == TipoExpresion.ID:
                getVariable = entorno.getVariable(primitivo.valor)
                print('------------')
                entorno.addVariable(self.identificador,
                                    Simbolo(
                                        getVariable.fila,
                                        getVariable.columna,
                                        getVariable.identificador,
                                        getVariable.tipo,
                                        getVariable.valor,
                                        getVariable.mutabilidad
                                    ))


            elif self.tipo == primitivo.tipo:

                entorno.addVariable(self.identificador, 
                                    Simbolo(primitivo.fila, 
                                    primitivo.columna, 
                                    self.identificador, 
                                    primitivo.tipo, 
                                    primitivo.valor, 
                                    self.mutabilidad) )


                # para reportes
                self.tablaSimbolos.append([self.identificador,'Variable',primitivo.tipo,entorno.nombre,self.fila,self.columna])
                # -------------

                return None


            elif primitivo.tipo == TipoExpresion.STRUCT:

                searchStruct = entorno.getStruct(self.tipo)

                if searchStruct is not None:

                    value_struct = self.valor.ejecutar(entorno)
                    value_struct.mutabilidad = self.mutabilidad
                    entorno.addVariable(self.identificador,value_struct)

                    # para reportes
                    self.tablaSimbolos.append([self.identificador,'Variable',primitivo.tipo,entorno.nombre,self.fila,self.columna])
                    # -------------

                    return None

                else:
                    # para reportes
                    self.tablaErrores.append([f'DECLARACION: Struct {self.tipo} no existe',entorno.nombre,self.fila,self.columna])
                    # --------------------------------
                    return f'DECLARACION: Struct {self.tipo} no existe'


            else: 
                # para reportes
                self.tablaErrores.append(['DECLARACION: error tipos no coinciden para declaracion de variables',entorno.nombre,self.fila,self.columna])
                # --------------------------------
                return 'DECLARACION: error tipos no coinciden para declaracion de variables'




        else:
            # para reportes
            self.tablaErrores.append(['DECLARACION: error tipos para declaracion de variables',entorno.nombre,self.fila,self.columna])
            # --------------------------------
            return 'DECLARACION: error tipos para declaracion de variables'




















    # -------------------------------------------------------------------------
    #                   TRADUCCION DE DECLARACIONES DE VARIABLES 3D
    # -------------------------------------------------------------------------

    # self.identificador = viene el identificador de la variable
    # self.valor = viene el simbolo para la variable
    def traducir(self, entorno, traductor3d, cadena):


        # traduccion a 3d
        cadenaTraduccion3d = ''


        # self.valor = valor de la variable
        # obtener el valor del simbolo para hacer la asginacion de la variable
        resultado = self.valor.traducir(entorno, traductor3d, cadena)



                

        
        # tipo del simbolo --> INTEGER o FLOAT
        # valores de un solo byte asignacion va al stack
        if resultado.tipo == TipoExpresion.INTEGER or resultado.tipo == TipoExpresion.FLOAT:
            cadenaTraduccion3d += '\n'
            cadenaTraduccion3d += '/*------ DECLARACION --------*/\n'
            cadenaTraduccion3d += f'stack[(int){traductor3d.getStack()}] = {resultado.valor};\n'
            # cadenaTraduccion3d += 'P = P + 1;\n'
            cadenaTraduccion3d += '\n'
            cadenaTraduccion3d += '\n'


            # agrega al entorno la variable
            resultado.posicion = traductor3d.getStack()
            traductor3d.aumentarStack()
            entorno.addVariable3d(self.identificador,resultado)
            


            # **********************************************
            #               TRADUCCION
            traductor3d.addCadenaTemporal(cadenaTraduccion3d)



        # menajeo de variables tipo --> CHAR
        elif resultado.tipo == TipoExpresion.CHAR:
            cadenaTraduccion3d += '\n'
            cadenaTraduccion3d += '/*------ DECLARACION --------*/\n'
            cadenaTraduccion3d += f'stack[(int){traductor3d.getStack()}] = {ord(resultado.valor)};\n'
            # cadenaTraduccion3d += 'P = P + 1;\n'
            cadenaTraduccion3d += '\n'
            cadenaTraduccion3d += '\n'


            # agrega al entorno la variable
            resultado.posicion = traductor3d.getStack()
            entorno.addVariable3d(self.identificador, resultado)
            traductor3d.aumentarStack()

            # **********************************************
            #               TRADUCCION               
            traductor3d.addCadenaTemporal(cadenaTraduccion3d)



        # menjo de variables tipo --> BOOL
        elif resultado.tipo == TipoExpresion.BOOL:
            if resultado.valor == '1':
                cadenaTraduccion3d += '\n'
                cadenaTraduccion3d += '/*------ DECLARACION --------*/\n'
                cadenaTraduccion3d += f'stack[(int){traductor3d.getStack()}] = 1;\n'
                # cadenaTraduccion3d += 'P = P + 1;\n'
                cadenaTraduccion3d += '\n'
                cadenaTraduccion3d += '\n'

                

                # agrega al entorno la variable
                resultado.posicion = traductor3d.getStack()
                entorno.addVariable3d(self.identificador, resultado)
                traductor3d.aumentarStack()


                # **********************************************
                #               TRADUCCION     
                traductor3d.addCadenaTemporal(cadenaTraduccion3d)

            elif resultado.valor == '0':
                cadenaTraduccion3d += '\n'
                cadenaTraduccion3d += '/*------ DECLARACION --------*/\n'
                cadenaTraduccion3d += f'stack[(int){traductor3d.getStack()}] = 0;\n'
                # cadenaTraduccion3d += 'P = P + 1;\n'
                cadenaTraduccion3d += '\n'
                cadenaTraduccion3d += '\n'


                
                # agrega al entorno la variable
                resultado.posicion = traductor3d.getStack()
                entorno.addVariable3d(self.identificador, resultado)
                traductor3d.aumentarStack()


                # **********************************************
                #               TRADUCCION     
                traductor3d.addCadenaTemporal(cadenaTraduccion3d)


        # menjo de variables tipo --> STRING
        elif resultado.tipo == TipoExpresion.STRING:
            cadenaTraduccion3d = ''
            # ************ traduccion ******************
            # guardo va iniciar el arreglo en el stack
            cadenaTraduccion3d += '\n'
            cadenaTraduccion3d += '/*--------- MOVIMIENTOS PARA UN STRING ------------*/\n'
            cadenaTraduccion3d += f'stack[(int){traductor3d.getStack()}] = H;\n'
            # cadenaTraduccion3d += 'P = P + 1;\n'
            cadenaTraduccion3d += '\n'
            posicionStackVariable = traductor3d.getStack()
            traductor3d.aumentarStack()

            # guardo el tambio del arreglo en la primera posicion del heap
            cadenaTraduccion3d += f'heap[(int)H] = {len(resultado.valor)};\n'
            cadenaTraduccion3d += 'H = H + 1;\n'
            traductor3d.aumentarHeap()


            # for para recorrer caracter a caracter el string
            for letra in resultado.valor:
                cadenaTraduccion3d += f'heap[(int)H] = {ord(letra)};\n'
                cadenaTraduccion3d += f'H = H + 1;\n'
                cadenaTraduccion3d += '\n'
                traductor3d.aumentarHeap()


            
            # agrega al entorno la variable
            resultado.posicion = posicionStackVariable
            resultado.tamanio = len(resultado.valor)
            entorno.addVariable3d(self.identificador, resultado)


            # **********************************************
            #               TRADUCCION     
            traductor3d.addCadenaTemporal(cadenaTraduccion3d)







        elif resultado.tipo == TipoExpresion.ARREGLO:
            cadenaTraduccion3d = ''

            posicion_stack = traductor3d.getStack()
            traductor3d.aumentarStack()

            temporal_stack = traductor3d.getTemporal()
            traductor3d.aumentarTemporal()

            # ************ traduccion ******************
            # guardo va iniciar el arreglo en el stack
            cadenaTraduccion3d += '\n'
            cadenaTraduccion3d += '/*--------- MOVIMIENTOS PARA UN ARREGLO ------------*/\n'
            cadenaTraduccion3d += f't{temporal_stack} = {posicion_stack};\n'
            cadenaTraduccion3d += f'stack[(int) t{temporal_stack}] = H;\n'
            cadenaTraduccion3d += f'\n'
            cadenaTraduccion3d += f'\n'
            cadenaTraduccion3d += f'\n'


            # tamanio del arreglo
            tamanio_arreglo = len(resultado.listadoExpresiones)

            cadenaTraduccion3d += f'heap[(int)H] = {tamanio_arreglo};\n'
            cadenaTraduccion3d += f'H = H + 1;\n'
            cadenaTraduccion3d += f'\n'
            cadenaTraduccion3d += f'\n'
            traductor3d.aumentarHeap()
            

            # for para recorrer todos los eelementos de un arreglo
            for elemento in resultado.listadoExpresiones:
                cadenaTraduccion3d += f'heap[(int) H] = {elemento.valor};\n'
                cadenaTraduccion3d += f'H = H + 1;\n'
                cadenaTraduccion3d += f'\n'
                traductor3d.aumentarHeap()

            cadenaTraduccion3d += f'\n'
            cadenaTraduccion3d += f'\n'

            # agregar la variable al entorno
            # contendio en un simbolo3d
            variable_arreglo = Simbolo3d(
                resultado.fila,
                resultado.columna,
                None,
                TipoExpresion.ARREGLO,
                resultado.listadoExpresiones,
                None,
                posicion_stack,
                tamanio_arreglo
            )


            # agrego variable al entorno
            entorno.addVariable3d(self.identificador, variable_arreglo)


            
            


            # **********************************************
            #               TRADUCCION     
            traductor3d.addCadenaTemporal(cadenaTraduccion3d)

        
        # --------------  para reportes -----------------------
        self.tablaSimbolos.append([self.identificador,'Variable',resultado.tipo,entorno.nombre,self.fila,self.columna])
        # --------------------------------------------




        return None
















    # -------------------------------------------------------------------------
    #                   TRADUCCION DE DECLARACIONES DE VARIABLES 3D
    # -------------------------------------------------------------------------

    # self.identificador = viene el identificador de la variable
    # self.valor = viene el simbolo para la variable
    def optimizar(self, entorno, traductor3d, cadena):


        # traduccion a 3d
        cadenaTraduccion3d = ''


        # self.valor = valor de la variable
        # obtener el valor del simbolo para hacer la asginacion de la variable
        resultado = self.valor.optimizar(entorno, traductor3d, cadena)
        

        
        # tipo del simbolo --> INTEGER o FLOAT
        # valores de un solo byte asignacion va al stack
        if resultado.tipo == TipoExpresion.INTEGER or resultado.tipo == TipoExpresion.FLOAT:
            cadenaTraduccion3d += '\n'
            cadenaTraduccion3d += '/*------ DECLARACION --------*/\n'
            cadenaTraduccion3d += f'stack[(int){traductor3d.getStack()}] = {resultado.valor};\n'
            # cadenaTraduccion3d += 'P = P + 1;\n'
            cadenaTraduccion3d += '\n'
            cadenaTraduccion3d += '\n'


            # agrega al entorno la variable
            resultado.posicion = traductor3d.getStack()
            traductor3d.aumentarStack()
            entorno.addVariable3d(self.identificador,resultado)
            


            # **********************************************
            #               TRADUCCION
            traductor3d.addCadenaTemporal(cadenaTraduccion3d)



        # menajeo de variables tipo --> CHAR
        elif resultado.tipo == TipoExpresion.CHAR:
            cadenaTraduccion3d += '\n'
            cadenaTraduccion3d += '/*------ DECLARACION --------*/\n'
            cadenaTraduccion3d += f'stack[(int){traductor3d.getStack()}] = {ord(resultado.valor)};\n'
            # cadenaTraduccion3d += 'P = P + 1;\n'
            cadenaTraduccion3d += '\n'
            cadenaTraduccion3d += '\n'


            # agrega al entorno la variable
            resultado.posicion = traductor3d.getStack()
            entorno.addVariable3d(self.identificador, resultado)
            traductor3d.aumentarStack()

            # **********************************************
            #               TRADUCCION               
            traductor3d.addCadenaTemporal(cadenaTraduccion3d)



        # menjo de variables tipo --> BOOL
        elif resultado.tipo == TipoExpresion.BOOL:
            if resultado.valor == '1':
                cadenaTraduccion3d += '\n'
                cadenaTraduccion3d += '/*------ DECLARACION --------*/\n'
                cadenaTraduccion3d += f'stack[(int){traductor3d.getStack()}] = 1;\n'
                # cadenaTraduccion3d += 'P = P + 1;\n'
                cadenaTraduccion3d += '\n'
                cadenaTraduccion3d += '\n'

                

                # agrega al entorno la variable
                resultado.posicion = traductor3d.getStack()
                entorno.addVariable3d(self.identificador, resultado)
                traductor3d.aumentarStack()


                # **********************************************
                #               TRADUCCION     
                traductor3d.addCadenaTemporal(cadenaTraduccion3d)

            elif resultado.valor == '0':
                cadenaTraduccion3d += '\n'
                cadenaTraduccion3d += '/*------ DECLARACION --------*/\n'
                cadenaTraduccion3d += f'stack[(int){traductor3d.getStack()}] = 0;\n'
                # cadenaTraduccion3d += 'P = P + 1;\n'
                cadenaTraduccion3d += '\n'
                cadenaTraduccion3d += '\n'


                
                # agrega al entorno la variable
                resultado.posicion = traductor3d.getStack()
                entorno.addVariable3d(self.identificador, resultado)
                traductor3d.aumentarStack()


                # **********************************************
                #               TRADUCCION     
                traductor3d.addCadenaTemporal(cadenaTraduccion3d)


        # menjo de variables tipo --> STRING
        elif resultado.tipo == TipoExpresion.STRING:
            cadenaTraduccion3d = ''
            # ************ traduccion ******************
            # guardo va iniciar el arreglo en el stack
            cadenaTraduccion3d += '\n'
            cadenaTraduccion3d += '/*--------- MOVIMIENTOS PARA UN STRING ------------*/\n'
            cadenaTraduccion3d += f'stack[(int){traductor3d.getStack()}] = H;\n'
            # cadenaTraduccion3d += 'P = P + 1;\n'
            cadenaTraduccion3d += '\n'
            posicionStackVariable = traductor3d.getStack()
            traductor3d.aumentarStack()

            # guardo el tambio del arreglo en la primera posicion del heap
            cadenaTraduccion3d += f'heap[(int)H] = {len(resultado.valor)};\n'
            cadenaTraduccion3d += 'H = H + 1;\n'
            traductor3d.aumentarHeap()


            # for para recorrer caracter a caracter el string
            for letra in resultado.valor:
                cadenaTraduccion3d += f'heap[(int)H] = {ord(letra)};\n'
                cadenaTraduccion3d += f'H = H + 1;\n'
                cadenaTraduccion3d += '\n'
                traductor3d.aumentarHeap()


            
            # agrega al entorno la variable
            resultado.posicion = posicionStackVariable
            resultado.tamanio = len(resultado.valor)
            entorno.addVariable3d(self.identificador, resultado)


            # **********************************************
            #               TRADUCCION     
            traductor3d.addCadenaTemporal(cadenaTraduccion3d)







        elif resultado.tipo == TipoExpresion.ARREGLO:
            cadenaTraduccion3d = ''

            posicion_stack = traductor3d.getStack()
            traductor3d.aumentarStack()

            temporal_stack = traductor3d.getTemporal()
            traductor3d.aumentarTemporal()

            # ************ traduccion ******************
            # guardo va iniciar el arreglo en el stack
            cadenaTraduccion3d += '\n'
            cadenaTraduccion3d += '/*--------- MOVIMIENTOS PARA UN ARREGLO ------------*/\n'
            cadenaTraduccion3d += f't{temporal_stack} = {posicion_stack};\n'
            cadenaTraduccion3d += f'stack[(int) t{temporal_stack}] = H;\n'
            cadenaTraduccion3d += f'\n'
            cadenaTraduccion3d += f'\n'
            cadenaTraduccion3d += f'\n'


            # tamanio del arreglo
            tamanio_arreglo = len(resultado.listadoExpresiones)

            cadenaTraduccion3d += f'heap[(int)H] = {tamanio_arreglo};\n'
            cadenaTraduccion3d += f'H = H + 1;\n'
            cadenaTraduccion3d += f'\n'
            cadenaTraduccion3d += f'\n'
            traductor3d.aumentarHeap()
            

            # for para recorrer todos los eelementos de un arreglo
            for elemento in resultado.listadoExpresiones:
                cadenaTraduccion3d += f'heap[(int) H] = {elemento.valor};\n'
                cadenaTraduccion3d += f'H = H + 1;\n'
                cadenaTraduccion3d += f'\n'
                traductor3d.aumentarHeap()

            cadenaTraduccion3d += f'\n'
            cadenaTraduccion3d += f'\n'

            # agregar la variable al entorno
            # contendio en un simbolo3d
            variable_arreglo = Simbolo3d(
                resultado.fila,
                resultado.columna,
                None,
                TipoExpresion.ARREGLO,
                resultado.listadoExpresiones,
                None,
                posicion_stack,
                tamanio_arreglo
            )


            # agrego variable al entorno
            entorno.addVariable3d(self.identificador, variable_arreglo)


            # **********************************************
            #               TRADUCCION     
            traductor3d.addCadenaTemporal(cadenaTraduccion3d)





        return None



