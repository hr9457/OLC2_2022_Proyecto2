

class Environment3d:


    def __init__(self):
        self.temporal = 11
        self.etiqueta = 0
        self.punteroStack = 0
        self.punteroHeap = 0
        self.traduccion = ''
        self.contenidoMain = '' 
        self.cadenaTemporal = ''
        self.saltosTemporales = ''
        self.saltoBreak = ''
        self.saltoContinue = ''
        self.saltoRetun = ''
        self.satoLogicoTrue = ''


    


    # inicio concatenacion de 3d
    def cabecera(self):
        self.traduccion += '/*------------- HEADER --------------*/\n' 
        self.traduccion += '# include <stdio.h>\n'
        self.traduccion += '\n'
        self.traduccion += '\n'


        self.traduccion += 'float heap[10000];\n'
        self.traduccion += 'float stack[10000];\n'
        self.traduccion += 'float P;\n'
        self.traduccion += 'float H;\n'
        self.traduccion += '\n'
        self.traduccion += '\n'
        self.traduccion += '\n'


        # -------------- TEMPORALES -----------------------
        # ciclo for para crear todos los temporales
        self.traduccion += 'float '
        for i in range(self.temporal):
            self.traduccion += f't{i} '
            if i < self.temporal-1:
                self.traduccion += ', '
        self.traduccion += ';\n'
        self.traduccion += '\n'
        self.traduccion += '\n'
        self.traduccion += '\n'



        self.traduccion += '/*------------- NATIVAS --------------*/\n'
        self.traduccion += '\n'
        self.traduccion += '\n'
        self.traduccion += 'void printString(){\n'
        self.traduccion += '    /*------(tamanio del arreglo)------*/\n'
        self.traduccion += '    t1 = t0;\n'
        self.traduccion += '\n'
        self.traduccion += '    /*------(inicio del arreglo)------*/\n'
        self.traduccion += '    t3 = heap[(int)t2];\n'
        self.traduccion += '\n'
        self.traduccion += '    /*------(contador del for)------*/\n'
        self.traduccion += '    t4 = 0;\n'
        self.traduccion += '    IMPRIMIR:\n'
        self.traduccion += '       if(t4 > t1) goto FINIMPRIMIR;\n'
        self.traduccion += '        printf("%c",(char)t3);\n'
        self.traduccion += '\n'
        self.traduccion += '        t2 = t2 + 1;\n'
        self.traduccion += '        t3 = heap[(int)t2];\n'
        self.traduccion += '        t4 = t4 + 1;\n'
        self.traduccion += '        goto IMPRIMIR;\n'
        self.traduccion += '        FINIMPRIMIR:\n'
        self.traduccion += '        return;\n'
        self.traduccion += '}\n'       
        self.traduccion += '\n'
        self.traduccion += '\n'
        self.traduccion += '\n'
        self.traduccion += '\n'
        self.traduccion += 'void funcionSqrt(){\n'
        self.traduccion += '\n'
        self.traduccion += '    // parametro es t5\n'
        self.traduccion += '    //operacion sqlrt\n'
        self.traduccion += '    t6 = t5 / 2;\n'
        self.traduccion += '\n'
        self.traduccion += '    //contador temp \n'
        self.traduccion += '    t7 = 0;\n'
        self.traduccion += '\n'
        self.traduccion += '\n'
        self.traduccion += '    //ciclo\n'
        self.traduccion += '    inicioSqrt:\n'
        self.traduccion += '    if (t6 != t7) goto cicloSqrt; \n'
        self.traduccion += '    goto finSqrt;\n'
        self.traduccion += '    cicloSqrt:\n'
        self.traduccion += '\n'
        self.traduccion += '\n'
        self.traduccion += '    // temp = sqrt\n'
        self.traduccion += '    t7 = t6;\n'
        self.traduccion += '\n'
        self.traduccion += '    //operacion\n'
        self.traduccion += '    t8 = t5 / t7;\n'
        self.traduccion += '    t9 = t8 + t7;\n'
        self.traduccion += '    t10 = t9 / 2;\n'
        self.traduccion += '\n'
        self.traduccion += '    // sqrt = operacion\n'
        self.traduccion += '    t6 = t10;\n'
        self.traduccion += '\n'
        self.traduccion += '    goto inicioSqrt;\n'
        self.traduccion += '\n'
        self.traduccion += '    //salida\n'
        self.traduccion += '    finSqrt:\n'
        self.traduccion += '    return;\n'
        self.traduccion += '\n'
        self.traduccion += '    //respuesta almacena en t6\n'
        self.traduccion += '}\n'
        self.traduccion += '\n'
        self.traduccion += '\n'
        self.traduccion += '\n'
        self.traduccion += '\n'
        self.traduccion += '\n'
        self.traduccion += '\n'
        self.traduccion += '\n'




        self.traduccion += '/*------------- INICIO -----------------*/\n'
        self.traduccion += '\n'
        self.traduccion += 'void main(){\n'
        self.traduccion += '\n'
        self.traduccion += '\n'
        self.traduccion += '/*----  PUNTEROS ------*/\n'
        self.traduccion += '    P = 0;\n'
        self.traduccion += '    H = 0;\n'
        self.traduccion += '\n'
        self.traduccion += '\n'
        self.traduccion += f'{self.contenidoMain}\n'
        self.traduccion += '\n'
        self.traduccion += '    return;\n'
        self.traduccion += '}\n'
        self.traduccion += '\n'






    # metodo para obtener la cadena de la traduccion
    def getCadena(self):
        return self.traduccion




    # metodo pra concatenar la traduccion
    def setCadena(self, cadena):
        self.traduccion += self.traduccion + cadena






    # contenido
    def getContenidoMain(self):
        return self.contenidoMain



    def setContenidoMain(self, cadena):
        self.contenidoMain += cadena






    # metodo para aumentar el numero del temporal
    def aumentarTemporal(self):
        self.temporal += 1


    # obtener el numero del temporal actual
    def getTemporal(self):
        return self.temporal







    # metodo para aumetar el numero de las etiquetas
    def aumentarEtiqueta(self):
        self.etiqueta += 1



    # etiqueta para aumetar la etiqueta
    def getEtiqueta(self):
        return self.etiqueta








    # metodo para manejar el valor de los puntero
    def aumentarStack(self):
        self.punteroStack += 1



    def getStack(self):
        return self.punteroStack







    # para menejo del puntero del heap
    def aumentarHeap(self):
        self.punteroHeap += 1


    def getHeap(self):
        return self.punteroHeap








    # cadena de concatenacion temporal
    def getCadenaTemporal(self):
        return self.cadenaTemporal


    def addCadenaTemporal(self, cadena):
        self.cadenaTemporal += cadena


    def clearCadenaTemporal(self):
        self.cadenaTemporal = ''








    # cadena para manejar saltos temporales 
    def getSaltosTemporales(self):
        return self.saltosTemporales


    def addSaltoTemporal(self, cadena):
        self.saltosTemporales += cadena

    def clearSaltosTemporales(self):
        self.saltosTemporales = ''









    # SALTO LOGICO TRUE
    def getSaltoLogicoTrue(self):
        return self.satoLogicoTrue


    def addSaltoLogicoTrue(self, cadena):
        self.satoLogicoTrue += cadena


    def clearSaltoLogicoTrue(self):
        self.satoLogicoTrue = ''







    # menajo de saltos
    # BREAK
    def getSaltoBreak(self):
        return self.saltoBreak


    def addSaltoBreak(self, cadena):
        self.saltoBreak += cadena


    def clearSaltoBreak(self):
        self.saltoBreak = ''


    
    # CONTINUE
    def getSaltoContinue(self):
        return self.saltoContinue

    
    def addSaltoContinue(self, cadena):
        self.saltoContinue += cadena


    def clearSaltoContinue(self):
        self.saltoContinue = ''