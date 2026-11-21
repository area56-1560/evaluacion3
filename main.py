from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/notas', methods=['GET', 'POST'])
def notas():
    promedio = None
    estado = None

    if request.method == 'POST':
        nota1 = float(request.form['nota1'])
        nota2 = float(request.form['nota2'])
        nota3 = float(request.form['nota3'])
        asistencia = float(request.form['asistencia'])

        promedio = round((nota1 + nota2 + nota3) / 3, 1)

        if promedio >= 40 and asistencia >= 75:
            estado = 'APROBADO'
        else:
            estado = 'REPROBADO'

    return render_template('notas.html', promedio=promedio, estado=estado)

@app.route('/nombres', methods=['GET', 'POST'])
def nombres():
    nombre_mayor = None
    cantidad_letras = None

    if request.method == 'POST':
        nombre1 = request.form['nombre1'].strip()
        nombre2 = request.form['nombre2'].strip()
        nombre3 = request.form['nombre3'].strip()

        nombres = [nombre1, nombre2, nombre3]
        nombre_mayor = max(nombres, key=len)
        cantidad_letras = len(nombre_mayor)

    return render_template('nombres.html', nombre_mayor=nombre_mayor, cantidad_letras=cantidad_letras)

if __name__ == '__main__':
    app.run(debug=True)
