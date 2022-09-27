
from turtle import right
from src.Expresiones.Primitivo import Primitivo
from src.Interfaces.Expresion import Expresion
from src.Interfaces.TipoOperador import TipoOperador
from src.Interfaces.TipoExpresion import TipoExpresion
from src.environment.Simbolo import Simbolo
from src.Error.Error import Error



from src.environment.Simbolo3d import Simbolo3d



# clase para manejar las sumas
class Aritmetica(Expresion):

    # constructor usando el constructor de la clase Nodo
    def __init__(self, fila, columna,lefExp, operador ,rigthExp):
        self.fila = fila 
        self.columna = columna
        self.leftExp = lefExp
        self.operador = operador
        self.rigthExp = rigthExp
        self.tipo = None
        # self.tablaErrores = tablaErrores

    def ejecutar(self, entorno):


        # ejecucion del nodod izquierda y derecha
        nodoIzquierda = self.leftExp.ejecutar(entorno)
        nodoDerecha = self.rigthExp.ejecutar(entorno)


        print(f'Aritmetica --> {nodoIzquierda.tipo}')
        print(f'Aritmetica --> {nodoDerecha}')

        

        # verificacion si algun nodod que sube es una variable para buscar su valoe en el entorno
        if nodoIzquierda.tipo == TipoExpresion.ID and nodoDerecha.tipo == TipoExpresion.ID:

            nodoIzquierda = entorno.getVariable(nodoIzquierda.valor)
            nodoDerecha = entorno.getVariable(nodoDerecha.valor)

        elif nodoIzquierda.tipo == TipoExpresion.ID and nodoDerecha.tipo != TipoExpresion.ID:

            nodoIzquierda = entorno.getVariable(nodoIzquierda.valor)

        elif nodoIzquierda.tipo != TipoExpresion.ID and nodoDerecha.tipo == TipoExpresion.ID:

            nodoDerecha = entorno.getVariable(nodoDerecha.valor)



        print(f'Aritmetica --> {nodoIzquierda.valor}')
        print(f'Aritmetica --> {nodoDerecha.tipo}')        
        
        
        
        
        
        # *************
        #  TIPOS DE ARREGLOS
        # ***********
        if nodoDerecha.tipo == TipoExpresion.ARREGLO:
            print('tipo de expresion arreglo')
            n = nodoDerecha.ejecutar(entorno)


        
        
        
        
        # ****************************************************************
        #  OPERACIONES ARITMECAS SOBRE LOS VALORES DE LOS NODOS     
        #  ****************************************************************

        # evalucacion de tipos de los primitivos
        if nodoIzquierda.tipo == nodoDerecha.tipo:


            # evaluacion de tipo valor --> INTEGER
            if nodoIzquierda.tipo == TipoExpresion.INTEGER:

                # suma
                if self.operador == TipoOperador.MAS:
                    result = nodoIzquierda.valor + nodoDerecha.valor
                    self.tipo = TipoExpresion.INTEGER
                    return Primitivo(self.fila, self.columna, TipoExpresion.INTEGER, int(result))

                # resta
                elif self.operador == TipoOperador.MENOS:
                    result = nodoIzquierda.valor - nodoDerecha.valor
                    self.tipo = TipoExpresion.INTEGER
                    return Primitivo(self.fila, self.columna, TipoExpresion.INTEGER, int(result))

                
                # multiplacion
                elif self.operador == TipoOperador.POR:
                    result = nodoIzquierda.valor * nodoDerecha.valor
                    self.tipo = TipoExpresion.INTEGER
                    return Primitivo(self.fila, self.columna, TipoExpresion.INTEGER, int(result))

                # division
                elif self.operador == TipoOperador.DIV:
                    result = nodoIzquierda.valor / nodoDerecha.valor
                    self.tipo = TipoExpresion.INTEGER
                    return Primitivo(self.fila, self.columna, TipoExpresion.INTEGER, int(result))

                # mod
                elif self.operador == TipoOperador.DIV:
                    result = nodoIzquierda.valor % nodoDerecha.valor
                    self.tipo = TipoExpresion.INTEGER
                    return Primitivo(self.fila, self.columna, TipoExpresion.INTEGER, int(result))


            # evaluacion de tipo de valor --> FLOAT
            if nodoIzquierda.tipo == TipoExpresion.FLOAT:

                # suma
                if self.operador == TipoOperador.MAS:
                    result = nodoIzquierda.valor + nodoDerecha.valor
                    self.tipo = TipoExpresion.FLOAT
                    return Primitivo(self.fila, self.columna, TipoExpresion.FLOAT, result)

                # resta
                elif self.operador == TipoOperador.MENOS:
                    result = nodoIzquierda.valor - nodoDerecha.valor
                    self.tipo = TipoExpresion.FLOAT
                    return Primitivo(self.fila, self.columna, TipoExpresion.FLOAT, result)

                
                # multiplacion
                elif self.operador == TipoOperador.POR:
                    result = nodoIzquierda.valor * nodoDerecha.valor
                    self.tipo = TipoExpresion.FLOAT
                    return Primitivo(self.fila, self.columna, TipoExpresion.FLOAT, result)

                # division
                elif self.operador == TipoOperador.DIV:
                    result = nodoIzquierda.valor / nodoDerecha.valor
                    self.tipo = TipoExpresion.FLOAT
                    return Primitivo(self.fila, self.columna, TipoExpresion.FLOAT, result)

                # mod
                elif self.operador == TipoOperador.DIV:
                    result = nodoIzquierda.valor % nodoDerecha.valor
                    self.tipo = TipoExpresion.FLOAT
                    return Primitivo(self.fila, self.columna, TipoExpresion.FLOAT, result)


            # evaluacion de tipo de valor --> FLOAT
            if nodoIzquierda.tipo == TipoExpresion.STRING:

                # suma
                if self.operador == TipoOperador.MAS:
                    result = nodoIzquierda.valor + nodoDerecha.valor
                    self.tipo = TipoExpresion.STRING
                    return Primitivo(self.fila, self.columna, TipoExpresion.STRING, result)





        # caso para tipos diferentes   
        else:
            # # para reportes
            # self.tablaErrores.append(['Aritmetica, Error operacion Aritmetica <-',entorno.nombre,self.fila,self.columna])
            # # --------------------------------
            return '--> Aritmetica, Error operacion Aritmetica <-'























    # -------------------------------------------------------------------------
    #                   TRADUCCION DE LA PIRNTLN A 3D
    # -------------------------------------------------------------------------
    def traducir(self, entorno, traductor3d, cadena):



        cadenaTraduccion3d = ''


        # ejecucion del nodod izquierda y derecha
        # OBTENER LOS VALORES
        # EJECUCION DEL NODO DERECHO Y DEL NODO IZQUIERDO
        nodoIzquierdo = self.leftExp.traducir(entorno, traductor3d, cadena)
        nodoDerecho = self.rigthExp.traducir(entorno, traductor3d, cadena)




        # VERIFICACION DE LOS NODOS SI SON TIPO ID Y HAY QUE BUSCARLOS EN EL STACK
        if nodoIzquierdo.tipo == TipoExpresion.ID and nodoDerecho.tipo == TipoExpresion.ID:

            nodoIzquierdo = entorno.getVariable3d(nodoIzquierdo.valor)
            nodoDerecho = entorno.getVariable3d(nodoDerecho.valor)


        # SI SOLO EL NODO IZQUIERDO ES UN ID
        elif nodoIzquierdo.tipo == TipoExpresion.ID and nodoDerecho.tipo != TipoExpresion.ID:

            nodoIzquierdo = entorno.getVariable3d(nodoIzquierdo.valor)


        # SI SOLO  EL NODO DERECHO ES UN ID
        elif nodoIzquierdo.tipo != TipoExpresion.ID and nodoDerecho.tipo == TipoExpresion.ID:

            temporal_derecho = traductor3d.getTemporal()
            traductor3d.aumentarTemporal()

            nodoDerecho = entorno.getVariable3d(nodoDerecho.valor)

            traductor3d.addCadenaTemporal('\n')
            traductor3d.addCadenaTemporal('\n')
            traductor3d.addCadenaTemporal(f't{temporal_derecho} = stack[(int) {nodoDerecho.posicion}];\n')
            nodoDerecho.valor = f't{temporal_derecho}'





        
        
        # verificaion de tipo del nodo derecha y nodo izquierda
        if nodoIzquierdo.tipo == nodoDerecho.tipo:

            # evaluacion de tipo valor --> INTEGER o FLOAT
            if nodoIzquierdo.tipo == TipoExpresion.INTEGER:

                # suma
                if self.operador == TipoOperador.MAS:

                    
                    # obteniendo valores de los nodos
                    resultadoNodoIzquierdo = nodoIzquierdo.valor
                    resultadoNodoDerecho = nodoDerecho.valor

                    # ********** traduccion **************
                    # obtengo el valor actual de los temporales
                    temporalActual = traductor3d.getTemporal()

                    cadenaTraduccion3d += f't{temporalActual} = {resultadoNodoIzquierdo} + {resultadoNodoDerecho} ;\n'
                    traductor3d.addCadenaTemporal(cadenaTraduccion3d)
                    traductor3d.aumentarTemporal()

                    return Simbolo3d(
                        self.fila,
                        self.columna,
                        None,
                        TipoExpresion.INTEGER,
                        f't{temporalActual}',
                        None,
                        0,
                        0
                    )
                    # *************************************


                # resta
                if self.operador == TipoOperador.MENOS:
                    # obteniendo valores de los nodos
                    resultadoNodoIzquierdo = nodoIzquierdo.valor
                    resultadoNodoDerecho = nodoDerecho.valor

                    # ********** traduccion **************
                    # obtengo el valor actual de los temporales
                    temporalActual = traductor3d.getTemporal()

                    cadenaTraduccion3d += f't{temporalActual} = {resultadoNodoIzquierdo} - {resultadoNodoDerecho} ;\n'
                    traductor3d.addCadenaTemporal(cadenaTraduccion3d)
                    traductor3d.aumentarTemporal()

                    return Simbolo3d(
                        self.fila,
                        self.columna,
                        None,
                        TipoExpresion.INTEGER,
                        f't{temporalActual}',
                        None,
                        0,
                        0
                    )
                    # *************************************



                # multiplicacion
                if self.operador == TipoOperador.POR:
                    # obteniendo valores de los nodos
                    resultadoNodoIzquierdo = nodoIzquierdo.valor
                    resultadoNodoDerecho = nodoDerecho.valor

                    # ********** traduccion **************
                    # obtengo el valor actual de los temporales
                    temporalActual = traductor3d.getTemporal()

                    cadenaTraduccion3d += f't{temporalActual} = {resultadoNodoIzquierdo} * {resultadoNodoDerecho} ;\n'
                    traductor3d.addCadenaTemporal(cadenaTraduccion3d)
                    traductor3d.aumentarTemporal()

                    return Simbolo3d(
                        self.fila,
                        self.columna,
                        None,
                        TipoExpresion.INTEGER,
                        f't{temporalActual}',
                        None,
                        0,
                        0
                    )
                    # *************************************



                # division
                if self.operador == TipoOperador.DIV:
                    # obteniendo valores de los nodos
                    resultadoNodoIzquierdo = nodoIzquierdo.valor
                    resultadoNodoDerecho = nodoDerecho.valor

                    # ********** traduccion **************
                    # obtengo el valor actual de los temporales
                    temporalActual = traductor3d.getTemporal()

                    cadenaTraduccion3d += f't{temporalActual} = {resultadoNodoIzquierdo} / {resultadoNodoDerecho} ;\n'
                    traductor3d.addCadenaTemporal(cadenaTraduccion3d)
                    traductor3d.aumentarTemporal()

                    return Simbolo3d(
                        self.fila,
                        self.columna,
                        None,
                        TipoExpresion.INTEGER,
                        f't{temporalActual}',
                        None,
                        0,
                        0
                    )
                    # *************************************




                # PORCENTAJE
                if self.operador == TipoOperador.PORCENTAJE:
                    # obteniendo valores de los nodos
                    resultadoNodoIzquierdo = nodoIzquierdo.valor
                    resultadoNodoDerecho = nodoDerecho.valor

                    # ********** traduccion **************
                    # obtengo el valor actual de los temporales
                    temporalActual = traductor3d.getTemporal()

                    cadenaTraduccion3d += f't{temporalActual} = {resultadoNodoIzquierdo} % {resultadoNodoDerecho} ;\n'
                    traductor3d.addCadenaTemporal(cadenaTraduccion3d)
                    traductor3d.aumentarTemporal()

                    return Simbolo3d(
                        self.fila,
                        self.columna,
                        None,
                        TipoExpresion.INTEGER,
                        f't{temporalActual}',
                        None,
                        0,
                        0
                    )
                    # *************************************






            # evaluacion de tipo valor --> FLOAT
            elif  nodoIzquierdo.tipo == TipoExpresion.FLOAT:

                # suma
                if self.operador == TipoOperador.MAS:

                    
                    # obteniendo valores de los nodos
                    resultadoNodoIzquierdo = nodoIzquierdo.valor
                    resultadoNodoDerecho = nodoDerecho.valor

                    # ********** traduccion **************
                    # obtengo el valor actual de los temporales
                    temporalActual = traductor3d.getTemporal()

                    cadenaTraduccion3d += f't{temporalActual} = {resultadoNodoIzquierdo} + {resultadoNodoDerecho} ;\n'
                    traductor3d.addCadenaTemporal(cadenaTraduccion3d)
                    traductor3d.aumentarTemporal()

                    return Simbolo3d(
                        self.fila,
                        self.columna,
                        None,
                        TipoExpresion.FLOAT,
                        f't{temporalActual}',
                        None,
                        0,
                        0
                    )
                    # *************************************


                # resta
                if self.operador == TipoOperador.MENOS:
                    # obteniendo valores de los nodos
                    resultadoNodoIzquierdo = nodoIzquierdo.valor
                    resultadoNodoDerecho = nodoDerecho.valor

                    # ********** traduccion **************
                    # obtengo el valor actual de los temporales
                    temporalActual = traductor3d.getTemporal()

                    cadenaTraduccion3d += f't{temporalActual} = {resultadoNodoIzquierdo} - {resultadoNodoDerecho} ;\n'
                    traductor3d.addCadenaTemporal(cadenaTraduccion3d)
                    traductor3d.aumentarTemporal()

                    return Simbolo3d(
                        self.fila,
                        self.columna,
                        None,
                        TipoExpresion.FLOAT,
                        f't{temporalActual}',
                        None,
                        0,
                        0
                    )
                    # *************************************



                # multiplicacion
                if self.operador == TipoOperador.POR:
                    # obteniendo valores de los nodos
                    resultadoNodoIzquierdo = nodoIzquierdo.valor
                    resultadoNodoDerecho = nodoDerecho.valor

                    # ********** traduccion **************
                    # obtengo el valor actual de los temporales
                    temporalActual = traductor3d.getTemporal()

                    cadenaTraduccion3d += f't{temporalActual} = {resultadoNodoIzquierdo} * {resultadoNodoDerecho} ;\n'
                    traductor3d.addCadenaTemporal(cadenaTraduccion3d)
                    traductor3d.aumentarTemporal()

                    return Simbolo3d(
                        self.fila,
                        self.columna,
                        None,
                        TipoExpresion.FLOAT,
                        f't{temporalActual}',
                        None,
                        0,
                        0
                    )
                    # *************************************



                # division
                if self.operador == TipoOperador.DIV:
                    # obteniendo valores de los nodos
                    resultadoNodoIzquierdo = nodoIzquierdo.valor
                    resultadoNodoDerecho = nodoDerecho.valor

                    # ********** traduccion **************
                    # obtengo el valor actual de los temporales
                    temporalActual = traductor3d.getTemporal()

                    cadenaTraduccion3d += f't{temporalActual} = {resultadoNodoIzquierdo} / {resultadoNodoDerecho} ;\n'
                    traductor3d.addCadenaTemporal(cadenaTraduccion3d)
                    traductor3d.aumentarTemporal()

                    return Simbolo3d(
                        self.fila,
                        self.columna,
                        None,
                        TipoExpresion.FLOAT,
                        f't{temporalActual}',
                        None,
                        0,
                        0
                    )
                    # *************************************



                # PORCENTAJE
                if self.operador == TipoOperador.PORCENTAJE:
                    # obteniendo valores de los nodos
                    resultadoNodoIzquierdo = nodoIzquierdo.valor
                    resultadoNodoDerecho = nodoDerecho.valor

                    # ********** traduccion **************
                    # obtengo el valor actual de los temporales
                    temporalActual = traductor3d.getTemporal()

                    cadenaTraduccion3d += f't{temporalActual} = {resultadoNodoIzquierdo} % {resultadoNodoDerecho} ;\n'
                    traductor3d.addCadenaTemporal(cadenaTraduccion3d)
                    traductor3d.aumentarTemporal()

                    return Simbolo3d(
                        self.fila,
                        self.columna,
                        None,
                        TipoExpresion.FLOAT,
                        f't{temporalActual}',
                        None,
                        0,
                        0
                    )
                    # *************************************










            # evaluacion de tipo valor --> STRING
            elif  nodoIzquierdo.tipo == TipoExpresion.STRING:
                cadena3d = ''

                # elementos necesario para concatenar
                
                # NODO IZQUIERDO 
                temporal_nodo_izquierdo = traductor3d.getTemporal()
                traductor3d.aumentarTemporal()
                temporal_posicion_izquierdo = traductor3d.getTemporal()
                traductor3d.aumentarTemporal()


                # NODO DERECHO
                temporal_nodo_derecho = traductor3d.getTemporal()
                traductor3d.aumentarTemporal()
                temporal_posicion_derecho = traductor3d.getTemporal()
                traductor3d.aumentarTemporal()


                temporal_contador = traductor3d.getTemporal()
                traductor3d.aumentarTemporal()


                temporal_recolector = traductor3d.getTemporal()
                traductor3d.aumentarTemporal()


                inicio_string = traductor3d.getHeap()
                traductor3d.aumentarHeap()



                # LARGO DE CADA UNO DE LOS ELEMENTOS
                tamanio_ambos = nodoIzquierdo.tamanio + nodoDerecho.tamanio
                print(f'----------------------------------------------------> {tamanio_ambos}')




                cadena3d += f'\n'
                cadena3d += f'\n'
                cadena3d += f'\n'
                cadena3d += f'/*---- CONCATENAR STRING ----*/\n'
                cadena3d += f'\n'
                cadena3d += f'//nodo Izquierdo\n'
                cadena3d += f't{temporal_nodo_izquierdo} = stack[(int) {nodoIzquierdo.posicion}];\n'
                cadena3d += f'\n'
                cadena3d += f'//TAMANIO DEL STRING\n'
                cadena3d += f't{temporal_posicion_izquierdo} = heap[(int) t{temporal_nodo_izquierdo}];\n'
                cadena3d += f'\n'
                cadena3d += f'//INICIO DEL STRING\n'
                cadena3d += f't{temporal_nodo_izquierdo} = t{temporal_nodo_izquierdo} + 1;\n'
                cadena3d += f'\n'


                cadena3d += f'\n'
                cadena3d += f'//nodo Derecho\n'
                cadena3d += f't{temporal_nodo_derecho} = stack[(int) {nodoDerecho.posicion}];\n'
                cadena3d += f'\n'
                cadena3d += f'//TAMANIO DEL STRING\n'
                cadena3d += f't{temporal_posicion_derecho} = heap[(int) t{temporal_nodo_derecho}];\n'
                cadena3d += f'\n'
                cadena3d += f'//INICIO DEL STRING\n'
                cadena3d += f't{temporal_nodo_derecho} = t{temporal_nodo_derecho} + 1;\n'
                cadena3d += f'\n'
                cadena3d += f'\n'
                cadena3d += f'\n'
                cadena3d += f'heap[(int) H] = {tamanio_ambos};\n'
                cadena3d += f'H = H + 1;\n'
                cadena3d += f'\n'
                cadena3d += f'\n'

                # for para colocar el primer string
                cadena3d += f'//PRIMERO NODO IZQUIERDO\n'
                cadena3d += f'\n'
                cadena3d += f'\n'
                cadena3d += f'//CONTADOR\n'
                cadena3d += f't{temporal_contador} = 0;\n'
                cadena3d += f'\n'
                cadena3d += f'concatString:\n'
                cadena3d += f'if ( t{temporal_contador} >= t{temporal_posicion_izquierdo} ) goto finConcatString;\n'
                cadena3d += f't{temporal_recolector} = heap[(int) t{temporal_nodo_izquierdo}];\n'
                cadena3d += f'heap[(int) H] = t{temporal_recolector};\n'
                cadena3d += f'H = H + 1;\n'
                traductor3d.aumentarHeap()
                cadena3d += f'\n'
                cadena3d += f't{temporal_contador} =  t{temporal_contador} + 1;\n'
                cadena3d += f'\n'
                cadena3d += f't{temporal_nodo_izquierdo} =  t{temporal_nodo_izquierdo} + 1;\n'
                cadena3d += f'\n'
                cadena3d += f'goto concatString;\n'
                cadena3d += f'\n'
                cadena3d += f'finConcatString:\n'
                cadena3d += f'\n'
                cadena3d += f'\n'
                cadena3d += f'\n'


                cadena3d += f'//SEGUNDO NODO DERECHO\n'
                cadena3d += f'\n'
                cadena3d += f'\n'
                cadena3d += f'//CONTADOR\n'
                cadena3d += f't{temporal_contador} = 0;\n'
                cadena3d += f'\n'
                cadena3d += f'concatString2:\n'
                cadena3d += f'if ( t{temporal_contador} >= t{temporal_posicion_derecho} ) goto finConcatString2;\n'
                cadena3d += f't{temporal_recolector} = heap[(int) t{temporal_nodo_derecho}];\n'
                cadena3d += f'heap[(int) H] = t{temporal_recolector};\n'
                cadena3d += f'H = H + 1;\n'
                traductor3d.aumentarHeap()
                cadena3d += f'\n'
                cadena3d += f't{temporal_contador} = t{temporal_contador} + 1;\n'
                cadena3d += f'\n'
                cadena3d += f't{temporal_nodo_derecho} = t{temporal_nodo_derecho} + 1;\n'
                cadena3d += f'\n'
                cadena3d += f'goto concatString2;\n'
                cadena3d += f'\n'
                cadena3d += f'finConcatString2:\n'
                cadena3d += f'\n'
                cadena3d += f'\n'



                # ************* TRADUCCION
                traductor3d.addCadenaTemporal(cadena3d)


                return Simbolo3d(
                        self.fila,
                        self.columna,
                        None,
                        TipoExpresion.STRING,
                        f'{inicio_string}',
                        None,
                        inicio_string,
                        tamanio_ambos
                    )