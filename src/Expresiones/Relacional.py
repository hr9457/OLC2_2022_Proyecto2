from src.Interfaces.Expresion import Expresion
from src.Interfaces.TipoExpresion import TipoExpresion
from src.Interfaces.TipoRelacional import TipoRelacional

from src.Expresiones.Primitivo import Primitivo
from src.Interfaces.TipoExpresion import TipoExpresion

from src.Error.Error import Error



# manejo del 3d
from src.environment.Simbolo3d import Simbolo3d



class Relacional(Expresion):


    def __init__(self, fila, columna,leftExp, operador, rightExp):
        self.fila = fila
        self.columna = columna
        self.leftExp = leftExp
        self.operador = operador
        self.rightExp = rightExp
        self.tipo = None
        # self.tablaErorres = tablaErorres


    def ejecutar(self, entorno):

        # ejecutamos nodos derecha y izquierda
        nodoIzquierda = self.leftExp.ejecutar(entorno)
        nodoDerecha = self.rightExp.ejecutar(entorno)


        print(f'RELACIONAL --> {nodoIzquierda}')
        print(f'RELACIONAL --> {self.operador}')
        print(f'RELACIONAL --> {type(nodoDerecha)}')
        


        # verificacion si algun nodod que sube es una variable para buscar su valoe en el entorno
        if nodoIzquierda.tipo == TipoExpresion.ID and nodoDerecha.tipo == TipoExpresion.ID:

            nodoIzquierda = entorno.getVariable(nodoIzquierda.valor)
            nodoDerecha = entorno.getVariable(nodoDerecha.valor)

        elif nodoIzquierda.tipo == TipoExpresion.ID and nodoDerecha.tipo != TipoExpresion.ID:

            nodoIzquierda = entorno.getVariable(nodoIzquierda.valor)

        elif nodoIzquierda.tipo != TipoExpresion.ID and nodoDerecha.tipo == TipoExpresion.ID:

            nodoDerecha = entorno.getVariable(nodoDerecha.valor)



       

        # evalucacion de tipos de los primitivos
        if nodoIzquierda.tipo == nodoDerecha.tipo:

            
            # evalucaion de tipo valor --> INTEGER
            if nodoIzquierda.tipo == TipoExpresion.INTEGER:


                # evaluacion del mayor que 
                if self.operador == TipoRelacional.MAYORQUE:
                    
                    if nodoIzquierda.valor > nodoDerecha.valor:
                        return Primitivo(0, 0, TipoExpresion.BOOL, 'true')
                        # return True
                    else:
                        return Primitivo(0, 0, TipoExpresion.BOOL, 'false')
                        # return False

                
                # evaluacion del menor que
                if self.operador == TipoRelacional.MENORQUE:

                    if nodoIzquierda.valor < nodoDerecha.valor:
                        return Primitivo(0, 0, TipoExpresion.BOOL, 'true')
                    else:
                        return Primitivo(0, 0, TipoExpresion.BOOL, 'false')


                # evalucacion del mayor igual que
                if self.operador == TipoRelacional.MAYORIGUALQUE:

                    if nodoIzquierda.valor >= nodoDerecha.valor:
                        return Primitivo(0, 0, TipoExpresion.BOOL, 'true')
                    else:
                        return Primitivo(0, 0, TipoExpresion.BOOL, 'false')

                # evaluacion del menor igual que
                if self.operador == TipoRelacional.MENORIGUALQUE:

                    if nodoIzquierda.valor <= nodoDerecha.valor:
                        return Primitivo(0, 0, TipoExpresion.BOOL, 'true')
                    else:
                        return Primitivo(0, 0, TipoExpresion.BOOL, 'false')

                
                # evalucacion de la igual 
                if self.operador == TipoRelacional.IGUALDAD:

                    if nodoIzquierda.valor == nodoDerecha.valor:
                        return Primitivo(0, 0, TipoExpresion.BOOL, 'true')
                    else:
                        return Primitivo(0, 0, TipoExpresion.BOOL, 'false')


                # evalucacion de la diferentes
                if self.operador == TipoRelacional.DIFERENTE:

                    if nodoIzquierda.valor != nodoDerecha.valor:
                        return Primitivo(0, 0, TipoExpresion.BOOL, 'true')
                    else:
                        return Primitivo(0, 0, TipoExpresion.BOOL, 'false')


            
            # evalucaion de tipo valor --> FLOAT
            if nodoIzquierda.tipo == TipoExpresion.FLOAT:


                # evaluacion del mayor que 
                if self.operador == TipoRelacional.MAYORQUE:
                    
                    if nodoIzquierda.valor > nodoDerecha.valor:
                        return Primitivo(0, 0, TipoExpresion.BOOL, 'true')
                    else:
                        return Primitivo(0, 0, TipoExpresion.BOOL, 'false')

                
                # evaluacion del menor que
                if self.operador == TipoRelacional.MENORQUE:

                    if nodoIzquierda.valor < nodoDerecha.valor:
                        return Primitivo(0, 0, TipoExpresion.BOOL, 'true')
                    else:
                        return Primitivo(0, 0, TipoExpresion.BOOL, 'false')


                # evalucacion del mayor igual que
                if self.operador == TipoRelacional.MAYORIGUALQUE:

                    if nodoIzquierda.valor >= nodoDerecha.valor:
                        return Primitivo(0, 0, TipoExpresion.BOOL, 'true')
                    else:
                        return Primitivo(0, 0, TipoExpresion.BOOL, 'false')

                # evaluacion del menor igual que
                if self.operador == TipoRelacional.MENORIGUALQUE:

                    if nodoIzquierda.valor <= nodoDerecha.valor:
                        return Primitivo(0, 0, TipoExpresion.BOOL, 'true')
                    else:
                        return Primitivo(0, 0, TipoExpresion.BOOL, 'false')

                
                # evalucacion de la igual 
                if self.operador == TipoRelacional.IGUALDAD:

                    if nodoIzquierda.valor == nodoDerecha.valor:
                        return Primitivo(0, 0, TipoExpresion.BOOL, 'true')
                    else:
                        return Primitivo(0, 0, TipoExpresion.BOOL, 'false')



                # evalucacion de la diferentes 
                if self.operador == TipoRelacional.DIFERENTE:

                    if nodoIzquierda.valor != nodoDerecha.valor:
                        return Primitivo(0, 0, TipoExpresion.BOOL, 'true')
                    else:
                        return Primitivo(0, 0, TipoExpresion.BOOL, 'false')





            # evalucaion de tipo valor --> FLOAT
            if nodoIzquierda.tipo == TipoExpresion.STRING:
                # evaluacion del mayor que 
                if self.operador == TipoRelacional.MAYORQUE:
                    
                    if nodoIzquierda.valor > nodoDerecha.valor:
                        return Primitivo(0, 0, TipoExpresion.BOOL, 'true')
                    else:
                        return Primitivo(0, 0, TipoExpresion.BOOL, 'false')

                
                # evaluacion del menor que
                if self.operador == TipoRelacional.MENORQUE:

                    if nodoIzquierda.valor < nodoDerecha.valor:
                        return Primitivo(0, 0, TipoExpresion.BOOL, 'true')
                    else:
                        return Primitivo(0, 0, TipoExpresion.BOOL, 'false')


                # evalucacion del mayor igual que
                if self.operador == TipoRelacional.MAYORIGUALQUE:

                    if nodoIzquierda.valor >= nodoDerecha.valor:
                        return Primitivo(0, 0, TipoExpresion.BOOL, 'true')
                    else:
                        return Primitivo(0, 0, TipoExpresion.BOOL, 'false')

                # evaluacion del menor igual que
                if self.operador == TipoRelacional.MENORIGUALQUE:

                    if nodoIzquierda.valor <= nodoDerecha.valor:
                        return Primitivo(0, 0, TipoExpresion.BOOL, 'true')
                    else:
                        return Primitivo(0, 0, TipoExpresion.BOOL, 'false')

                
                # evalucacion de la igual 
                if self.operador == TipoRelacional.IGUALDAD:

                    if nodoIzquierda.valor == nodoDerecha.valor:
                        return Primitivo(0, 0, TipoExpresion.BOOL, 'true')
                    else:
                        return Primitivo(0, 0, TipoExpresion.BOOL, 'false')



                # evalucacion de la diferentes
                if self.operador == TipoRelacional.DIFERENTE:

                    if nodoIzquierda.valor != nodoDerecha.valor:
                        return Primitivo(0, 0, TipoExpresion.BOOL, 'true')
                    else:
                        return Primitivo(0, 0, TipoExpresion.BOOL, 'false')

                


        else:
            # # para reportes
            # self.tablaErrores.append(['RELACIONAL: Error operador relacional',entorno.nombre,self.fila,self.columna])
            # # --------------------------------
            return Error('RELACIONAL: Error operador relacional')






















    # -------------------------------------------------------------------------
    #                   TRADUCCION DE LA PIRNTLN A 3D
    # -------------------------------------------------------------------------
    def traducir(self, entorno, traductor3d, cadena):


        # cadena para concatenar
        cadenaTraduccion3d = ''



        # ejecutamos nodos derecha y izquierda
        nodoIzquierdo = self.leftExp.traducir(entorno, traductor3d, cadena)
        nodoDerecho = self.rightExp.traducir(entorno, traductor3d, cadena)



        # VARIFICACION SI UNO DE LOS NODOS ES UNA VARIABLE
        # verificacion si algun nodod que sube es una variable para buscar su valoe en el entorno
        if nodoIzquierdo.tipo == TipoExpresion.ID and nodoDerecho.tipo == TipoExpresion.ID:

            nodoIzquierdo = entorno.getVariable3d(nodoIzquierdo.valor)
            nodoDerecho = entorno.getVariable3d(nodoDerecho.valor)


            temporal_izquierdo = traductor3d.getTemporal()
            traductor3d.aumentarTemporal()

            temporal_derecho = traductor3d.getTemporal()
            traductor3d.aumentarTemporal()

            traduccion = ''
            traduccion += f'\n'
            traduccion += f't{temporal_izquierdo} = {nodoIzquierdo.posicion};\n'
            traduccion += f't{temporal_izquierdo} = stack[(int) t{temporal_izquierdo}];\n'
            traduccion += f'\n'
            traduccion += f'\n'
            traduccion += f'\n'
            traduccion += f't{temporal_derecho} = {nodoDerecho.posicion};\n'
            traduccion += f't{temporal_derecho} = stack[(int) t{temporal_derecho}];\n'
            traduccion += f'\n'
            traduccion += f'\n'
            traductor3d.addCadenaTemporal(traduccion)
            
            nodoDerecho.valor = f't{temporal_derecho}'
            nodoIzquierdo.valor = f't{temporal_izquierdo}'




        elif nodoIzquierdo.tipo == TipoExpresion.ID and nodoDerecho.tipo != TipoExpresion.ID:

            temporal_actual = traductor3d.getTemporal()
            traductor3d.aumentarTemporal()

            nodoIzquierdo = entorno.getVariable3d(nodoIzquierdo.valor)

            traductor3d.addCadenaTemporal('\n')
            traductor3d.addCadenaTemporal('\n')
            traductor3d.addCadenaTemporal(f't{temporal_actual} = stack[(int) {nodoIzquierdo.posicion}];\n')
            nodoIzquierdo.valor = f't{temporal_actual}'



        elif nodoIzquierdo.tipo != TipoExpresion.ID and nodoDerecho.tipo == TipoExpresion.ID:

            nodoDerecho = entorno.getVariable3d(nodoDerecho.valor)

            temporal_derecho = traductor3d.getTemporal()
            traductor3d.aumentarTemporal()

            traduccion = ''
            traduccion += f'\n'
            traduccion += f't{temporal_derecho} = {nodoDerecho.posicion};\n'
            traduccion += f't{temporal_derecho} = stack[(int) t{temporal_derecho}];\n'
            traduccion += f'\n'
            traduccion += f'\n'
            traductor3d.addCadenaTemporal(traduccion)
            
            nodoDerecho.valor = f't{temporal_derecho}'









        # COMPARACION DE TIPO DE REALCION
        if self.operador == TipoRelacional.MAYORQUE:
            # cadenaTraduccion3d = ''
            
            # temporal para guardar el resultado
            temporal_actual = traductor3d.getTemporal()
            traductor3d.aumentarTemporal()

            cadenaTraduccion3d += '\n'
            cadenaTraduccion3d += '\n'
            cadenaTraduccion3d += '/*-- RELACIONAL --*/\n'
            cadenaTraduccion3d += f't{temporal_actual} = {nodoIzquierdo.valor} > {nodoDerecho.valor};\n'
            cadenaTraduccion3d += '\n'
            cadenaTraduccion3d += '\n'
            traductor3d.addCadenaTemporal(cadenaTraduccion3d)

            return Simbolo3d(
                self.fila,
                self.columna,
                None,
                TipoExpresion.BOOL,
                f't{temporal_actual}',
                None,
                0,
                0,
            )




        elif self.operador == TipoRelacional.MAYORIGUALQUE:
            # cadenaTraduccion3d = ''
            # temporal para guardar el resultado
            temporal_actual = traductor3d.getTemporal()
            traductor3d.aumentarTemporal()

            cadenaTraduccion3d += '\n'
            cadenaTraduccion3d += '\n'
            cadenaTraduccion3d += '/*-- RELACIONAL --*/\n'
            cadenaTraduccion3d += f't{temporal_actual} = {nodoIzquierdo.valor} >= {nodoDerecho.valor};\n'
            cadenaTraduccion3d += '\n'
            cadenaTraduccion3d += '\n'
            traductor3d.addCadenaTemporal(cadenaTraduccion3d)

            return Simbolo3d(
                self.fila,
                self.columna,
                None,
                TipoExpresion.BOOL,
                f't{temporal_actual}',
                None,
                0,
                0,
            )





        elif self.operador == TipoRelacional.MENORQUE:
            # cadenaTraduccion3d = ''
            # temporal para guardar el resultado
            temporal_actual = traductor3d.getTemporal()
            traductor3d.aumentarTemporal()

            cadenaTraduccion3d += '\n'
            cadenaTraduccion3d += '\n'
            cadenaTraduccion3d += '/*-- RELACIONAL --*/\n'
            cadenaTraduccion3d += f't{temporal_actual} = {nodoIzquierdo.valor} < {nodoDerecho.valor};\n'
            cadenaTraduccion3d += '\n'
            cadenaTraduccion3d += '\n'
            traductor3d.addCadenaTemporal(cadenaTraduccion3d)


            return Simbolo3d(
                self.fila,
                self.columna,
                None,
                TipoExpresion.BOOL,
                f't{temporal_actual}',
                None,
                0,
                0,
            )





        elif self.operador == TipoRelacional.MENORIGUALQUE:
            # cadenaTraduccion3d = ''
            # temporal para guardar el resultado
            temporal_actual = traductor3d.getTemporal()
            traductor3d.aumentarTemporal()

            cadenaTraduccion3d += '\n'
            cadenaTraduccion3d += '\n'
            cadenaTraduccion3d += '/*-- RELACIONAL --*/\n'
            cadenaTraduccion3d += f't{temporal_actual} = {nodoIzquierdo.valor} <= {nodoDerecho.valor};\n'
            cadenaTraduccion3d += '\n'
            cadenaTraduccion3d += '\n'
            traductor3d.addCadenaTemporal(cadenaTraduccion3d)


            return Simbolo3d(
                self.fila,
                self.columna,
                None,
                TipoExpresion.BOOL,
                f't{temporal_actual}',
                None,
                0,
                0,
            )






        elif self.operador == TipoRelacional.IGUALDAD:
            # cadenaTraduccion3d = ''
            # temporal para guardar el resultado
            temporal_actual = traductor3d.getTemporal()
            traductor3d.aumentarTemporal()

            cadenaTraduccion3d += '\n'
            cadenaTraduccion3d += '\n'
            cadenaTraduccion3d += '/*-- RELACIONAL --*/\n'
            cadenaTraduccion3d += f't{temporal_actual} = {nodoIzquierdo.valor} == {nodoDerecho.valor};\n'
            cadenaTraduccion3d += '\n'
            cadenaTraduccion3d += '\n'
            traductor3d.addCadenaTemporal(cadenaTraduccion3d)

            return Simbolo3d(
                self.fila,
                self.columna,
                None,
                TipoExpresion.BOOL,
                f't{temporal_actual}',
                None,
                0,
                0,
            )





        elif self.operador == TipoRelacional.DIFERENTE:
            # cadenaTraduccion3d = ''
            # temporal para guardar el resultado
            temporal_actual = traductor3d.getTemporal()
            traductor3d.aumentarTemporal()

            cadenaTraduccion3d += '\n'
            cadenaTraduccion3d += '\n'
            cadenaTraduccion3d += '/*-- RELACIONAL --*/\n'
            cadenaTraduccion3d += f't{temporal_actual} = {nodoIzquierdo.valor} != {nodoDerecho.valor};\n'
            cadenaTraduccion3d += '\n'
            cadenaTraduccion3d += '\n'
            traductor3d.addCadenaTemporal(cadenaTraduccion3d)


            return Simbolo3d(
                self.fila,
                self.columna,
                None,
                TipoExpresion.BOOL,
                f't{temporal_actual}',
                None,
                0,
                0,
            )


        # error
        return -1


        













    # -------------------------------------------------------------------------
    #                   TRADUCCION DE LA PIRNTLN A 3D
    # -------------------------------------------------------------------------
    def optimizar(self, entorno, traductor3d, cadena):


        # cadena para concatenar
        cadenaTraduccion3d = ''



        # ejecutamos nodos derecha y izquierda
        nodoIzquierdo = self.leftExp.optimizar(entorno, traductor3d, cadena)
        nodoDerecho = self.rightExp.optimizar(entorno, traductor3d, cadena)



        # VARIFICACION SI UNO DE LOS NODOS ES UNA VARIABLE
        # verificacion si algun nodod que sube es una variable para buscar su valoe en el entorno
        if nodoIzquierdo.tipo == TipoExpresion.ID and nodoDerecho.tipo == TipoExpresion.ID:


            nodoIzquierdo = entorno.getVariable3d(nodoIzquierdo.valor)
            nodoDerecho = entorno.getVariable3d(nodoDerecho.valor)


        elif nodoIzquierdo.tipo == TipoExpresion.ID and nodoDerecho.tipo != TipoExpresion.ID:

            temporal_actual = traductor3d.getTemporal()
            traductor3d.aumentarTemporal()

            nodoIzquierdo = entorno.getVariable3d(nodoIzquierdo.valor)

            traductor3d.addCadenaTemporal('\n')
            traductor3d.addCadenaTemporal('\n')
            traductor3d.addCadenaTemporal(f't{temporal_actual} = stack[(int) {nodoIzquierdo.posicion}];\n')
            nodoIzquierdo.valor = f't{temporal_actual}'



        elif nodoIzquierdo.tipo != TipoExpresion.ID and nodoDerecho.tipo == TipoExpresion.ID:


            nodoDerecho = entorno.getVariable3d(nodoDerecho.valor)









        # COMPARACION DE TIPO DE REALCION
        if self.operador == TipoRelacional.MAYORQUE:
            # cadenaTraduccion3d = ''
            
            # temporal para guardar el resultado
            temporal_actual = traductor3d.getTemporal()
            traductor3d.aumentarTemporal()

            cadenaTraduccion3d += '\n'
            cadenaTraduccion3d += '\n'
            cadenaTraduccion3d += '/*-- RELACIONAL --*/\n'
            cadenaTraduccion3d += f't{temporal_actual} = {nodoIzquierdo.valor} > {nodoDerecho.valor};\n'
            cadenaTraduccion3d += '\n'
            cadenaTraduccion3d += '\n'
            traductor3d.addCadenaTemporal(cadenaTraduccion3d)

            return Simbolo3d(
                self.fila,
                self.columna,
                None,
                TipoExpresion.BOOL,
                f't{temporal_actual}',
                None,
                0,
                0,
            )




        elif self.operador == TipoRelacional.MAYORIGUALQUE:
            # cadenaTraduccion3d = ''
            # temporal para guardar el resultado
            temporal_actual = traductor3d.getTemporal()
            traductor3d.aumentarTemporal()

            cadenaTraduccion3d += '\n'
            cadenaTraduccion3d += '\n'
            cadenaTraduccion3d += '/*-- RELACIONAL --*/\n'
            cadenaTraduccion3d += f't{temporal_actual} = {nodoIzquierdo.valor} >= {nodoDerecho.valor};\n'
            cadenaTraduccion3d += '\n'
            cadenaTraduccion3d += '\n'
            traductor3d.addCadenaTemporal(cadenaTraduccion3d)

            return Simbolo3d(
                self.fila,
                self.columna,
                None,
                TipoExpresion.BOOL,
                f't{temporal_actual}',
                None,
                0,
                0,
            )





        elif self.operador == TipoRelacional.MENORQUE:
            # cadenaTraduccion3d = ''
            # temporal para guardar el resultado
            temporal_actual = traductor3d.getTemporal()
            traductor3d.aumentarTemporal()

            cadenaTraduccion3d += '\n'
            cadenaTraduccion3d += '\n'
            cadenaTraduccion3d += '/*-- RELACIONAL --*/\n'
            cadenaTraduccion3d += f't{temporal_actual} = {nodoIzquierdo.valor} < {nodoDerecho.valor};\n'
            cadenaTraduccion3d += '\n'
            cadenaTraduccion3d += '\n'
            traductor3d.addCadenaTemporal(cadenaTraduccion3d)


            return Simbolo3d(
                self.fila,
                self.columna,
                None,
                TipoExpresion.BOOL,
                f't{temporal_actual}',
                None,
                0,
                0,
            )





        elif self.operador == TipoRelacional.MENORIGUALQUE:
            # cadenaTraduccion3d = ''
            # temporal para guardar el resultado
            temporal_actual = traductor3d.getTemporal()
            traductor3d.aumentarTemporal()

            cadenaTraduccion3d += '\n'
            cadenaTraduccion3d += '\n'
            cadenaTraduccion3d += '/*-- RELACIONAL --*/\n'
            cadenaTraduccion3d += f't{temporal_actual} = {nodoIzquierdo.valor} <= {nodoDerecho.valor};\n'
            cadenaTraduccion3d += '\n'
            cadenaTraduccion3d += '\n'
            traductor3d.addCadenaTemporal(cadenaTraduccion3d)


            return Simbolo3d(
                self.fila,
                self.columna,
                None,
                TipoExpresion.BOOL,
                f't{temporal_actual}',
                None,
                0,
                0,
            )






        elif self.operador == TipoRelacional.IGUALDAD:
            # cadenaTraduccion3d = ''
            # temporal para guardar el resultado
            temporal_actual = traductor3d.getTemporal()
            traductor3d.aumentarTemporal()

            cadenaTraduccion3d += '\n'
            cadenaTraduccion3d += '\n'
            cadenaTraduccion3d += '/*-- RELACIONAL --*/\n'
            cadenaTraduccion3d += f't{temporal_actual} = {nodoIzquierdo.valor} == {nodoDerecho.valor};\n'
            cadenaTraduccion3d += '\n'
            cadenaTraduccion3d += '\n'
            traductor3d.addCadenaTemporal(cadenaTraduccion3d)

            return Simbolo3d(
                self.fila,
                self.columna,
                None,
                TipoExpresion.BOOL,
                f't{temporal_actual}',
                None,
                0,
                0,
            )





        elif self.operador == TipoRelacional.DIFERENTE:
            # cadenaTraduccion3d = ''
            # temporal para guardar el resultado
            temporal_actual = traductor3d.getTemporal()
            traductor3d.aumentarTemporal()

            cadenaTraduccion3d += '\n'
            cadenaTraduccion3d += '\n'
            cadenaTraduccion3d += '/*-- RELACIONAL --*/\n'
            cadenaTraduccion3d += f't{temporal_actual} = {nodoIzquierdo.valor} != {nodoDerecho.valor};\n'
            cadenaTraduccion3d += '\n'
            cadenaTraduccion3d += '\n'
            traductor3d.addCadenaTemporal(cadenaTraduccion3d)


            return Simbolo3d(
                self.fila,
                self.columna,
                None,
                TipoExpresion.BOOL,
                f't{temporal_actual}',
                None,
                0,
                0,
            )


        # error
        return -1


        