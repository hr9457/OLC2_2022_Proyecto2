# importacion de ply
from Compiler.Lexico import tokens, columnToken
from src.Instrucciones.Struct.BuildStruct import BuildStruct
input = ""

# importaciones de clases manejo de semantica

# importaciones para manejo de tipos
from src.Interfaces.TipoExpresion import TipoExpresion
from src.Interfaces.TipoOperador import TipoOperador
from src.Interfaces.TipoRelacional import TipoRelacional
from src.Interfaces.TipoLogico import TipoLogico
from src.Interfaces.TipoMutable import TipoMutable
from src.Interfaces.TipoNativas import TipoNativas



# importaciones para manejo de Expresiones
from src.Expresiones.Primitivo import Primitivo
from src.Expresiones.Aritmetica import Aritmetica
from src.Expresiones.Negativo import Negativo
from src.Expresiones.Relacional import Relacional
from src.Expresiones.Logico import Logico
from src.Expresiones.Pow import Pow
from src.Expresiones.Nativas.Nativas import Nativas



# importacion de instrucciones
from src.Instrucciones.Imprimir import Imprimir
from src.Instrucciones.Variables.Declaracion import Declaracion
from src.Instrucciones.Variables.Asignacion import Asignacion
from src.Instrucciones.Casteo.Casteo import Casteo
from src.Instrucciones.Decision.InstruccionIf import InstruccionIf
from src.Instrucciones.Decision.instruccionElse import InstruccionElse
from src.Instrucciones.Bucle.While import While
from src.Instrucciones.Bucle.Loop import Loop
from src.Instrucciones.Bucle.Forin import Forin
from src.Instrucciones.Bucle.ForinArreglos import ForinArreglos



# importaciones para funciones
from src.Instrucciones.Funciones.Funciones import Funciones
from src.Instrucciones.Funciones.GetFuncion import GetFuncion




# importaciones para structs
from src.Instrucciones.Struct.Struct import Struct
from src.Instrucciones.Struct.SimboloStruct import SimboloStruct
from src.Instrucciones.Struct.AsignacionStruct import AsignacionStruct
from src.Instrucciones.Struct.AccesStruct import AccesStruct




# manejo de arreglos
from src.Instrucciones.Arreglos.ExpArreglo import ExpArreglo
from src.Instrucciones.Arreglos.AcessArreglo import AcessArreglo
from src.Instrucciones.Arreglos.ExpArreglo import ExpArreglo
from src.Instrucciones.Arreglos.TipoArreglo import TipoArreglo
from src.Instrucciones.Arreglos.ModificarValor import ModificarValorArreglo
from src.Instrucciones.Arreglos.Len import Len




# manejo de vectores
from src.Instrucciones.Vectores.VariableVector import VariableVector
from src.Instrucciones.Vectores.VariableVectorExp import VariableVectorExp
from src.Instrucciones.Vectores.VariableVectorCapacity import VariableVectorCapacity
from src.Instrucciones.Vectores.Push import Push
from src.Instrucciones.Vectores.InsertVector import InsertVector
from src.Instrucciones.Vectores.Insert import Insert
from src.Instrucciones.Vectores.Remove import Remove
from src.Instrucciones.Vectores.Capacity import Capacity
from src.Instrucciones.Vectores.PushExp import PushExp
from src.Instrucciones.Vectores.VectorDafault import VectorDefault
from src.Instrucciones.Vectores.Contains import Contains









# manejo de la funcion main
from src.Instrucciones.Main.Main import FuncionMain



# menjo de entorno
from src.environment.Environment import Environment
from src.environment.Simbolo import Simbolo



from src.Error.Error import Error




# manejo de reporteria
tablaSimbolos = []
tablaErrores = []






# importacion para el manejo de la traduccion 3d
from src.environment3d.Enviroment3d import Environment3d
from src.environment.Simbolo3d import Simbolo3d









# ----------------------------------------------------------------
#                      Precedencia de Operadores
# ----------------------------------------------------------------
# precedencia de abajo hacia arriba
precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('right', 'UNOT'),
    ('left', 'IGUALDAD' ,'DIFERENTE'),
    ('left', 'MENOR', 'MAYOR', 'MAYORIGUAL', 'MENORIGUAL'),
    ('left', 'MAS', 'MENOS'),
    ('left', 'MULTIPLICAR', 'DIV', 'PORCENTAJE'),
    ('right', 'UMENOS')
    )








# ----------------------------------------------------------------
#                      Definicion de la Gramatica
# ----------------------------------------------------------------


def p_arranque_gramatica(p):
    ' arranque : instruccionGeneral '
    p[0] = p[1]



def p_lista_instrucciones_general(p):
    '   instruccionGeneral  :   instruccionGeneral  inicio   '
    p[1].append(p[2])
    p[0] = p[1]



def p_instruccion_general(p):
    '   instruccionGeneral  :   inicio  '
    p[0] = [p[1]] 






# ***********************************
#  INSTRUCCIONS DEL BLOQUE GENERAL
# ***********************************
def p_listado_gramatica_general(p):
    ''' inicio  :   fnMain
                |   funciones
                |   funcionesParametros '''
    p[0] = p[1]














# ********************************
#  CREACION DE LA FUNCION MAIN
# ********************************
def p_fn_main(p):
    #     0    1   2         3                    4                5              6              7
    ' fnMain : FN MAIN PARENTESISIZQUIERDO PARENTESISDERECHO LLAVEIZQUIERDO instrucciones LLAVEDERECHO '
    # print('se va ejecutar el main')
    p[0] = FuncionMain(
        p.lineno(1),
        columnToken(input, p.slice[1]),
        p[6]
    )




















