

from Compiler.Sintactico import p_asignacion_variables


class Environment3d:


    def __init__(self):
        self.temporal = 16
        self.etiqueta = 0
        self.punteroStack = 0
        self.punteroHeap = 0
        self.traduccion = ''
        self.contenidoMain = '' 
        self.contendioFuncion = ''
        self.cadenaTemporal = ''
        self.saltosTemporales = ''
        self.saltoBreak = ''
        self.saltoContinue = ''
        self.saltoRetun = ''
        self.satoLogicoTrue = ''
        self.saltoReturn = ''
        # optimizacion
        self.tabla_optimizacion = []


    


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
        self.traduccion += '//IMPRESION PARA ERRORES MATEMATICOS\n'
        self.traduccion += 'void mathError(){\n'
        self.traduccion += '\n'
        self.traduccion += '    printf("%c", 77);\n'
        self.traduccion += '    printf("%c", 97);\n'
        self.traduccion += '    printf("%c", 116);\n'
        self.traduccion += '    printf("%c", 104);\n'
        self.traduccion += '    printf("%c", 69);\n'
        self.traduccion += '    printf("%c", 114);\n'
        self.traduccion += '    printf("%c", 114);\n'
        self.traduccion += '    printf("%c", 111);\n'
        self.traduccion += '    printf("%c", 114);\n'
        self.traduccion += '    printf("%c", 10);\n'
        self.traduccion += '\n'
        self.traduccion += '\n'
        self.traduccion += '    return;\n'
        self.traduccion += '}\n'       
        self.traduccion += '\n'
        self.traduccion += '\n'
        self.traduccion += '\n'
        self.traduccion += '\n'
        self.traduccion += '//IMPRESION PARA ERRORES MATEMATICOS\n'
        self.traduccion += 'void boundsError(){\n'
        self.traduccion += '\n'
        self.traduccion += '    printf("%c", 66);\n'
        self.traduccion += '    printf("%c", 111);\n'
        self.traduccion += '    printf("%c", 117);\n'
        self.traduccion += '    printf("%c", 110);\n'
        self.traduccion += '    printf("%c", 100);\n'
        self.traduccion += '    printf("%c", 115);\n'
        self.traduccion += '    printf("%c", 69);\n'
        self.traduccion += '    printf("%c", 114);\n'
        self.traduccion += '    printf("%c", 114);\n'
        self.traduccion += '    printf("%c", 111);\n'
        self.traduccion += '    printf("%c", 114);\n'
        self.traduccion += '    printf("%c", 10);\n'
        self.traduccion += '\n'
        self.traduccion += '\n'
        self.traduccion += '    return;\n'
        self.traduccion += '}\n'  
        self.traduccion += '\n'
        self.traduccion += '\n'
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
        self.traduccion += 'void printArreglo(){\n'
        self.traduccion += '    /*------(tamanio del arreglo)------*/\n'
        self.traduccion += '    t12 = t11;\n'
        self.traduccion += '    t12 = heap[(int)t12];\n'
        self.traduccion += '\n'
        self.traduccion += '    /*------(inicio del arreglo)------*/\n'
        self.traduccion += '    t13 = t11 + 1;\n'
        self.traduccion += '    t14 = heap[(int)t13];\n'
        self.traduccion += '\n'
        self.traduccion += '    /*------(contador del for)------*/\n'
        self.traduccion += '    t15 = 0;\n'
        self.traduccion += '    printf("%c", 91);\n'
        self.traduccion += '    IMPRIMIR_ARRELGO:\n'
        self.traduccion += '       if(t15 >= t12) goto FIN_IMPRIMIR_ARREGLO;\n'
        self.traduccion += '        printf("%d",(int)t14);\n'
        self.traduccion += '        printf("%c", 32);\n'
        self.traduccion += '\n'
        self.traduccion += '        t13 = t13 + 1;\n'
        self.traduccion += '        t14 = heap[(int)t13];\n'
        self.traduccion += '        t15 = t15 + 1;\n'
        self.traduccion += '        goto IMPRIMIR_ARRELGO;\n'
        self.traduccion += '        FIN_IMPRIMIR_ARREGLO:\n'
        self.traduccion += '        printf("%c", 93);\n'
        self.traduccion += '        return;\n'
        self.traduccion += '}\n'       
        self.traduccion += '\n'
        self.traduccion += '\n'
        self.traduccion += '\n'
        self.traduccion += '\n'
        self.traduccion += '\n'
        self.traduccion += '\n'
        self.traduccion += '\n'
        self.traduccion += '/*------------- FUNCIONES -----------------*/\n'
        self.traduccion += '\n'
        self.traduccion += f'{self.contendioFuncion}\n'
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





    # *********************************************
    # metodo para obtener la cadena de la traduccion
    def getCadena(self):
        return self.traduccion




    # metodo pra concatenar la traduccion
    def setCadena(self, cadena):
        self.traduccion += self.traduccion + cadena





    # *********************************************
    # contenido Funcion Main
    def getContenidoMain(self):
        return self.contenidoMain



    def setContenidoMain(self, cadena):
        self.contenidoMain += cadena






    # *********************************************
    # contendio Funciones 
    def getContenidoFuncion(self):
        return self.contendioFuncion


    
    def setContenidoFuncion(self, cadena):
        self.contendioFuncion += cadena


    
    def clearContenidoFuncion(self):
        self.contendioFuncion = ''








    # *********************************************
    # metodo para aumentar el numero del temporal
    def aumentarTemporal(self):
        self.temporal += 1


    # obtener el numero del temporal actual
    def getTemporal(self):
        return self.temporal






    # *********************************************
    # metodo para aumetar el numero de las etiquetas
    def aumentarEtiqueta(self):
        self.etiqueta += 1



    # etiqueta para aumetar la etiqueta
    def getEtiqueta(self):
        return self.etiqueta







    # *********************************************
    # metodo para manejar el valor de los puntero
    def aumentarStack(self):
        self.punteroStack += 1



    def getStack(self):
        return self.punteroStack






    # *********************************************
    # para menejo del puntero del heap
    def aumentarHeap(self):
        self.punteroHeap += 1


    def getHeap(self):
        return self.punteroHeap







    # *********************************************
    # cadena de concatenacion temporal
    def getCadenaTemporal(self):
        return self.cadenaTemporal


    def addCadenaTemporal(self, cadena):
        self.cadenaTemporal += cadena


    def clearCadenaTemporal(self):
        self.cadenaTemporal = ''







    # *********************************************
    # cadena para manejar saltos temporales 
    def getSaltosTemporales(self):
        return self.saltosTemporales


    def addSaltoTemporal(self, cadena):
        self.saltosTemporales += cadena

    def clearSaltosTemporales(self):
        self.saltosTemporales = ''








    # *********************************************
    # SALTO LOGICO TRUE
    def getSaltoLogicoTrue(self):
        return self.satoLogicoTrue


    def addSaltoLogicoTrue(self, cadena):
        self.satoLogicoTrue += cadena


    def clearSaltoLogicoTrue(self):
        self.satoLogicoTrue = ''









    # *********************************************
    # menajo de saltos
    # BREAK
    def getSaltoBreak(self):
        return self.saltoBreak


    def addSaltoBreak(self, cadena):
        self.saltoBreak += cadena


    def clearSaltoBreak(self):
        self.saltoBreak = ''






    # *********************************************
    # CONTINUE
    def getSaltoContinue(self):
        return self.saltoContinue

    
    def addSaltoContinue(self, cadena):
        self.saltoContinue += cadena


    def clearSaltoContinue(self):
        self.saltoContinue = ''






    # *********************************************
    # RETURN
    def getSaltoReturn(self):
        return self.saltoReturn

    
    def addSaltoReturn(self, cadena):
        self.saltoReturn += cadena


    def clearSaltoReturn(self):
        self.saltoReturn = ''




    

    # # *********************************************
    # # Vector con las reglas optimizacion

    # # vector con las reglas ya aplicadas
    # def add_reporte_optimizacion(self,tipo, regla, orginal, optimizada, fila):
    #     self.tabla_optimizacion.append([tipo,regla, orginal, optimizada, fila])


    # def get_reporte_optimizacion(self):
    #     return self.tabla_optimizacion