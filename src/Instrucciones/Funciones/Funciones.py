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


        cadena3d = ''

        # transformar la funcione en formato 3d
        funcion3d = Funcion3d(
            self.fila,
            self.columna,
            self.nombreFuncion,
            self.listaParametros,
            self.listaInstrucciones,
            self.tipoFuncion,
            traductor3d.getStack()
        )
        

        # agregar al entorno con toda su estructura
        entorno.addFuncion3D(self.nombreFuncion, funcion3d)



        # crear un nuevo entorno para la funcion
        numeroEntrono = entorno.numero + 1
        envFn = Environment(self.nombreFuncion, numeroEntrono, entorno)


        cadena3d += f'\n'
        cadena3d += f'\n'
        cadena3d += f'\n'
        cadena3d += f'\n'
        cadena3d += f'\n'
        cadena3d += f'void {self.nombreFuncion} () \n'
        cadena3d += '{\n'
        cadena3d += f'\n'


        for instruccion  in self.listaInstrucciones:
            instruccion.traducir(envFn, traductor3d, cadena3d)


        cadena3d += traductor3d.getCadenaTemporal()    
        traductor3d.clearCadenaTemporal()

        cadena3d += f'\n'
        cadena3d += f'// SALIDA DE LA FUNCION\n'
        cadena3d += f'  return;\n'
        cadena3d += '}\n'
        cadena3d += f'\n'
        cadena3d += f'\n'
        cadena3d += f'\n'
        cadena3d += f'\n'



        # **********************************************
        #               TRADUCCION
        traductor3d.setContenidoFuncion(cadena3d)
        # **********************************************




        return None