# ***************************
#   INICIO DE LA GRAMATICA
# ***************************
# def p_inicio(p):
#     ''' inicio : instrucciones '''
#     p[0] = p[1]






# ***************************
#  GENERAR INSTRUCCIONES
# ***************************
def p_lista_instrucciones(p):
    ''' instrucciones : instrucciones instruccion '''
    p[1].append(p[2])
    p[0] = p[1]


def p_intrucciones(p):
    ''' instrucciones : instruccion '''
    p[0] = [p[1]]







# ***************************
#  INSTRUCCIONES DENTRO DEL LENGUAJE
# ***************************

def p_instruccion(p):
    ''' instruccion : imprimir  
                    | variable 
                    | asignacion
                    | instruccionif
                    | instruccionWhile 
                    | instruccionBreak
                    | instruccionContinue
                    | instruccionLoop
                    | instruccionFor
                    | funciones
                    | llamadofuncion
                    | funcionesParametros
                    | instruccionReturn
                    | alterValueArray
                    | instruccionFor2
                    | instruccionPush
                    | instruccionInsert '''
    p[0] = p[1]




# | instruccionStruct
# | alterValueStruct














# *************************************
#  RETORNOS PERMITIDOS EN EL LENGUAJE
# *************************************
def p_instruccion_break(p):
    ' instruccionBreak : BREAK PUNTOCOMA '
    p[0] = Primitivo(p.lineno(1), columnToken(input, p.slice[1]), TipoExpresion.BREAK, None)
    # p[0] = Simbolo3d(
    #     p.lineno(1),
    #     columnToken(input, p.slice[1]),
    #     None,
    #     TipoExpresion.BREAK,
    #     None,
    #     None,
    #     0,
    #     0
    #     )







def p_instruccion_continue(p):
    ' instruccionContinue : CONTINUE PUNTOCOMA '
    p[0] = Primitivo(p.lineno(1), columnToken(input, p.slice[1]), TipoExpresion.CONTINUE, None)
    # p[0] = Simbolo3d(
    #     p.lineno(1),
    #     columnToken(input, p.slice[1]),
    #     None,
    #     TipoExpresion.CONTINUE,
    #     None,
    #     None,
    #     0,
    #     0
    #     )






def p_instruccion_return(p):
    #       0              1     2     3
    ' instruccionReturn : RETURN exp PUNTOCOMA '
    p[0] = Primitivo(p.lineno(1), columnToken(input, p.slice[1]), TipoExpresion.RETURN, p[2])
    # p[0] = Simbolo3d(
    #     p.lineno(1),
    #     columnToken(input, p.slice[1]),
    #     None,
    #     TipoExpresion.RETURN,
    #     None,
    #     None,
    #     0,
    #     0
    #     )





# para poder manejar los remove en los returns
def p_instruccion_return_remove(p):
    #        0              1     2   3      4           5             6        7             8
    ' instruccionReturn : RETURN exp PUNTO REMOVE PARENTESISIZQUIERDO exp PARENTESISDERECHO PUNTOCOMA '
    p[0] = Remove(p[2], p[6])





























# ***************************
#   MANEJO DE FUNCIONES
# ***************************




# funciones void sin parametros
def p_funciones(p):
    #    0         1  2         3              4                   5             6            7
    ' funciones : FN ID PARENTESISIZQUIERDO PARENTESISDERECHO LLAVEIZQUIERDO instrucciones LLAVEDERECHO '
    p[0] = Funciones(p.lineno(1), columnToken(input, p.slice[1]), p[2], None, p[6], None ,tablaSimbolos)









# funciones con tipo sin parametros
def p_funciones_tipo(p):
    #    0         1  2         3              4                   5      6          7           8            9
    ' funciones : FN ID PARENTESISIZQUIERDO PARENTESISDERECHO TIPORETURN tipo LLAVEIZQUIERDO instrucciones LLAVEDERECHO '
    p[0] = Funciones(p.lineno(1), columnToken(input, p.slice[1]), p[2], None, p[8], p[6] ,tablaSimbolos)











# funciones con parametros
def p_funciones_parametros(p):
    #          0             1  2         3              4                   5             6            7           8
    ' funcionesParametros : FN ID PARENTESISIZQUIERDO parametros PARENTESISDERECHO LLAVEIZQUIERDO instrucciones LLAVEDERECHO '
    p[0] = Funciones(p.lineno(1), columnToken(input, p.slice[1]), p[2], p[4], p[7], None ,tablaSimbolos)








# funciones con tipo y con parametros
def p_funciones_parametros_tipo(p):
    #          0             1  2         3              4                5             6       7           8            9           10
    ' funcionesParametros : FN ID PARENTESISIZQUIERDO parametros PARENTESISDERECHO  TIPORETURN tipo  LLAVEIZQUIERDO instrucciones LLAVEDERECHO '
    p[0] = Funciones(p.lineno(1), columnToken(input, p.slice[1]), p[2], p[4], p[9], p[7] ,tablaSimbolos)






# listado de parametros
def p_lista_parametros(p):
    #        0           1        2           3 
    ''' parametros : parametros COMA instruccionParametro '''
    p[1].append(p[3])
    p[0] = p[1]


def p_parametros(p):
    ''' parametros : instruccionParametro '''
    p[0] = [p[1]]



def p_instruccion_parametro(p):
    #       0                 1    2       3
    ' instruccionParametro : ID DOSPUNTOS tipo '
    p[0] = Simbolo(0, 0, p[1], p[3], None, TipoMutable.MUTABLE) 











#  ---------------------------------
# llamado a funciones sin parametros
def p_llamado_funcion(p):
    #       0          1            2                3            4
    ' llamadofuncion : ID PARENTESISIZQUIERDO PARENTESISDERECHO PUNTOCOMA '
    p[0] = GetFuncion(p.lineno(2), columnToken(input, p.slice[2]), None, p[1], tablaErrores)





