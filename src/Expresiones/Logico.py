from functools import cached_property
from src.Expresiones.Primitivo import Primitivo
from src.Interfaces.Expresion import Expresion
from src.Interfaces.TipoLogico import TipoLogico
from src.Interfaces.TipoExpresion import TipoExpresion
from src.Interfaces.TipoOperador import TipoOperador


# para manejo de la traduccion 3d
from src.environment.Simbolo3d import Simbolo3d



class Logico(Expresion):
    

    def __init__(self, fila, columna, leftExp, operador, rightExp):
        self.fila = fila 
        self.columna = columna
        self.leftExp = leftExp
        self.operador = operador
        self.rightExp = rightExp
        self.tipo = None


    def ejecutar(self, entorno):
        

        # evualicion de la compuert NOT
        if self.rightExp is None:

            # ejecutamos solo el nodo izquierdo
            nodoIzquierda = self.leftExp.ejecutar(entorno)

            if nodoIzquierda.tipo == TipoExpresion.ID:
                nodoIzquierda = entorno.getVariable(nodoIzquierda.valor)

            #  evaluacion del tipo de operacion not
            if self.operador == TipoLogico.NOT:

                if nodoIzquierda.valor == 'false':
                    return Primitivo(self.fila, self.columna, TipoExpresion.BOOL, 'true')
                

                elif nodoIzquierda.valor == 'true':
                    return Primitivo(self.fila, self.columna, TipoExpresion.BOOL, 'false')



        elif self.leftExp != None and self.rightExp != None: 

            # ejecutamos los nodos de derecha y izquierda
            nodoIzquierda = self.leftExp.ejecutar(entorno)
            nodoDerecha = self.rightExp.ejecutar(entorno)

            print(f'LOGICO --> {type(nodoIzquierda)}')
            print(f'LOGICO --> {self.operador}')
            print(f'LOGICO --> {nodoDerecha}')

            # evalucaion del tipo de operacion
            if self.operador == TipoLogico.OR:

                if nodoIzquierda.valor == 'false' and nodoDerecha.valor == 'false':
                    return Primitivo(self.fila, self.columna, TipoExpresion.BOOL, 'false')
                

                elif nodoIzquierda.valor == 'false' and nodoDerecha.valor == 'true':
                    return Primitivo(self.fila, self.columna, TipoExpresion.BOOL, 'true')


                elif nodoIzquierda.valor == 'true' and nodoDerecha.valor == 'false':
                    return Primitivo(self.fila, self.columna, TipoExpresion.BOOL, 'true')


                elif nodoIzquierda.valor == 'true' and nodoDerecha.valor == 'true':
                    return Primitivo(self.fila, self.columna, TipoExpresion.BOOL, 'true')



            #  evaluacion del tipo de operacion and
            elif self.operador == TipoLogico.AND:

                if nodoIzquierda.valor == 'false' and nodoDerecha.valor == 'false':
                    return Primitivo(self.fila, self.columna, TipoExpresion.BOOL, 'false')
                

                elif nodoIzquierda.valor == 'false' and nodoDerecha.valor == 'true':
                    return Primitivo(self.fila, self.columna, TipoExpresion.BOOL, 'false')

                elif nodoIzquierda.valor == 'true' and nodoDerecha.valor == 'false':
                    return Primitivo(self.fila, self.columna, TipoExpresion.BOOL, 'false')

                elif nodoIzquierda.valor == 'true' and nodoDerecha.valor == 'true':
                    return Primitivo(self.fila, self.columna, TipoExpresion.BOOL, 'true')



        # no se cumple con ninguna condicion
        else: 
            return None
















    # -------------------------------------------------------------------------
    #                   TRADUCCION DE LA PIRNTLN A 3D
    # -------------------------------------------------------------------------
    def traducir(self, entorno, traductor3d, cadena):
        
        cadenaTraduccion3d = ''



        # comprobacion si para la compuerta not
        if self.rightExp is None:

            if self.operador == TipoLogico.NOT:
                nodo = self.leftExp.traducir(entorno, traductor3d, cadena)

                # 1. que lo que queramos negar sea una variable
                if nodo.tipo == TipoExpresion.ID:
                    variable3d = entorno.getVariable3d(nodo.valor)

                    # cambio de valor
                    if variable3d.valor == '0':
                        variable3d.valor = '1'
                    elif variable3d.valor == '1':
                        variable3d.valor = '0'


                    entorno.addVariable3d(nodo.valor,variable3d)
                    return variable3d


                else:
                    if nodo.valor == '1':
                        nodo.valor = '0'
                    elif nodo.valor == '0':
                        nodo.valor = '1'
                    return nodo





        
        elif self.leftExp != None and self.rightExp != None: 

            # ejecutamos los nodos de derecha y izquierda
            nodoIzquierdo = self.leftExp.traducir(entorno, traductor3d, cadena)
            nodoDerecho = self.rightExp.traducir(entorno, traductor3d, cadena)

            
            if nodoDerecho.tipo == TipoExpresion.ID:
                nodoDerecho = entorno.getVariable3d(nodoDerecho.valor)

            if nodoIzquierdo.tipo == TipoExpresion.ID:
                nodoIzquierdo = entorno.getVariable3d(nodoIzquierdo.valor)








            # TRADUCCION PARA LA COMPUERTA OR
            if self.operador == TipoLogico.OR:


                
                # elementos para la compuerta OR
                temporal_respuesta = traductor3d.getTemporal()
                traductor3d.aumentarTemporal()


                # NODO IZQUIERDO
                etiquetaIf = traductor3d.getEtiqueta()
                traductor3d.aumentarEtiqueta()


                else_nodo_izquierdo = traductor3d.getEtiqueta()
                traductor3d.aumentarEtiqueta()


                salto_true_if = traductor3d.getEtiqueta()
                traductor3d.aumentarEtiqueta()


                cadenaTraduccion3d += '\n'
                cadenaTraduccion3d += '\n'
                cadenaTraduccion3d += '/*------ IF LOGICO -------*/\n'
                cadenaTraduccion3d += f'if ( {nodoIzquierdo.valor} ) goto L{etiquetaIf};\n'  
                cadenaTraduccion3d += f'goto L{else_nodo_izquierdo};\n'                

                cadenaTraduccion3d += f'L{etiquetaIf}:\n'
                cadenaTraduccion3d += f'    t{temporal_respuesta}=1;\n'
                cadenaTraduccion3d += f'    goto L{salto_true_if};\n'
                cadenaTraduccion3d += f'L{else_nodo_izquierdo}:\n'
                cadenaTraduccion3d += f'    t{temporal_respuesta}=0;\n'


                traductor3d.addSaltoLogicoTrue(f'L{salto_true_if}:\n')

                
                # NODO DERECHO
                etiquetaIf = traductor3d.getEtiqueta()
                traductor3d.aumentarEtiqueta()


                etiquetaElse = traductor3d.getEtiqueta()
                traductor3d.aumentarEtiqueta()


                salto_true_if = traductor3d.getEtiqueta()
                traductor3d.aumentarEtiqueta()


                cadenaTraduccion3d += '\n'
                cadenaTraduccion3d += '\n'
                cadenaTraduccion3d += '/*------ IF LOGICO -------*/\n'
                cadenaTraduccion3d += f'if ( {nodoDerecho.valor} ) goto L{etiquetaIf};\n'
                cadenaTraduccion3d += f'goto L{etiquetaElse};\n'

                cadenaTraduccion3d += f'L{etiquetaIf}:\n'
                cadenaTraduccion3d += f'    t{temporal_respuesta}=1;\n'
                cadenaTraduccion3d += f'    goto L{salto_true_if};\n'
                cadenaTraduccion3d += f'L{etiquetaElse}:\n'
                cadenaTraduccion3d += f'    t{temporal_respuesta}=0;\n'

                traductor3d.addSaltoLogicoTrue(f'L{salto_true_if}:\n')

                
                # se agrega a la traduccion general
                traductor3d.addCadenaTemporal(cadenaTraduccion3d)

                return Simbolo3d(
                    self.fila,
                    self.columna,
                    None,
                    TipoExpresion.BOOL,
                    f't{temporal_respuesta}',
                    None,
                    0,
                    0
                )













            # TRADUCCION PARA LA COMPUERTA AND
            elif self.operador == TipoLogico.AND:


                # PARA COMPUERTA AND

                # NODO IZQUIERDO
                etiquetaIf = traductor3d.getEtiqueta()
                traductor3d.aumentarEtiqueta()


                etiquetaElse = traductor3d.getEtiqueta()
                traductor3d.aumentarEtiqueta()

                temporal_respuesta = traductor3d.getTemporal()
                traductor3d.aumentarTemporal()


                cadenaTraduccion3d += '\n'
                cadenaTraduccion3d += '\n'
                cadenaTraduccion3d += '/*------ IF LOGICO -------*/\n'
                cadenaTraduccion3d += f'if ( {nodoIzquierdo.valor} ) goto L{etiquetaIf};\n'
                cadenaTraduccion3d += f'goto L{etiquetaElse};\n'
                cadenaTraduccion3d += f'L{etiquetaIf}:\n'
                cadenaTraduccion3d += f'    t{temporal_respuesta}=1;\n'

                # agrego etiqueta Salida temporalmente
                traductor3d.addSaltoTemporal(f'L{etiquetaElse}: \n')



                # NODO DERECHO
                if_nodo_derecho = traductor3d.getEtiqueta()
                traductor3d.aumentarEtiqueta()

                else_nodo_derecho = traductor3d.getEtiqueta()
                traductor3d.aumentarEtiqueta()


                cadenaTraduccion3d += '\n'
                cadenaTraduccion3d += '\n'
                cadenaTraduccion3d += '/*------ IF LOGICO -------*/\n'
                cadenaTraduccion3d += f'if ( {nodoDerecho.valor} ) goto  L{if_nodo_derecho};\n'
                cadenaTraduccion3d += f'goto L{else_nodo_derecho};\n'
                cadenaTraduccion3d += f'L{if_nodo_derecho}:\n'
                cadenaTraduccion3d += f'    t{temporal_respuesta}=1;\n'


                traductor3d.addSaltoTemporal(f'L{else_nodo_derecho}:\n')


                # se agrega a la traduccion general
                traductor3d.addCadenaTemporal(cadenaTraduccion3d)





                return Simbolo3d(
                    self.fila,
                    self.columna,
                    None,
                    TipoExpresion.BOOL,
                    f't{temporal_respuesta}',
                    None,
                    0,
                    0
                )














    # -------------------------------------------------------------------------
    #                   TRADUCCION DE LA PIRNTLN A 3D
    # -------------------------------------------------------------------------
    def optimizar(self, entorno, traductor3d, cadena):
        
        cadenaTraduccion3d = ''



        # comprobacion si para la compuerta not
        if self.rightExp is None:

            if self.operador == TipoLogico.NOT:
                nodo = self.leftExp.optimizar(entorno, traductor3d, cadena)

                # 1. que lo que queramos negar sea una variable
                if nodo.tipo == TipoExpresion.ID:
                    variable3d = entorno.getVariable3d(nodo.valor)

                    # cambio de valor
                    if variable3d.valor == '0':
                        variable3d.valor = '1'
                    elif variable3d.valor == '1':
                        variable3d.valor = '0'


                    entorno.addVariable3d(nodo.valor,variable3d)
                    return variable3d


                else:
                    if nodo.valor == '1':
                        nodo.valor = '0'
                    elif nodo.valor == '0':
                        nodo.valor = '1'
                    return nodo





        
        elif self.leftExp != None and self.rightExp != None: 

            # ejecutamos los nodos de derecha y izquierda
            nodoIzquierdo = self.leftExp.optimizar(entorno, traductor3d, cadena)
            nodoDerecho = self.rightExp.optimizar(entorno, traductor3d, cadena)

            
            if nodoDerecho.tipo == TipoExpresion.ID:
                nodoDerecho = entorno.getVariable3d(nodoDerecho.valor)

            if nodoIzquierdo.tipo == TipoExpresion.ID:
                nodoIzquierdo = entorno.getVariable3d(nodoIzquierdo.valor)








            # TRADUCCION PARA LA COMPUERTA OR
            if self.operador == TipoLogico.OR:


                
                # elementos para la compuerta OR
                temporal_respuesta = traductor3d.getTemporal()
                traductor3d.aumentarTemporal()


                # NODO IZQUIERDO
                etiquetaIf = traductor3d.getEtiqueta()
                traductor3d.aumentarEtiqueta()


                else_nodo_izquierdo = traductor3d.getEtiqueta()
                traductor3d.aumentarEtiqueta()


                salto_true_if = traductor3d.getEtiqueta()
                traductor3d.aumentarEtiqueta()


                cadenaTraduccion3d += '\n'
                cadenaTraduccion3d += '\n'
                cadenaTraduccion3d += '/*------ IF LOGICO -------*/\n'
                cadenaTraduccion3d += f'if ( {nodoIzquierdo.valor} ) goto L{etiquetaIf};\n'  
                cadenaTraduccion3d += f'goto L{else_nodo_izquierdo};\n'                

                cadenaTraduccion3d += f'L{etiquetaIf}:\n'
                cadenaTraduccion3d += f'    t{temporal_respuesta}=1;\n'
                cadenaTraduccion3d += f'    goto L{salto_true_if};\n'
                cadenaTraduccion3d += f'L{else_nodo_izquierdo}:\n'
                cadenaTraduccion3d += f'    t{temporal_respuesta}=0;\n'


                traductor3d.addSaltoLogicoTrue(f'L{salto_true_if}:\n')

                
                # NODO DERECHO
                etiquetaIf = traductor3d.getEtiqueta()
                traductor3d.aumentarEtiqueta()


                etiquetaElse = traductor3d.getEtiqueta()
                traductor3d.aumentarEtiqueta()


                salto_true_if = traductor3d.getEtiqueta()
                traductor3d.aumentarEtiqueta()


                cadenaTraduccion3d += '\n'
                cadenaTraduccion3d += '\n'
                cadenaTraduccion3d += '/*------ IF LOGICO -------*/\n'
                cadenaTraduccion3d += f'if ( {nodoDerecho.valor} ) goto L{etiquetaIf};\n'
                cadenaTraduccion3d += f'goto L{etiquetaElse};\n'

                cadenaTraduccion3d += f'L{etiquetaIf}:\n'
                cadenaTraduccion3d += f'    t{temporal_respuesta}=1;\n'
                cadenaTraduccion3d += f'    goto L{salto_true_if};\n'
                cadenaTraduccion3d += f'L{etiquetaElse}:\n'
                cadenaTraduccion3d += f'    t{temporal_respuesta}=0;\n'

                traductor3d.addSaltoLogicoTrue(f'L{salto_true_if}:\n')

                
                # se agrega a la traduccion general
                traductor3d.addCadenaTemporal(cadenaTraduccion3d)

                return Simbolo3d(
                    self.fila,
                    self.columna,
                    None,
                    TipoExpresion.BOOL,
                    f't{temporal_respuesta}',
                    None,
                    0,
                    0
                )













            # TRADUCCION PARA LA COMPUERTA AND
            elif self.operador == TipoLogico.AND:


                # PARA COMPUERTA AND

                # NODO IZQUIERDO
                etiquetaIf = traductor3d.getEtiqueta()
                traductor3d.aumentarEtiqueta()


                etiquetaElse = traductor3d.getEtiqueta()
                traductor3d.aumentarEtiqueta()

                temporal_respuesta = traductor3d.getTemporal()
                traductor3d.aumentarTemporal()


                cadenaTraduccion3d += '\n'
                cadenaTraduccion3d += '\n'
                cadenaTraduccion3d += '/*------ IF LOGICO -------*/\n'
                cadenaTraduccion3d += f'if ( {nodoIzquierdo.valor} ) goto L{etiquetaIf};\n'
                cadenaTraduccion3d += f'goto L{etiquetaElse};\n'
                cadenaTraduccion3d += f'L{etiquetaIf}:\n'
                cadenaTraduccion3d += f'    t{temporal_respuesta}=1;\n'

                # agrego etiqueta Salida temporalmente
                traductor3d.addSaltoTemporal(f'L{etiquetaElse}: \n')



                # NODO DERECHO
                if_nodo_derecho = traductor3d.getEtiqueta()
                traductor3d.aumentarEtiqueta()

                else_nodo_derecho = traductor3d.getEtiqueta()
                traductor3d.aumentarEtiqueta()


                cadenaTraduccion3d += '\n'
                cadenaTraduccion3d += '\n'
                cadenaTraduccion3d += '/*------ IF LOGICO -------*/\n'
                cadenaTraduccion3d += f'if ( {nodoDerecho.valor} ) goto  L{if_nodo_derecho};\n'
                cadenaTraduccion3d += f'goto L{else_nodo_derecho};\n'
                cadenaTraduccion3d += f'L{if_nodo_derecho}:\n'
                cadenaTraduccion3d += f'    t{temporal_respuesta}=1;\n'


                traductor3d.addSaltoTemporal(f'L{else_nodo_derecho}:\n')


                # se agrega a la traduccion general
                traductor3d.addCadenaTemporal(cadenaTraduccion3d)





                return Simbolo3d(
                    self.fila,
                    self.columna,
                    None,
                    TipoExpresion.BOOL,
                    f't{temporal_respuesta}',
                    None,
                    0,
                    0
                )

