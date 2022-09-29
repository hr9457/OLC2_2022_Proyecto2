from src.Interfaces.Instruccion import Instruccion
from src.environment.Environment import Environment
from src.Expresiones.Primitivo import Primitivo
from src.Interfaces.TipoExpresion import TipoExpresion


class Loop(Instruccion):

    def __init__(self, fila, columna, nodo):
        self.fila = fila
        self.columna = columna
        self.nodo = nodo
        self.resultadoWhile = ''


    def ejecutar(self, entorno):
        

        if self.nodo != None:

            numeroEntorno = entorno.numero + 1
            envWhile = Environment('LOOP', numeroEntorno, entorno)


            while True:
                for instruccion in self.nodo:
                    result = instruccion.ejecutar(envWhile)


                    # si viene una instruccion break
                    if isinstance(result,Primitivo) and result.tipo == TipoExpresion.BREAK:
                        return self.resultadoWhile


                    # si viene una instruccion continue
                    elif isinstance(result, Primitivo) and result.tipo == TipoExpresion.CONTINUE:
                        break


                    # concatenacion
                    if result != None:
                        self.resultadoWhile += result


        else:
            return ''





    
    # -------------------------------------------------------------------------
    #                   TRADUCCION DE LA PIRNTLN A 3D
    # -------------------------------------------------------------------------
    def traducir(self, entorno, traductor3d, cadena):
        
        traduccion = ''

        # creacion de un nuevo entrono para el while
        numeroEntorno = entorno.numero + 1
        envLoop = Environment('LOOP', numeroEntorno, entorno)


        etiqueta_rebote = traductor3d.getEtiqueta()
        traductor3d.aumentarEtiqueta()

        etiqueta_verdadero = traductor3d.getEtiqueta()
        traductor3d.aumentarEtiqueta()

        
        traduccion += f'\n'
        traduccion += f'\n'
        traduccion += f'/*-------- LOOP ---------*/\n'
        traduccion += f'\n'
        traduccion += f'L{etiqueta_rebote}:\n'
        traduccion += f'\n'
        traduccion += f'if ( 1 ) goto L{etiqueta_verdadero};\n'
        traduccion += f'L{etiqueta_verdadero}:\n'
        traduccion += f'\n'
        traduccion += f'\n'
        


        # *********************** TRADUCCION *********************
        traductor3d.addCadenaTemporal(traduccion)
        traduccion = ''
        traduccion += f'\n'
        traduccion += f'\n'
        
        
        for instruccion in self.nodo:

            instruccion.traducir(envLoop, traductor3d, cadena)


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



        
        
        traduccion += f'\n'
        traduccion += f'\n'
        traduccion += f'/*---- FIN DEL CICLO LOOP ----*/\n'
        traduccion += f'goto L{etiqueta_rebote};\n'
        traduccion += f'\n'
        traduccion += f'\n'
        traduccion += f'\n'


        # *********************** TRADUCCION *********************
        traductor3d.addCadenaTemporal(traduccion)



        #           SALIDA DEL BREAK
        #           QUIEBRE DE CICLO
        traductor3d.addCadenaTemporal(traductor3d.getSaltoBreak())
        traductor3d.clearSaltoBreak()
        traductor3d.clearSaltoContinue()






        return None