# llamado a funciones con parametros
def p_llamado_funcion_parametros(p):
    #       0          1            2                3            4                   5
    ' llamadofuncion : ID PARENTESISIZQUIERDO parametrosllamado PARENTESISDERECHO PUNTOCOMA '
    p[0] = GetFuncion(p.lineno(2), columnToken(input, p.slice[2]), p[3], p[1], tablaErrores)





# listado de parametros llamado a funcion(parametos)
def p_lista_parametros_llamado_funcion(p):
    #        0                 1               2           3 
    ''' parametrosllamado : parametrosllamado COMA instruccionLlamado '''
    p[1].append(p[3])
    p[0] = p[1]


def p_parametros_llamado_funcion(p):
    ''' parametrosllamado : instruccionLlamado '''
    p[0] = [p[1]]



def p_instruccion_parametro_llamado_funcion(p):
    #       0                 1 
    ' instruccionLlamado : exp '
    p[0] = p[1] 






























# ***************************
#   MANEJO DE STRUCTS
# ***************************

# # menejo de struct simple
# def p_struct(p):
#     #         0              1   2         3              4         5
#     ' instruccionStruct : STRUCT ID LLAVEIZQUIERDO listadoStruct LLAVEDERECHO '
#     p[0] = Struct(p.lineno(2), columnToken(input, p.slice[2]), p[2], p[4], tablaSimbolos)







# # para manejar el listado que se puede componer un struct
# def p_struct_listado(p):
#     ' listadoStruct : listadoStruct COMA elementoStruct '
#     p[1].append(p[3])
#     p[0] = p[1]






# def p_parametros_struct(p):
#     ' listadoStruct : elementoStruct  '
#     p[0] = [p[1]]






# def p_elemento_struct(p):
#     #        0          1   2         3  
#     ' elementoStruct : ID DOSPUNTOS tipo '
#     p[0] = Simbolo(
#         p.lineno(1), 
#         columnToken(input, p.slice[1]),
#         p[1],
#         p[3],
#         None,
#         TipoMutable.MUTABLE
#         )










# # build de structs
# # def p_build_struct(p):
# #     #    0           1         2            3          4            5
# #     ' buildStruct : ID LLAVEIZQUIERDO listadoBuild LLAVEDERECHO PUNTOCOMA '
# #     p[0] = BuildStruct(
# #         p.lineno(1),
# #         columnToken(input, p.slice[1]),
# #         p[1],
# #         p[3]
# #     )




# # para manejar el listado de los elementos de un struct
# def p_build_struct_listado(p):
#     ' listadoBuild : listadoBuild COMA elementoBuild '
#     p[1].append(p[3])
#     p[0] = p[1]






# def p_build_parametros_struct(p):
#     ' listadoBuild : elementoBuild  '
#     p[0] = [p[1]]
#     # p[0] = [None]





# def p_elemento_struct_build(p):
#     #        0           1     2        3 
#     ' elementoBuild :   ID  DOSPUNTOS   elementoStructBuild '    
#     p[0] = SimboloStruct(p[1],p[3])


# # def p_elemento_struct_build(p):
# #     #        0           1     2        3 
# #     ' elementoBuild :   ID  DOSPUNTOS   exp '    
# #     p[0] = SimboloStruct(p[1],p[3])




# # def p_elemento_struct_bulid_struct(p):
# #     ' elementoBuild : ID DOSPUNTOS ID LLAVEIZQUIERDO listadoBuild LLAVEDERECHO '
# #     p[0] = p[5]




# def p_expresion_struct(p):
#     ' elementoStructBuild : exp '
#     p[0] = p[1]



# # porbar acar retornar algo diferentes
# def p_struct_struct(p):
#     ' elementoStructBuild : ID LLAVEIZQUIERDO listadoBuild LLAVEDERECHO '
#     p[0] = BuildStruct(
#         p.lineno(1),
#         columnToken(input, p.slice[1]),
#         p[1],
#         p[3]
#     )








# # alteracion de valores dentro de un struct
# def p_alter_value_struct(p):
#     #      0              1   2    3   4    5
#     ' alterValueStruct : ID PUNTO ID IGUAL exp PUNTOCOMA '
#     p[0] = AsignacionStruct(
#         p.lineno(1),
#         columnToken(input, p.slice[1]),
#         p[1],
#         p[3],
#         p[5]
#     )





















# ***************************
#   MANEJO DE VECTORES
# ***************************
# def p_instruccion_push_vectores_struct(p):
#     #     0              1   2     3           4           5        6            7           8              9          
#     ' instruccionPush : ID PUNTO PUSH PARENTESISIZQUIERDO ID LLAVEIZQUIERDO listadoBuild LLAVEDERECHO PARENTESISDERECHO PUNTOCOMA '
#     p[0] = Push(p.lineno(3), columnToken(input, p.slice[3]), p[1], p[7])









def p_instruccion_push_vectores_exp(p):
    #     0              1   2     3           4            5        6        7           8           
    ' instruccionPush : ID PUNTO PUSH PARENTESISIZQUIERDO  exp  PARENTESISDERECHO PUNTOCOMA '
    p[0] = PushExp(p[1], p[5])







def p_instruccion_push_vectores_vectores(p):
    #     0              1   2     3           4           5   6   7           8             9           
    ' instruccionPush : ID PUNTO PUSH PARENTESISIZQUIERDO VEC NOT exp  PARENTESISDERECHO PUNTOCOMA '
    p[0] = PushExp(p[1], p[5])








