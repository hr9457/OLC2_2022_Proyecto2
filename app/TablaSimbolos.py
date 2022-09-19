def generarTablaSimbolos(tablaSimbolos):
    print('------- Reporte de tabla de simbolos ---------------')
    print(len(tablaSimbolos))

    fichero = open('./app/reports/tabla.html','w', encoding='utf-8')
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
    
    <h1>TALBA DE SIMBOLOS</h1>
    ''')

    # creacion de la tabla de reportes
    fichero.write('<table class="default">')

    fichero.write('</tr>')
    fichero.write('<th>Identificador</th>')#1
    fichero.write('<th>Tipo Simbolo</th>')#2
    fichero.write('<th>Tipo dato</th>')#3
    fichero.write('<th>Ambito</th>')#4
    fichero.write('<th>Fila</th>')#5
    fichero.write('<th>Columna</th>')#6
    fichero.write('</tr>')


    # verificacion del contendio para la tabla de simbolos
    if len(tablaSimbolos) == 0:
        fichero.write('''
        <tr>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
        </tr>''')

    else: 
        for elemento in tablaSimbolos:
            fichero.write(f'''
            <tr>
            <td>{elemento[0]}</td>
            <td>{elemento[1]}</td>
            <td>{elemento[2]}</td>
            <td>{elemento[3]}</td>
            <td>{elemento[4]}</td>
            <td>{elemento[5]}</td>
            </tr> 
            ''')


    fichero.write('</table>')

    fichero.write('''
    </body>
    </html> ''')
    fichero.close()