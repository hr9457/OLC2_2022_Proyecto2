from src.Interfaces.Instruccion import Instruccion
from src.environment.Environment import Environment


from src.environment.Funcion3d import Funcion3d


class Funciones(Instruccion):


    def __init__(self, fila, columna, nombreFuncion, listaParamentros, listaInstrucciones, tipoFuncion, tablaSimbolos):
        self.fila = fila
        self.columna = columna
        self.nombreFuncion = nombreFuncion
        self.listaParametros = listaParamentros
        self.listaInstrucciones = listaInstrucciones
        self.tipoFuncion = tipoFuncion
        self.retornoFuncion = ''
        self.expReturn = None
        self.tablaSimbolos = tablaSimbolos


    def ejecutar(self,entorno):
        entorno.addFuncion(self.nombreFuncion,self)


        # para reportes
        self.tablaSimbolos.append([self.nombreFuncion,'Funcion',self.tipoFuncion,entorno.nombre,self.fila,self.columna])
        # -------------

        return None







    # -------------------------------------------------------------------------
    #                   TRADUCCION DE LA PIRNTLN A 3D
    # -------------------------------------------------------------------------
    def traducir(self, entorno, traductor3d, cadena):



        cantidad_parametros = len(self.listaParametros)


        # transformar la funcione en formato 3d
        funcion3d = Funcion3d(
            self.fila,
            self.columna,
            self.nombreFuncion,
            self.listaParametros,
            self.listaInstrucciones,
            self.tipoFuncion,
            cantidad_parametros
        )
        

        # agregar al entorno con toda su estructura
        entorno.addFuncion3D(self.nombreFuncion, funcion3d)


        return None




