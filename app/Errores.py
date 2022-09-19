from datetime import date
from datetime import datetime
from traceback import format_exception

def generarTablaErrores(tablaErrores):
    
    #Día actual
    today = date.today()

    #Fecha actual
    now = datetime.now()


    fichero = open('./app/reports/tablaErrores.html','w', encoding='utf-8')
    fichero.write(f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
        <link rel="stylesheet" href="style.css">
    </head>
    <body>            
    
    <h1>TALBA DE ERRORES</h1>
    ''')

    # creacion de la tabla de reportes
    fichero.write('<table class="default">')

    fichero.write('</tr>')
    fichero.write('<th>No.</th>')#1
    fichero.write('<th>Descripcion</th>')#2
    fichero.write('<th>Ambiot</th>')#3
    fichero.write('<th>Fila</th>')#4
    fichero.write('<th>Columna</th>')#5
    fichero.write('<th>Fecha</th>')#6
    fichero.write('</tr>')


    # verificacion del contendio para la tabla de simbolos
    if len(tablaErrores) == 0:
        fichero.write(f'''
        <tr>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>{format(today.day)}/{format(today.month)}/{format(today.year)} - {format(now.hour)}:{format(now.minute)}</td>
        </tr>''')

    else: 
        contador = 0
        for elemento in tablaErrores:
            fichero.write(f'''
            <tr>
            <td>{contador}</td>
            <td>{elemento[0]}</td>
            <td>{elemento[1]}</td>
            <td>{elemento[2]}</td>
            <td>{elemento[3]}</td>
            <td>{format(today.day)}/{format(today.month)}/{format(today.year)} - {format(now.hour)}:{format(now.minute)}</td>
            </tr> 
            ''')
            contador += 1


    fichero.write('</table>')

    fichero.write('''
    </body>
    </html> ''')
    fichero.close()