def p_instruccion_insert_vectores(p):
    #     0                1    2     3             4          5    6   7         8               9
    ' instruccionInsert : ID PUNTO INSERT PARENTESISIZQUIERDO exp COMA exp PARENTESISDERECHO PUNTOCOMA '
    p[0] = Insert(p[1], p[5], p[7])












def p_expresion_capacity_vectores(p):
    #  0     1    2      3
    ' instruccionCapacity : ID PUNTO CAPACITY PARENTESISIZQUIERDO PARENTESISDERECHO '
    p[0] = Capacity(p[1])









# # vec.contais(exp);
# def p_expresion_contains(p):
#     #          0             1    2      3           4              5        6          7
#     ' instruccionContains : ID PUNTO CONTAINS PARENTESISIZQUIERDO AMPERSAND exp PARENTESISDERECHO '
#     p[0] = Contains(p[1], p[6])



















# ***************************
#   IMPRESION PERMITIDAS
# ***************************
def p_imprimir(p):
    #  imprimir = println ( exp ) 
    #    0         1      2            3          4           5          6
    ' imprimir : PRINTLN NOT PARENTESISIZQUIERDO exp PARENTESISDERECHO PUNTOCOMA '
    p[0] = Imprimir(p[4], None)







def p_imprimir_elementos(p):
    #  imprimir = println ( exp ) 
    #    0         1      2            3          4    5        6          7                8
    ' imprimir : PRINTLN NOT PARENTESISIZQUIERDO exp COMA listadoprint PARENTESISDERECHO PUNTOCOMA '
    p[0] = Imprimir(p[4], p[6])






def p_lista_imprimir(p):
    ' listadoprint : listadoprint COMA exp '
    p[1].append(p[3])
    p[0] = p[1]






def p_print(p):
    ' listadoprint : exp '
    p[0] = [p[1]]




# para permitir la impresion del capacity
def p_print_capacity(p):
    ' listadoprint : instruccionCapacity'
    p[0] = [p[1]]











# def p_imprimir_structs(p):
#     #  imprimir = println ( exp ) 
#     #    0         1      2            3          4    5    6    7       8 
#     ' imprimir : PRINTLN NOT PARENTESISIZQUIERDO exp COMA  ID PUNTO listaAcces  PARENTESISDERECHO PUNTOCOMA '
#     p[0] = Imprimir(
#         p[4], 
#         [Simbolo(
#             p.lineno(1), 
#             columnToken(input, p.slice[1]), 
#             p[6],
#             TipoExpresion.STRUCT, 
#             p[8],
#             TipoMutable.MUTABLE
#             )]
#         )




# def p_q(p):
#     'listaAcces : listaAcces PUNTO elementoAcces'
#     p[1].append(p[3])
#     p[0] = p[1]



# def p_u(p):
#     'listaAcces : elementoAcces'
#     p[0] = [p[1]]



# def p_print_accesStruct(p):
#     #           0    1    2   3
#     ' elementoAcces : ID '
#     p[0] = p[1]




# # terminal
# def p_print_accesStruct(p):
#     #           0    1    2   3
#     ' elementoAcces : ID PUNTO ID '
#     p[0] = Simbolo(
#             p.lineno(1), 
#             columnToken(input, p.slice[1]), 
#             p[1],
#             TipoExpresion.STRUCT, 
#             p[3],
#             TipoMutable.MUTABLE
#             )



































# ***************************
#  DECLARACION DE VARIABLES
# ***************************

#  mutable 
def p_variables_mut_tipo(p):
    #     0              1   2   3   4        5    6      7    8
    '''  variable   :   LET MUT ID DOSPUNTOS tipo IGUAL exp PUNTOCOMA  '''

    # print(p[5])
    p[0] = Declaracion(p.lineno(1), columnToken(input, p.slice[1]), p[3], p[5], p[7], TipoMutable.MUTABLE ,tablaSimbolos, tablaErrores)




def p_variables_mut(p):
    #     0              1   2   3   4    5      6    
    '''  variable   :   LET MUT ID IGUAL exp PUNTOCOMA  '''
    p[0] = Declaracion(p.lineno(1), columnToken(input, p.slice[1]), p[3], None, p[5], TipoMutable.MUTABLE ,tablaSimbolos, tablaErrores)





# no mutables
def p_variables_tipo(p):
    #     0              1   2   3        4     5    6    7 
    '''  variable   :   LET ID DOSPUNTOS tipo IGUAL exp PUNTOCOMA  '''
    p[0] = Declaracion(p.lineno(1), columnToken(input, p.slice[1]), p[2], p[4], p[6], TipoMutable.NOMUTABLE, tablaSimbolos, tablaErrores)






def p_variables(p):
    #     0              1  2  3      4     5       
    '''  variable   :   LET ID IGUAL exp PUNTOCOMA  '''
    p[0] = Declaracion(p.lineno(1), columnToken(input, p.slice[1]), p[2], None, p[4], TipoMutable.NOMUTABLE, tablaSimbolos, tablaErrores)












# *********************** VECTORES DECLRADOS EN VARIABLES ****
# MANEJO PARA ASIGNAR VECTORES EN VARIABLES
# MANEJO PARA ASIGNAR VECTORES EN VARIABLES



def p_variable_mut_vector(p):
    #     0        1   2   3      4      5     6     7    8      9     10    11          12   13       14               15
    '  variable : LET MUT ID  DOSPUNTOS tipo  IGUAL VEC DOSPUNTOS DOSPUNTOS NEW PARENTESISIZQUIERDO PARENTESISDERECHO PUNTOCOMA '
    p[0] = VariableVector(p.lineno(1), columnToken(input, p.slice[1]), p[3], p[5], TipoMutable.MUTABLE)








