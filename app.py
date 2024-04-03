from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Función para inicializar la base de datos
def inicializar_base_de_datos():
    conexion = sqlite3.connect('base_de_datos.db')
    cursor = conexion.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS destinos (
                    id INTEGER PRIMARY KEY,
                    nombre TEXT,
                    descripcion TEXT
                )''')
    
    cursor.execute("SELECT COUNT(*) FROM destinos")
    cantidad_registros = cursor.fetchone()[0]

    if cantidad_registros == 0:
        destinos_ejemplo = [
            ('París', 'La ciudad del amor'),
            ('Nueva York', 'La ciudad que nunca duerme'),
            ('Tokio', 'La ciudad más grande del mundo')
        ]
        cursor.executemany("INSERT INTO destinos (nombre, descripcion) VALUES (?, ?)", destinos_ejemplo)
        conexion.commit()

    conexion.close()

# Llamar a la función para inicializar la base de datos
inicializar_base_de_datos()

# Ruta para la página de inicio
@app.route('/')
def index():
    conexion = sqlite3.connect('base_de_datos.db')
    cursor = conexion.cursor()
    cursor.execute("SELECT DISTINCT nombre FROM destinos")
    destinos = cursor.fetchall()
    conexion.close()
    return render_template('index.html', destinos=destinos)

# Ruta para seleccionar un destino
@app.route('/seleccionar-destino', methods=['GET', 'POST'])
def seleccionar_destino():
    if request.method == 'POST':
        destino_seleccionado = request.form['destino']
        return redirect(url_for('info_destino', destino=destino_seleccionado))
    else:
        conexion = sqlite3.connect('base_de_datos.db')
        cursor = conexion.cursor()
        cursor.execute("SELECT nombre FROM destinos")
        destinos = cursor.fetchall()
        conexion.close()
        return render_template('seleccionar_destino.html', destinos=destinos)

# Ruta para mostrar información sobre el destino seleccionado
@app.route('/info-destino/<destino>')
def info_destino(destino):
    conexion = sqlite3.connect('base_de_datos.db')
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM destinos WHERE nombre=?", (destino,))
    resultado = cursor.fetchone()
    conexion.close()
    return render_template('info_destino.html', destino=resultado)

if __name__ == '__main__':
    app.run(debug=True)