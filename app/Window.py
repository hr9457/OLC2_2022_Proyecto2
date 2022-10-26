import sys
import tkinter as tk
from tkinter import *
from app.TablaSimbolos import *
from app.Errores import *
from app.optimizacion import *


# Importacion del Analizador
from Compiler import Sintactico

# posiciones N(arriba), E(derecha), S(abajo), W(izquierda)
class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()
        # para obtener medidas de la pantalla para la ventana
        self.altoPantalla = self.ventana.winfo_screenheight()
        self.anchoPantalla = self.ventana.winfo_screenwidth()
        self.alto = int(self.altoPantalla-150)
        self.ancho = int(self.anchoPantalla-200)

        # formatos para la ventana de la app
        self.ventana.geometry(f'{self.ancho}x{self.alto}')
        self.ventana.title('OLC2-PROYECTO1')
        self.ventana['bg'] = '#49A'


        # utilidades para generar reportes
        self.tablaSimbolos = []
        self.tablaErrores = []
        self.tablaOptimizacion = []


        # llamado al menu principal
        self.crearMenu()

        # configuracion del area de trabajo
        self.ventana.rowconfigure(0, minsize=self.alto, weight=1)
        self.ventana.columnconfigure(1, weight=1)
        self.ventana.columnconfigure(2, minsize=30)
        self.ventana.columnconfigure(3, weight=1)

        # creacon y agregacion de los componentes
        self.crearComponentes()

        # corra la applicacion
        self.ventana.mainloop()


    # --------------------------------------------
    # FUNCIONES PARA LAS ACCIONES DE LA VENTANA

    # funcionalidad para compilar
    def compilar(self):
        print('compilando Entrada')
        entrada = self.textAreaEntrada.get(1.0, END)
        # print(entrada)
        result = Sintactico.analizar(entrada)
        # print(result)

        self.tablaSimbolos = result[1]
        self.tablaErrores = result[2]

        self.textAreaSalida.delete(1.0, END)
        self.textAreaSalida.insert(1.0, result[0])
        



    # funcionalidad para salir
    def salir(self):
        self.ventana.quit()
        self.ventana.destroy()
        sys.exit()




    # funcionalidad para traduccir a 3d
    def traducir3d(self):
        print('TRADUCCION A 3D')
        entrada = self.textAreaEntrada.get(1.0,END)
        result3d = Sintactico.traduccir3d(entrada)

        self.tablaSimbolos = result3d[1]
        self.tablaErrores = result3d[2]

        self.textAreaSalida.delete(1.0,END)
        self.textAreaSalida.insert(1.0,result3d[0])





    # funcionalidad para traduccir a 3d
    def optimizacion3d(self):
        print('OPTIMIZAR EN 3d')
        entrada = self.textAreaEntrada.get(1.0,END)
        result3d = Sintactico.traduccir3doptimizado(entrada)
        self.txtAreaOptimizacion.delete(1.0,END)
        self.txtAreaOptimizacion.insert(1.0,result3d)





    def ejecutarTraducciones3d(self):
        print('TRADUCCION A 3D')
        entrada = self.textAreaEntrada.get(1.0,END)
        result3d = Sintactico.traduccir3d(entrada)

        self.tablaSimbolos = result3d[1]
        self.tablaErrores = result3d[2]

        self.textAreaSalida.delete(1.0,END)
        self.textAreaSalida.insert(1.0,result3d[0])


        print('OPTIMIZAR EN 3d')
        entrada = self.textAreaEntrada.get(1.0,END)
        result3d_optimizado = Sintactico.traduccir3doptimizado(entrada)
        self.txtAreaOptimizacion.delete(1.0,END)
        self.txtAreaOptimizacion.insert(1.0,result3d_optimizado)







    # ------------------------------
    # funcionalidad para reportes
    def reporteErrores(self):
        print('Reporte de error')





    def reporteSemantico(self):
        generarTablaErrores(self.tablaErrores)





    def tablaSimbolo(self):
        generarTablaSimbolos(self.tablaSimbolos)



    def reporte_optimizacion(self):
        print('Generacion de reporte de optimizacion')
        reporteOptimizacion(self.tablaOptimizacion)


    def tablaBD(self):
        print('Reporte de taba de BD')

    # ---------------------------------




    # menu principal
    def crearMenu(self):
        menuPrincipal = Menu(self.ventana)
        menuPrincipal['bg'] = '#49A'

        # subMenu para manejo de archivos
        subMenuArchivo = Menu(menuPrincipal, tearoff=False)
        subMenuArchivo.add_command(label='Abrir')
        subMenuArchivo.add_separator()
        subMenuArchivo.add_command(label='Salir',command=self.salir)
        
        # subMenu para menjo de reportes
        subMenuReportes = Menu(menuPrincipal, tearoff=False)
        subMenuReportes.add_command(label='Tabla Simbolos', command=self.tablaSimbolo)
        subMenuReportes.add_command(label='Tabla de Errores', command=self.reporteSemantico)
        subMenuReportes.add_command(label='Optimizacion', command=self.reporte_optimizacion)

        menuPrincipal.add_cascade(menu=subMenuArchivo, label='Archivo')
        menuPrincipal.add_cascade(menu=subMenuReportes, label='Reportes')
        self.ventana.config(menu=menuPrincipal)




    #  creacion de componentes
    def crearComponentes(self):
        frameBotones = Frame(relief=RAISED, bd=2)
        frameBotones['bg'] = '#49A'
        botonAbrir = Button(frameBotones, text='Abrir')
        botonCompilar = Button(frameBotones, text='Compilar', command=self.compilar)
        boton3d = Button(frameBotones, text='3d', command=self.ejecutarTraducciones3d)

        # expasion de los botones de forma horizontal (stiky)
        botonAbrir.grid(row=0, column=0, sticky='WE', padx=5, pady= 5)
        botonCompilar.grid(row=1, column=0, sticky='WE', padx=5, pady=5)
        boton3d.grid(row=2, column=0, sticky='WE', padx=5, pady=5)
        frameBotones.grid(row=0, column=0, sticky='NS')


        frameEntrada = Frame(relief=RAISED, bd=1)
        frameEntrada.rowconfigure(0, minsize=self.alto, weight=1)
        frameEntrada.columnconfigure(0, weight=1)

        self.textAreaEntrada = Text(frameEntrada, wrap=WORD , font=('Consolas',12))
        self.textAreaEntrada.grid(row=0, column=0, sticky='nswe')

        scrollbar = Scrollbar(frameEntrada, orient='vertical', command=self.textAreaEntrada.yview)
        scrollbar.grid(row=0, column=1, sticky='ns')
        self.textAreaEntrada['yscrollcommand'] = scrollbar.set


        scrollbar2 = Scrollbar(frameEntrada, orient='horizontal', command=self.textAreaEntrada.xview)
        scrollbar2.grid(row=1, column=0, sticky='we')
        self.textAreaEntrada['xscrollcommand'] = scrollbar2.set

        frameEntrada.grid(row=0, column=1, sticky='nswe')




        separador = Frame(relief=RAISED, bd=1)
        separador.grid(row=0, column=2, sticky='ns')




        # FRAME QUE CONTIENE LOS TXT DE SALIDA 


        frameSalida = Frame(relief=RAISED, bd=1)
        frameSalida.rowconfigure(0, minsize=self.alto/2, weight=1)
        frameSalida.rowconfigure(1, minsize=self.alto/2, weight=1)
        frameSalida.columnconfigure(0,weight=1)



        self.textAreaSalida = Text(frameSalida, wrap=WORD, font=('Consolas',12))
        self.textAreaSalida.grid(row=0, column=0, sticky='nswe')


        self.txtAreaOptimizacion = Text(frameSalida, wrap=WORD, font=('Consolas',12))
        self.txtAreaOptimizacion.grid(row=1, column=0, sticky='nswe')


        scrollbar3 = Scrollbar(frameSalida, orient='vertical', command=self.textAreaSalida.yview)
        scrollbar3.grid(row=0, column=1, sticky='ns')
        self.textAreaSalida['yscrollcommand'] = scrollbar3.set	



        scrollbar4 = Scrollbar(frameSalida, orient='vertical', command=self.txtAreaOptimizacion.yview)
        scrollbar4.grid(row=1, column=1, sticky='ns')
        self.txtAreaOptimizacion['yscrollcommand'] = scrollbar4.set	



        frameSalida.grid(row=0, column=3, sticky='ns')
