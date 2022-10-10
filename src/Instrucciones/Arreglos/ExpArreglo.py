from src.Interfaces.TipoExpresion import TipoExpresion



from src.environment.Simbolo3d import Simbolo3d


class ExpArreglo:


    def __init__(self, fila, columna, listadoExpresiones):
        self.fila = fila
        self.columna = columna
        self.listadoExpresiones = listadoExpresiones
        self.tipo = TipoExpresion.ARREGLO



    def ejecutar(self, entorno):
        
        listaRetorno = []

        
        # ejecutar todo todo sea una primitivo
        for elemento in self.listadoExpresiones:
            
            # asegurar todos sea un primitivo
            exp = elemento.ejecutar(entorno)
            listaRetorno.append(exp)

        self.listadoExpresiones = listaRetorno
        return self
        




    # -------------------------------------------------------------------------
    #                   TRADUCCION DE DECLARACIONES DE VARIABLES 3D
    # -------------------------------------------------------------------------

    # self.identificador = viene el identificador de la variable
    # self.valor = viene el simbolo para la variable
    def traducir(self, entorno, traductor3d, cadena):

                
        listaRetorno = []

        
        # ejecutar todo todo sea una primitivo
        for elemento in self.listadoExpresiones:
            
            # asegurar todos sea un primitivo
            exp = elemento.ejecutar(entorno)
            listaRetorno.append(exp)

        self.listadoExpresiones = listaRetorno
        
        return self