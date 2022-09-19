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
                    if variable3d.valor == 'false':
                        variable3d.valor = 'true'
                    elif variable3d.valor == 'true':
                        variable3d.valor = 'false'


                    entorno.addVariable3d(nodo.valor,variable3d)
                    return variable3d


                else:
                    if nodo.valor == 'true':
                        nodo.valor = 'false'
                    elif nodo.valor == 'false':
                        nodo.valor = 'true'
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




                if nodoIzquierdo.valor == 'true' or nodoIzquierdo.valor == 'false':
                    cadenaTraduccion3d += '\n'
                    cadenaTraduccion3d += '\n'                    
                    cadenaTraduccion3d += '\n'
                    cadenaTraduccion3d += '/*------- IF LOGICO-------- */\n'
                    cadenaTraduccion3d += f'/*--- {nodoIzquierdo.valor} ---*/\n'
                    etiquetaIf = traductor3d.getEtiqueta()
                    traductor3d.aumentarEtiqueta()
                    cadenaTraduccion3d += f'goto L{etiquetaIf};\n'
                    cadenaTraduccion3d += f'L{etiquetaIf}:\n'
                    traductor3d.addCadenaTemporal(cadenaTraduccion3d)


                    if nodoDerecho.tipo == TipoExpresion.BOOL or nodoIzquierdo.tipo == TipoExpresion.BOOL:
                    # si los procesos logicos generaron etiquetas temporales de salida
                    # para saltar al else
                        traductor3d.addCadenaTemporal(traductor3d.getSaltosTemporales())
                        traductor3d.clearSaltosTemporales()


                    return Simbolo3d(
                        self.fila,
                        self.columna,
                        None,
                        TipoExpresion.BOOL,
                        nodoDerecho.valor,
                        None,
                        0,
                        0
                    )







                cadenaTraduccion3d += '\n'
                cadenaTraduccion3d += '/*------ IF LOGICO -------*/\n'
                
                etiquetaIf = traductor3d.getEtiqueta()
                cadenaTraduccion3d += f'if ( {nodoIzquierdo.valor} ) goto L{etiquetaIf};\n'
                traductor3d.aumentarEtiqueta()

                etiquetaElse = traductor3d.getEtiqueta()
                cadenaTraduccion3d += f'goto L{etiquetaElse};\n'
                traductor3d.aumentarEtiqueta()

                cadenaTraduccion3d += f'L{etiquetaIf}:\n'

                # se agrega a la traduccion general
                traductor3d.addCadenaTemporal(cadenaTraduccion3d)


                # agrego etiqueta Salida temporalmente
                traductor3d.addSaltoTemporal(f'L{etiquetaElse}: \n')


                if nodoDerecho.tipo == TipoExpresion.BOOL or nodoIzquierdo.tipo == TipoExpresion.BOOL:
                    # si los procesos logicos generaron etiquetas temporales de salida
                    # para saltar al else
                    traductor3d.addCadenaTemporal(traductor3d.getSaltosTemporales())
                    traductor3d.clearSaltosTemporales()


                return Simbolo3d(
                    self.fila,
                    self.columna,
                    None,
                    TipoExpresion.BOOL,
                    nodoDerecho.valor,
                    None,
                    0,
                    0
                )











            # TRADUCCION PARA LA COMPUERTA AND
            elif self.operador == TipoLogico.AND:

                cadenaTraduccion3d += '\n'
                cadenaTraduccion3d += '/*------ IF LOGICO -------*/\n'
                
                etiquetaIf = traductor3d.getEtiqueta()
                cadenaTraduccion3d += f'if ( {nodoIzquierdo.valor} ) goto L{etiquetaIf};\n'
                traductor3d.aumentarEtiqueta()

                etiquetaElse = traductor3d.getEtiqueta()
                cadenaTraduccion3d += f'goto L{etiquetaElse};\n'
                traductor3d.aumentarEtiqueta()

                cadenaTraduccion3d += f'L{etiquetaIf}:\n'

                # se agrega a la traduccion general
                traductor3d.addCadenaTemporal(cadenaTraduccion3d)


                # agrego etiqueta Salida temporalmente
                traductor3d.addSaltoTemporal(f'L{etiquetaElse}: \n')


                if nodoDerecho.tipo == TipoExpresion.BOOL or nodoIzquierdo.tipo == TipoExpresion.BOOL:
                    # si los procesos logicos generaron etiquetas temporales de salida
                    # para saltar al else
                    # traductor3d.addCadenaTemporal(traductor3d.getSaltosTemporales())
                    # traductor3d.clearSaltosTemporales()
                    pass


                return Simbolo3d(
                    self.fila,
                    self.columna,
                    None,
                    TipoExpresion.BOOL,
                    nodoDerecho.valor,
                    None,
                    0,
                    0
                )