def p_variable_mut_vector_capacity(p):
    #     0        1   2   3      4      5      6    7      8          9        10               11           12          13           14 
    '  variable : LET MUT ID  DOSPUNTOS tipo  IGUAL VEC DOSPUNTOS DOSPUNTOS WITH_CAPACITY PARENTESISIZQUIERDO exp PARENTESISDERECHO PUNTOCOMA '
    p[0] = VariableVectorCapacity(p.lineno(1), columnToken(input, p.slice[1]), p[3], p[5], TipoMutable.MUTABLE, p[12])






# vec![ exp; exp ]
def p_variable_mut_vec(p):
    #     0        1   2   3      4      5      6    7    8    9      10         
    '  variable : LET MUT ID  DOSPUNTOS tipo  IGUAL VEC  NOT  exp  PUNTOCOMA '
    p[0] = VariableVectorExp(p.lineno(1), columnToken(input, p.slice[1]), p[3], p[5], TipoMutable.MUTABLE,p[9])




# vec![ exp; exp ]
def p_variable_mut_sintipo_vec(p):
    #     0        1   2   3     4    5    6       7       8          
    '  variable : LET ID  IGUAL VEC  NOT  exp  PUNTOCOMA '
    p[0] = VariableVectorExp(p.lineno(1), columnToken(input, p.slice[1]), p[2], None, TipoMutable.MUTABLE,p[6])


# **********************************








# declaracion de struct sin tipo en variable
# def p_variables_mut_struct(p):
#     #     0              1   2   3   4    5      6            7           8            9  
#     '''  variable   :   LET MUT ID IGUAL ID LLAVEIZQUIERDO listadoBuild LLAVEDERECHO PUNTOCOMA  '''
#     p[0] = Declaracion(
#         p.lineno(1), columnToken(input, p.slice[1]), 
#         p[3], 
#         None, 
#         BuildStruct(
#             p.lineno(5),
#             columnToken(input, p.slice[5]),
#             p[5],
#             p[7])
#         , 
#         TipoMutable.MUTABLE,
#         tablaSimbolos,
#         tablaErrores
#         )



# delcaracion de struct en varibles con tipo
# def p_variables_mut_tipo_struct(p):
#     #     0              1   2   3   4       5    6    7     8             9            10           11 
#     '''  variable   :   LET MUT ID DOSPUNTOS ID IGUAL ID LLAVEIZQUIERDO listadoBuild LLAVEDERECHO PUNTOCOMA  '''
#     print(f' --> {p.slice[5]}')
#     p[0] = Declaracion(
#         p.lineno(1), columnToken(input, p.slice[1]),
#         p[3], 
#         p[5], 
#         BuildStruct(
#             p.lineno(7),
#             columnToken(input, p.slice[7]),
#             p[7],
#             p[9])
#         ,  
#         TipoMutable.MUTABLE,
#         tablaSimbolos,
#         tablaErrores
#         )















# ---------------------- ** -------------------------





# MANEJO PARA ASIGNAR VECTORES EN VARIABLES
def p_variable_vector(p):
    #     0        1   2      3      4    5    6     7      8    9     10        11     12          13                 14            15
    '  variable : LET ID  DOSPUNTOS VEC MENOR tipo MAYOR  IGUAL VEC DOSPUNTOS DOSPUNTOS NEW PARENTESISIZQUIERDO PARENTESISDERECHO PUNTOCOMA '
    p[0] = VariableVector(p.lineno(1), columnToken(input, p.slice[1]), p[2], p[6], TipoMutable.NOMUTABLE)











# declaracion de struct en varialbes sin tipo sin mut
# def p_variables_tipo_struct(p):
#     #     0              1  2  3      4        5             6           7          8       
#     '''  variable   :   LET ID IGUAL  ID LLAVEIZQUIERDO listadoBuild LLAVEDERECHO PUNTOCOMA '''
#     p[0] = Declaracion(
#         p.lineno(1), columnToken(input, p.slice[1]), 
#         p[2], 
#         None, 
#         BuildStruct(
#             p.lineno(4),
#             columnToken(input, p.slice[4]),
#             p[4],
#             p[6])
#         , 
#         TipoMutable.NOMUTABLE,
#         tablaSimbolos,
#         tablaErrores
#         )




# delcaracion de struct en varibles sin tipo y sin mut
# def p_variables_mut_tipo_struct(p):
#     #     0              1   2   3       4   5    6        7            8             9          10  
#     '''  variable   :   LET ID DOSPUNTOS ID IGUAL ID LLAVEIZQUIERDO listadoBuild LLAVEDERECHO PUNTOCOMA  '''
#     print(f' --> {p.slice[5]}')
#     p[0] = Declaracion(
#         p.lineno(1), 
#         columnToken(input, p.slice[1]), 
#         p[2], 
#         p[4], 
#         BuildStruct(
#             p.lineno(7),
#             columnToken(input, p.slice[7]),
#             p[6],
#             p[8])
#         ,  
#         TipoMutable.MUTABLE,
#         tablaSimbolos,
#         tablaErrores
#         )





























# ****************************************
#  ASIGNACION DE VALORES A UNA VARIABLE
# ****************************************
def p_asignacion_variables(p):
    #    0         1   2     3    4
    ' asignacion : ID IGUAL exp PUNTOCOMA '
    p[0] = Asignacion(p.lineno(2), columnToken(input, p.slice[2]), p[1], p[3], tablaErrores)

























# ****************************************
#  INSTRUCCIONE PARA MANEJO DEL IF
# ****************************************
def p_instruccion_if(p):
    #   0              1   2        3             4                5             6
    ' instruccionif : IF exp LLAVEIZQUIERDO   instrucciones   LLAVEDERECHO  instruccionElse'
    p[0] = InstruccionIf(p.lineno(1), columnToken(input, p.slice[1]), p[2], p[4], p[6])






