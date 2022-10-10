from src.Expresiones.Primitivo import Primitivo
from src.Interfaces.TipoExpresion import TipoExpresion
from src.environment.Simbolo import Simbolo
from src.Error.Error import Error
from src.Instrucciones.Struct.PrimateStruct import PrimateStruct

# clase para menejar los entornos
class Environment:
    
    # consturctor del entorno
    def __init__(self, nombre, numero, prev):
        self.nombre = nombre
        self.numero = numero
        self.variables = {}
        self.variables3d = {}
        self.funciones = {}
        self.funciones3d = {}
        self.structs = {}
        self.prev = prev
        self.next = None
        



    # ---------------------------------------------
    #            MANEJO DE VARIABLES
    # ---------------------------------------------

    #  metodo para agregar variables
    def addVariable(self, id ,nuevaVariable):

        self.variables.update({id: nuevaVariable})
        print('ENTORNO: variable agregada')
        # print(self.variables)


    
    # funcion para actualizar variables en los entornos
    def updateVariabe(self,id, actualizacion):

        # recorrro el listado de variables del entorno
        for key in self.variables.keys():
            if key == id:
                print('UPDATE: variable encontrada en el entorno')
                self.variables.update({id: actualizacion})
                return

        
        print('UPDATE: buscando en el entorno anterior')
        self.prev.updateVariabe(id,actualizacion)






    # metodo para obtener valor de una variable
    def getVariable(self, id):

        # print(self.variables)
        for key in self.variables.keys():        

            if key == id:
    
                if self.variables[key].tipo == TipoExpresion.STRUCT or self.variables[key].tipo == TipoExpresion.ARREGLO or self.variables[key].tipo == TipoExpresion.VECTOR:
                    return self.variables[key]



                else:
                    return Simbolo(
                        self.variables[key].fila,
                        self.variables[key].columna,
                        self.variables[key].identificador,
                        self.variables[key].tipo,
                        self.variables[key].valor,
                        self.variables[key].mutabilidad)

        # buscar en el etorno anterior
        if self.prev != None:
            print('buscando en el entorno anterior')
            return self.prev.getVariable(id)


        # print(key)
        print('variable no encontrada')
        return None
        # return Error('variable no encontrada')




    # ---------------------------------------------
    #            MANEJO DE FUNCIONES
    # ---------------------------------------------

    def addFuncion(self, id, contenido):
        self.funciones.update({id:contenido})
        # print(self.funciones)


    def getFuncion(self, id):
        for key in self.funciones.keys():
            if key == id:
                return self.funciones[key]


        if self.prev != None:
            return self.prev.getFuncion(id)

        return None




    def updateValueFuncion(self, id, value):
        for key in self.funciones.keys():
            if key == id:
                self.funciones[key] = value
                return None

        if self.prev != None:
            return self.prev.updateValueFuncion(id, value)

        return None




    # ---------------------------------------------
    #            MANEJO DE STRUCTS
    # ---------------------------------------------
    def addStruct(self, id, contenido):
        self.structs.update({id:contenido})
        print('Struct agregado')


    
    def getStruct(self, id):
        for key in self.structs.keys():
            if key == id:
                return self.structs[key]

        if self.prev != None:
            return self.prev.getStruct(id)

        return None


















    # ---------------------------------------------
    #            MANEJO DE 3D
    # ---------------------------------------------

    # *********************************************
    #  metodo para agregar variables
    # *********************************************
    def addVariable3d(self, id ,nuevaVariable):

        self.variables3d.update({id: nuevaVariable})
        print('ENTORNO: variable agregada')
        # print(self.variables)


    
    # funcion para actualizar variables en los entornos
    def updateVariabe3d(self,id, actualizacion):

        # recorrro el listado de variables del entorno
        for key in self.variables3d.keys():
            if key == id:
                print('UPDATE: variable encontrada en el entorno')
                self.variables3d.update({id: actualizacion})
                return

        
        print('UPDATE: buscando en el entorno anterior')
        self.prev.updateVariabe(id,actualizacion)






    # metodo para obtener valor de una variable
    def getVariable3d(self, id):

        # print(self.variables)
        for key in self.variables3d.keys():        

            if key == id:

                return self.variables3d[key]

        # buscar en el etorno anterior
        if self.prev != None:
            print('buscando en el entorno anterior')
            return self.prev.getVariable3d(id)


        # print(key)
        print('variable no encontrada')
        return -1
        # return Error('variable no encontrada')






    # *********************************************
    #               FUNCIONES EN 3D    
    # *********************************************
    def addFuncion3D(self, id, funcion):
        self.funciones3d.update({id:funcion})
        print('funcion agregada')




    def getFuncion3D(self, id):
        for key in self.funciones3d.keys():
            if key == id:
                return self.funciones3d[key]


        if self.prev != None:
            return self.prev.getFuncion3D(id)

        return -1