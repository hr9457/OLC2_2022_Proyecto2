# from Sintactico import analizar
from Compiler.Sintactico import analizar


def saludo():
    print('hola desde prueba.py')
    # f = open('./entrada.txt')
    # contenido = f.read()
    contenido = '3+3'
    # result = parser.parse(contenido)
    print(analizar(contenido))

# from Sintactico import analizar
# #
# if __name__ == '__main__':
#
#     f = open('./entrada.txt')
#     contenido = f.read()
#
#     # result = parser.parse(contenido)
#     print(analizar(contenido))