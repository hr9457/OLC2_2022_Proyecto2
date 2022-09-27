from src.Interfaces.Instruccion import Instruccion
from src.environment.Environment import Environment
from src.Expresiones.Primitivo import Primitivo
from src.environment.Simbolo import Simbolo
from src.Interfaces.TipoMutable import TipoMutable
from src.Interfaces.TipoExpresion import TipoExpresion



# utilidades para traduccion en 3d
from src.environment.Simbolo3d import Simbolo3d
from src.environment3d.Enviroment3d import Environment3d




class Forin(Instruccion):

    def __init__(self, fila, columna, tablaErrores, variable, inicio, final, instrucciones):
        self.fila = fila
        self.columna = columna
        self.variable = variable
        self.inicio = inicio
        self.final = final
        self.instrucciones = instrucciones
        # self.retornoForin = ''
        self.tablaErrores = tablaErrores




    def ejecutar(self, entorno):


        retornoForin = ''
        # crear un nuevo entorno para el for
        numeroEntorno = entorno.numero + 1
        envFor = Environment('FOR',numeroEntorno,entorno)




                
        # tipo de ejecucion del ciclo for
        inicioFor = self.inicio.ejecutar(entorno)
        finalFor = self.final.ejecutar(entorno)

        # si son variables
        if inicioFor.tipo == TipoExpresion.ID and finalFor.tipo == TipoExpresion.ID:
            inicioFor = entorno.getVariable(inicioFor.valor)
            finalFor = entorno.getVariable(finalFor.valor)
        
        elif finalFor.tipo == TipoExpresion.ID:
            finalFor = entorno.getVariable(finalFor.valor)

        elif inicioFor.tipo == TipoExpresion.ID:
            inicioFor = entorno.getVariable(inicioFor.valor)



        # creacion variables para iteraciones
        if self.variable.tipo == TipoExpresion.ID:
            entorno.addVariable(self.variable.valor,
                        Simbolo(
                            self.fila,
                            self.columna,
                            self.variable.valor,
                            inicioFor.tipo,
                            inicioFor.valor,
                            TipoMutable.MUTABLE
                            ))
        else:
            return 'FORIN -> erorr parametros'




        if inicioFor.tipo == TipoExpresion.INTEGER and finalFor.tipo == TipoExpresion.INTEGER:           

            
            # ejecucion del ciclo for
            for i in range(inicioFor.valor, finalFor.valor):

                # ejecucion de las instrucciones que hay en el ciclo for
                for instruccion in self.instrucciones:

                    result = instruccion.ejecutar(envFor)

                    # menejo de instrucciones break y continue
                    if isinstance(result, Primitivo) and result.tipo == TipoExpresion.BREAK:
                        if result.valor is not None:
                            retornoForin += result.valor
                        return retornoForin

                    elif isinstance(result, Primitivo) and result.tipo == TipoExpresion.CONTINUE:
                        if result.valor is not None:
                            retornoForin += result.valor
                        break


                    # concatenacion del resultado del for
                    if result is not None:
                        retornoForin += result


                # actualizcion de la variable
                variableFor = envFor.getVariable(self.variable.valor)
                envFor.updateVariabe(self.variable.valor,
                    Simbolo(
                        self.fila,
                        self.columna,
                        self.variable.valor,
                        inicioFor.tipo,
                        variableFor.valor + 1,
                        TipoMutable.MUTABLE
                        ))



            return retornoForin

        else:
            # para reportes
            self.tablaErrores.append(['FORIN : error paramentros',entorno.nombre,self.fila,self.columna])
            # --------------------------------
            return 'FORIN : error paramentros'


        











    # -------------------------------------------------------------------------
    #                   TRADUCCION DE LA PIRNTLN A 3D
    # -------------------------------------------------------------------------
    def traducir(self, entorno, traductor3d, cadena):
        
        # cadena para concatenar
        cadenaTraduccion3d = ''


        # crear un nuevo entorno para el for
        numeroEntorno = entorno.numero + 1
        envFor = Environment('FOR',numeroEntorno,entorno)


        
        # for exp in expInicio punto punto expFinal { instrucciones }

        # utildades para el manejo del for        
        # exp --> n (pivote)
        pivote = self.variable.traducir(entorno, traductor3d, cadena)
        posicion_pivote = traductor3d.getStack()
        traductor3d.aumentarStack()

        envFor.addVariable3d(
            pivote.valor,
            Simbolo3d(
                pivote.fila,
                pivote.columna,
                pivote.valor,
                TipoExpresion.INTEGER,
                0,
                None,
                posicion_pivote,
                0
            )
        )
        cadenaTraduccion3d += f'\n'
        cadenaTraduccion3d += f'\n'
        cadenaTraduccion3d += f'\n'
        cadenaTraduccion3d += f'/*------ PIVOTE FOR IN ------*/\n'
        cadenaTraduccion3d += f'stack[(int)P] = 0;\n'
        cadenaTraduccion3d += f'P = P + 1;\n'





        # expInicio
        inicio_for = self.inicio.traducir(entorno, traductor3d, cadena)
        temporal_inicio = traductor3d.getTemporal()
        traductor3d.aumentarTemporal()


        # expFinal
        final_for = self.final.traducir(entorno, traductor3d, cadena) 
        temporal_final = traductor3d.getTemporal()
        traductor3d.aumentarTemporal()





        # etiqueta pivotear en el for
        etiqueta_pivote = traductor3d.getEtiqueta()
        traductor3d.aumentarEtiqueta()

        etiqueta_true = traductor3d.getEtiqueta()
        traductor3d.aumentarEtiqueta()

        etiqueta_false = traductor3d.getEtiqueta()
        traductor3d.aumentarEtiqueta()



        cadenaTraduccion3d += f'\n'
        cadenaTraduccion3d += f'\n'
        cadenaTraduccion3d += f'\n'
        cadenaTraduccion3d += f'/*------ FOR IN ------*/\n'
        cadenaTraduccion3d += f'\n'
        cadenaTraduccion3d += f't{temporal_inicio} = {inicio_for.valor};\n'
        cadenaTraduccion3d += f'\n'
        cadenaTraduccion3d += f't{temporal_final} = {final_for.valor};\n'
        cadenaTraduccion3d += f'\n'
        cadenaTraduccion3d += f'\n'        
        cadenaTraduccion3d += f'L{etiqueta_pivote}:\n'
        cadenaTraduccion3d += f'\n'
        cadenaTraduccion3d += f'if ( t{temporal_inicio} < t{temporal_final} )  goto L{etiqueta_true};\n'
        cadenaTraduccion3d += f'goto L{etiqueta_false};\n'
        cadenaTraduccion3d += f'L{etiqueta_true}:\n'
        cadenaTraduccion3d += '\n'
        cadenaTraduccion3d += '\n'

        traductor3d.addCadenaTemporal(cadenaTraduccion3d)
        cadenaTraduccion3d = ''
        
        
        # instrucciones
        actualizacion_pivote = ''
        temporal_actualizacion = traductor3d.getTemporal()
        traductor3d.aumentarTemporal()

        for instruccion in self.instrucciones:
            instruccion.traducir(envFor, traductor3d, cadena)


        # por cada paso de instruccion se actualizara la variable pivote
        variable_pivote_for = envFor.getVariable3d(pivote.valor) 
        actualizacion_pivote += f'\n'
        actualizacion_pivote += f'\n'
        actualizacion_pivote += f'/*---- ACTUALIZACION DE PIVOTE FOR IN ----*/\n'           
        actualizacion_pivote += f't{temporal_actualizacion} = stack[(int) {variable_pivote_for.posicion}];\n'
        actualizacion_pivote += f't{temporal_actualizacion} = t{temporal_actualizacion} + 1;\n'
        actualizacion_pivote += f'stack[(int) {variable_pivote_for.posicion}] = t{temporal_actualizacion};\n'
        traductor3d.addCadenaTemporal(actualizacion_pivote)
        actualizacion_pivote = ''



        cadenaTraduccion3d += '\n'
        cadenaTraduccion3d += '\n'
        cadenaTraduccion3d += '\n'
        cadenaTraduccion3d += '/*---- AUMENTO ----*/\n'
        cadenaTraduccion3d += f't{temporal_inicio} = t{temporal_inicio} + 1;\n'
        cadenaTraduccion3d += '\n'
        cadenaTraduccion3d += '\n'
        cadenaTraduccion3d += '/*---- PIVOTE ----*/\n'
        cadenaTraduccion3d += f'goto L{etiqueta_pivote};\n'
        cadenaTraduccion3d += '\n'
        cadenaTraduccion3d += '/*--- SALIDA DEL FOR IN ---*/\n'
        cadenaTraduccion3d += f'L{etiqueta_false}:\n'
        cadenaTraduccion3d += '\n'
        cadenaTraduccion3d += '\n'


        

        traductor3d.addCadenaTemporal(cadenaTraduccion3d)



        
        return None