def p_instruccion_else(p):
    #    0                 1        2           3              4        
    ''' instruccionElse : ELSE LLAVEIZQUIERDO instrucciones LLAVEDERECHO '''    
    p[0] = InstruccionElse(p.lineno(1), columnToken(input, p.slice[1]),  p[3])






def p_instruccion_else_if(p):
    #    0                 1         2                  
    ''' instruccionElse : ELSE instruccionif
                        | '''
    # print(len(p))
    if len(p) > 2:
        p[0] = p[2]
    else:
        p[0] = None




















# ****************************************
#  INSTRUCCIONE PARA MANEJO DEL WHILE
# ****************************************
def p_instruccion_while(p):
    #    0                1     2        3             4          5
    ' instruccionWhile : WHILE exp LLAVEIZQUIERDO instrucciones LLAVEDERECHO '
    p[0] = While(p.lineno(1), columnToken(input, p.slice[1]), tablaErrores, p[2], p[4])






















# ****************************************
#  INSTRUCCIONE PARA MANEJO DEL LOOP
# ****************************************
def p_instruccion_loop(p):
    #    0                1          2              3          4
    ' instruccionLoop : LOOP LLAVEIZQUIERDO instrucciones LLAVEDERECHO '
    p[0] = Loop(p.lineno(1), columnToken(input, p.slice[1]), p[3])





















# ****************************************
#  INSTRUCCIONE PARA MANEJO DEL FOR IN
# ****************************************
def p_instruccion_forin(p):
    #    0              1   2  3   4   5     6     7       8             9             10 
    ' instruccionFor : FOR exp IN exp PUNTO PUNTO exp LLAVEIZQUIERDO instrucciones LLAVEDERECHO '
    p[0] = Forin(0, 0, tablaErrores, p[2], p[4], p[7], p[9])












def p_instruccion_forin_arreglos(p):
    #       0            1   2   3  4        5             6             7
    ' instruccionFor2 : FOR exp IN exp LLAVEIZQUIERDO instrucciones LLAVEDERECHO '
    p[0] = ForinArreglos(
        p.lineno(1),
        columnToken(input, p.slice[1]),
        p[2], # pivote
        p[4], # variable a recorrer
        p[6]  # instrucciones
    )





















# ******************************************
#  INSTRUCCIONE PARA MANEJO DE LOS ARREGLOS
# ******************************************

# def p_expresion_arreglo(p):
#     #     0                  1               2                3
#     ' expresionArreglo : CORCHETEDERECHO listadoArreglo CORCHETEIZQUIERDO '
#     p[0] = ExpArreglo(
#         p.lineno(1),
#         columnToken(input, p.slice[1]),
#         p[2]
#     )




# genera el listado de exp
def p_listado_arreglo(p):
    ' listadoArreglo : listadoArreglo COMA exp '
    p[1].append(p[3])
    p[0] = p[1]





def p_elemento_arreglo(p):
    ' listadoArreglo : exp '
    p[0] = [p[1]]










# def modificar datos de un arreglo
# alterar valores de un arreglo 
def p_alter_value_arregle(p):
    #     0             1   2      3    4              
    ' alterValueArray : ID list IGUAL exp PUNTOCOMA '
    p[0] = ModificarValorArreglo(
        p.lineno(3),
        columnToken(input, p.slice[3]),
        tablaErrores,
        p[1], #id
        p[2], #lista
        p[4]  #exp
    )




def p_list(p):
    ' list : list CORCHETEDERECHO exp CORCHETEIZQUIERDO'
    p[1].append(p[3])
    p[0] = p[1]





def p_list2(p):
    ' list : CORCHETEDERECHO exp CORCHETEIZQUIERDO '
    p[0] = [p[2]]
































# ***************************
#   ACEPTACION DE TIPOS
# ***************************
def p_tipos(p):
    '''  tipo   :   I64
                |   F64 
                |   BOOL 
                |   STRING
                |   CHAR
                |   ID
                |   USIZE
                |   CORCHETEDERECHO  tipo  CORCHETEIZQUIERDO  '''

    # print(p.slice[1].type)USIZE

    if p.slice[1].type == 'I64' or p.slice[1].type == 'USIZE':
        p[0] = TipoExpresion.INTEGER


    elif p.slice[1].type == 'F64':
        p[0] = TipoExpresion.FLOAT


    elif p.slice[1].type == 'BOOL':
        p[0] = TipoExpresion.BOOL


    elif p.slice[1].type == 'STRING':
        p[0] = TipoExpresion.STRING


    elif p.slice[1].type == 'CHAR':
        p[0] = TipoExpresion.CHAR



    elif p.slice[1].type == 'ID':
        p[0] = TipoExpresion.STRUCT


    else:
        p[0] = TipoExpresion.ARREGLO




def p_tipo_vector(p):
    ' tipo : VEC MENOR tipo MAYOR'
    p[0] = TipoExpresion.VECTOR





def p_tipos_appersand_mut(p):
    ' tipo : AMPERSAND MUT tipo'
    p[0] = p[3]






# TIPO ARREGLO
# [tipo;exp]
def p_tipo_arreglo(p):
    #  0           1            2      3      4        5
    ' tipo : CORCHETEDERECHO  tipo PUNTOCOMA exp CORCHETEIZQUIERDO '
    # p[0] = TipoArreglo(
    #     p.lineno(1), 
    #     columnToken(input, p.slice[1]),
    #     p[2],
    #     p[4]
    # )
    p[0] = TipoExpresion.ARREGLO


























# **************************************
#   OPERACIONES ACPETADAS - EXPRESIONES
# **************************************

