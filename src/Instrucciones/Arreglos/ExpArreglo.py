from src.Interfaces.TipoExpresion import TipoExpresion




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
        