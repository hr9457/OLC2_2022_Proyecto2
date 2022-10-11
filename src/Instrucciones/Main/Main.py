from src.Interfaces.Instruccion import Instruccion



from src.Instrucciones.Funciones.GetFuncion import GetFuncion
from src.Instrucciones.Imprimir import Imprimir



class FuncionMain(Instruccion):

    def __init__(self, fila, columna, instrucciones):
        self.fila = fila
        self.columna = columna
        self.instrucciones = instrucciones



    def ejecutar(self, entorno):

        resultInstrucciones =''

        # ejecucion de todas las intrucciones del metodo main
        for instruccion in self.instrucciones:
            retorno = instruccion.ejecutar(entorno)
            # print('paro')

            if retorno != None and isinstance(retorno, str):
                resultInstrucciones += retorno


        return resultInstrucciones











    # -------------------------------------------------------------------------
    #                   TRADUCCION DE LA PIRNTLN A 3D
    # -------------------------------------------------------------------------

    # para ejecutar todas la acciones de la traduccion en 3d
    def traducir(self, entorno, traductor3d, cadena):

        cadena3d = ''

        for instruccion in self.instrucciones:

            if isinstance(instruccion, GetFuncion):
                # **********************************************
                #               TRADUCCION
                traductor3d.setContenidoMain(traductor3d.getCadenaTemporal())
                traductor3d.clearCadenaTemporal()
                # **********************************************

            
            if isinstance(instruccion, Imprimir):
                # **********************************************
                #               TRADUCCION
                traductor3d.setContenidoMain(traductor3d.getCadenaTemporal())
                traductor3d.clearCadenaTemporal()
                # **********************************************



            instruccion.traducir(entorno, traductor3d, cadena3d)


            

        


        # **********************************************
        #               TRADUCCION
        traductor3d.setContenidoMain(traductor3d.getCadenaTemporal())
        traductor3d.clearCadenaTemporal()
        # **********************************************


        return None











    # -------------------------------------------------------------------------
    #                   TRADUCCION DE LA PIRNTLN A 3D
    # -------------------------------------------------------------------------
    
    # para ejecutar todas la acciones de la traduccion en 3d
    def optimizar(self, entorno, traductor3d, cadena):

        cadena3d = ''

        for instruccion in self.instrucciones:

            if isinstance(instruccion, GetFuncion):
                # **********************************************
                #               TRADUCCION
                traductor3d.setContenidoMain(traductor3d.getCadenaTemporal())
                traductor3d.clearCadenaTemporal()
                # **********************************************

            
            if isinstance(instruccion, Imprimir):
                # **********************************************
                #               TRADUCCION
                traductor3d.setContenidoMain(traductor3d.getCadenaTemporal())
                traductor3d.clearCadenaTemporal()
                # **********************************************



            instruccion.optimizar(entorno, traductor3d, cadena3d)


            

        


        # **********************************************
        #               TRADUCCION
        traductor3d.setContenidoMain(traductor3d.getCadenaTemporal())
        traductor3d.clearCadenaTemporal()
        # **********************************************


        return None