def p_aritmetica(p):
    # aritmetica + prim
    ''' exp : exp MAS exp 
            | exp MENOS exp 
            | exp MULTIPLICAR exp 
            | exp DIV exp
            | exp PORCENTAJE exp
            | exp MAYOR exp 
            | exp MENOR exp 
            | exp MAYORIGUAL exp 
            | exp MENORIGUAL exp 
            | exp IGUALDAD exp
            | exp DIFERENTE exp
            | exp OR exp
            | exp AND exp '''

    if p[2] == '+':
        # p[0] = p[1] + p[3]
        p[0] = Aritmetica(0, 0,  p[1], TipoOperador.MAS ,p[3])

    elif p[2] == '-':
        # p[0] = p[1] - p[3]
        p[0] = Aritmetica(0, 0,  p[1], TipoOperador.MENOS ,p[3])

    elif p[2] == '*':
        # p[0] = p[1] * p[3]
        p[0] = Aritmetica(0, 0,  p[1], TipoOperador.POR, p[3])
        
    elif p[2] == '/':
        # p[0] = p[1] / p[3]
        p[0] = Aritmetica(0, 0,  p[1], TipoOperador.DIV, p[3])

    elif p[2] == '%':
        # p[0] = p[1] % p[3]
        p[0] = Aritmetica(0, 0, p[1], TipoOperador.PORCENTAJE, p[3])


    elif p[2] == '>':
        # p[0] = p[1] > p[3]
        p[0] = Relacional(0, 0,  p[1], TipoRelacional.MAYORQUE, p[3])

    elif p[2] == '<':
        # p[0] = p[1] < p[3]
        p[0] = Relacional(0, 0,  p[1], TipoRelacional.MENORQUE, p[3])


    elif p[2] == '>=':
        # p[0] = p[1] >= p[3]
        p[0] = Relacional(0, 0,  p[1], TipoRelacional.MAYORIGUALQUE, p[3])


    elif p[2] == '<=':
        # p[0] = p[1] <= p[3]
        p[0] = Relacional(0, 0,  p[1], TipoRelacional.MENORIGUALQUE, p[3])


    elif p[2] == '==':
        # p[0] = p[1] == p[3]
        p[0] = Relacional(0, 0,  p[1], TipoRelacional.IGUALDAD, p[3])


    elif p[2] == '!=':
        # p[0] = p[1] == p[3]
        p[0] = Relacional(0, 0,  p[1], TipoRelacional.DIFERENTE, p[3])


    elif p[2] == '||':
        # p[0] = p[1] || p[3]
        p[0] = Logico(0, 0, p[1], TipoLogico.OR, p[3])


    
    elif p[2] == '&&':
        # p[0] = p[1] || p[3]
        p[0] = Logico(0, 0, p[1], TipoLogico.AND, p[3])


    

# manejo de casteos para expresiones
def p_casteos(p):
    ''' exp :   exp AS I64 
        exp :   exp AS F64   
        exp :   exp AS USIZE   '''

    if p.slice[3].type == 'I64' or p.slice[3].type == 'USIZE':
        p[0] = Casteo(0,0, p[1], TipoExpresion.INTEGER)

    
    if p.slice[3].type == 'F64':
        p[0] = Casteo(0,0, p[1], TipoExpresion.FLOAT)




# manejo para funciones nativas
def p_funcion_nativa_tostring(p):
    ' exp : exp PUNTO TO_STRING PARENTESISIZQUIERDO PARENTESISDERECHO'
    p[0] = Nativas(0, 0, p[1], TipoNativas.TOSTRING)



# exp.ABS()
def p_funcion_nativa_abs(p):
    ' exp : exp PUNTO ABS PARENTESISIZQUIERDO PARENTESISDERECHO '
    p[0] = Nativas(0, 0, p[1], TipoNativas.ABS)



#    exp.SQRT()
def p_funcion_nativa_sqrt(p):
    ' exp : exp PUNTO SQRT PARENTESISIZQUIERDO PARENTESISDERECHO '
    p[0] = Nativas(0, 0, p[1], TipoNativas.SQRT)



#    exp.CLONE()
def p_funcion_nativa_clone(p):
    ' exp : exp PUNTO CLONE PARENTESISIZQUIERDO PARENTESISDERECHO '
    p[0] = Nativas(0, 0, p[1], TipoNativas.CLONE)





# operaciones unitarias con precedencia
def p_logica_unitaria(p):
    ' exp : NOT exp %prec UNOT '
    p[0] = Logico(0, 0, p[2], TipoLogico.NOT, None) 


def p_aritmetica_unaria(p):
    ' exp : MENOS exp %prec UMENOS '
    p[0] = Negativo(0, 0, p[2])





# exp en una agrupacion
def p_aritmetica_agrupacion(p):
    ' exp : PARENTESISIZQUIERDO exp PARENTESISDERECHO '
    # ( exp )
    p[0] = p[2] 






# exp retornoa una potencia
def p_aritmetica_potencia(p):
    ''' exp : I64 DOSPUNTOS DOSPUNTOS POW PARENTESISIZQUIERDO exp COMA exp PARENTESISDERECHO 
            | F64 DOSPUNTOS DOSPUNTOS POW PARENTESISIZQUIERDO exp COMA exp PARENTESISDERECHO '''
    if p[1] == 'i64':
        p[0] = Pow(0, 0, TipoExpresion.INTEGER, p[6], p[8])	

    elif p[1] == 'f64':
        p[0] = Pow(0, 0, TipoExpresion.FLOAT, p[6], p[8])	






# exp retorno un primitivo
def p_expresion(p):
    ' exp : primitivo '
    p[0] = p[1]








