def reporteOptimizacion(tabla):
    print('------- Reporte de tabla de optimizacion ---------------')
    print(len(tabla))

    fichero = open('./app/reports/optimizacion.html','w', encoding='utf-8')
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
    
    <h1>TALBA DE OPTIMIZACION</h1>
    ''')

    # creacion de la tabla de reportes
    fichero.write('<table class="default">')

    fichero.write('</tr>')
    fichero.write('<th>Tipo</th>')#1
    fichero.write('<th>Regla</th>')#2
    fichero.write('<th>Original</th>')#3
    fichero.write('<th>Optimizada</th>')#4
    fichero.write('<th>Fila</th>')#5
    fichero.write('</tr>')


    # verificacion del contendio para la tabla de simbolos
    if len(tabla) == 0:
        fichero.write('''
        <tr>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
        </tr>''')

    else: 
        for elemento in tabla:
            fichero.write(f'''
            <tr>
            <td>{elemento[0]}</td>
            <td>{elemento[1]}</td>
            <td>{elemento[2]}</td>
            <td>{elemento[3]}</td>
            <td>{elemento[4]}</td>
            </tr> 
            ''')


    fichero.write('</table>')

    fichero.write('''
    </body>
    </html> ''')
    fichero.close()