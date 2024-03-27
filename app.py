from flask import Flask, render_template, request

app = Flask(__name__)

# Ruta para la página de inicio
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para la selección de destino
@app.route('/seleccionar-destino')
def seleccionar_destino():
    # Lógica para la página de selección de destino
    return render_template('seleccionar_destino.html')

# Ruta para mostrar información sobre el destino seleccionado
@app.route('/info-destino')
def info_destino():
    destino = request.args.get('destino')
    # Lógica para mostrar información sobre el destino seleccionado
    return render_template('info_destino.html', destino=destino)

if __name__ == '__main__':
    app.run(debug=True)