# exp tipo espcial
# exp para funciones
def p_expresion_llamada_funcion(p):
    ' exp : ID PARENTESISIZQUIERDO PARENTESISDERECHO '
    p[0] = GetFuncion(p.lineno(2), columnToken(input, p.slice[2]), None, p[1], tablaErrores)



def p_expresion_llamada_funcion_parametros(p):
    ' exp : ID PARENTESISIZQUIERDO parametrosllamado PARENTESISDERECHO '
    p[0] = GetFuncion(p.lineno(2), columnToken(input, p.slice[2]), p[3], p[1], tablaErrores)









# [ LISTADOEPXRESIONES ]
# arreglos como expresiones
def p_expresion_arreglo(p): 
    ' exp : CORCHETEDERECHO listadoArreglo CORCHETEIZQUIERDO  '
    p[0] = ExpArreglo(
        p.lineno(1),
        columnToken(input, p.slice[1]),
        p[2]
    )





# exp para acceso hacia los arreglos
# expresion para impresion de arreglos
# exp [ exp ]
# exp [exp][exp]

def p_expresion_acceso_arreglo(p):
    # 0      1         2         3        4
    ' exp : exp CORCHETEDERECHO exp CORCHETEIZQUIERDO '
    p[0] = AcessArreglo(
        p.lineno(2),
        columnToken(input, p.slice[2]),
        tablaErrores,
        p[1],
        p[3]
    )








# exp para len de arreglos
def p_expresion_len_arreglo(p):
    ' exp : exp PUNTO LEN PARENTESISIZQUIERDO PARENTESISDERECHO '
    p[0] = Len(p[1])







# vec.contais(exp);
def p_expresion_contains(p):
    #  0     1    2      3             4                5     6          7
    ' exp : exp PUNTO CONTAINS PARENTESISIZQUIERDO AMPERSAND exp PARENTESISDERECHO '
    p[0] = Contains(p[1], p[6])







# vector por defecto vec![exp; exp]
def p_expresion_vector_lleno(p):
    #  0     1   2        3          4      5      6         7
    ' exp : VEC NOT CORCHETEDERECHO exp PUNTOCOMA exp CORCHETEIZQUIERDO '
    p[0] = VectorDefault(p[4], p[6])







































# ***************************
#   VALORES ACPETADOS
# ***************************

def p_valor(p):
    ''' primitivo   : ENTERO 
                    | DECIMAL
                    | TRUE
                    | FALSE
                    | CADENA
                    | CARACTER 
                    | ID '''

    if p.slice[1].type == 'ENTERO': 
        p[0] = Primitivo(p.lineno(1), columnToken(input, p.slice[1]), TipoExpresion.INTEGER, p[1])
    
    elif p.slice[1].type == 'DECIMAL':
        p[0] = Primitivo(p.lineno(1), columnToken(input, p.slice[1]), TipoExpresion.FLOAT, p[1])
    
    elif p.slice[1].type == 'TRUE':
        p[0] = Primitivo(p.lineno(1), columnToken(input, p.slice[1]), TipoExpresion.BOOL, '1')

    elif p.slice[1].type == 'FALSE':
        p[0] = Primitivo(p.lineno(1), columnToken(input, p.slice[1]), TipoExpresion.BOOL, '0')

    elif p.slice[1].type == 'CADENA':
        p[0] = Primitivo(p.lineno(1), columnToken(input, p.slice[1]), TipoExpresion.STRING, p[1])


    elif p.slice[1].type == 'CARACTER':
        p[0] = Primitivo(p.lineno(1), columnToken(input, p.slice[1]), TipoExpresion.CHAR, p[1])


    elif p.slice[1].type == 'ID':
        p[0] = Primitivo(p.lineno(1), columnToken(input, p.slice[1]), TipoExpresion.ID, p[1])

















# ***************************
#   ERRORES CAPTURADOS
# ***************************

def p_error(p):
    print(f'Error sintactico en -> {p.value} linea: {p}')


















# ***************************
#   ARRANQUE DE LA GRAMATICA 
# ***************************

import Compiler.ply.yacc as yacc
parser = yacc.yacc()


def analizar(entrada):
    input = entrada
    lista = parser.parse(entrada)
    # print(lista)

    # entorno principal declarado
    env = Environment('general', 0, None)

    tablaSimbolos.append(['Ambito','env','env','general',0,0])

    salida = ""
    for l in lista:
        # print(f'lista {l}')
        result = l.ejecutar(env)
        if result != None and isinstance(result, str):
            salida += str(result) + "\n"

    return salida, tablaSimbolos, tablaErrores








# funcion para devolver la traduccion en 3d
def traduccir3d(entrada):
    input = entrada
    lista = parser.parse(entrada)

    # traductor 3d
    traductor3d = Environment3d()

    cadena3d = ''
    

    # entorno principal declarado
    env = Environment('general', 0, None)

    salida = ''
    for l in lista:
        l.traducir(env, traductor3d, cadena3d)

    traductor3d.cabecera()
    return traductor3d.getCadena()







# funcion para devolver la traduccion en 3d
def traduccir3doptimizado(entrada):
    input = entrada
    lista = parser.parse(entrada)

    # traductor 3d
    traductor3d = Environment3d()

    cadena3d = ''
    

    # entorno principal declarado
    env = Environment('general', 0, None)

    salida = ''
    for l in lista:
        l.optimizar(env, traductor3d, cadena3d)

    traductor3d.cabecera()
    return traductor3d.getCadena()






# if __name__ == '__main__':
#     # Build the parser
#     # import ply.yacc as yacc
#     # parser = yacc.yacc()
#
#     f = open('./entrada.txt')
#     contenido = f.read()
#
#     # result = parser.parse(contenido)
#     print(analizar(contenido))
