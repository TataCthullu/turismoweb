from flask import Flask, render_template, redirect, url_for
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
    
    conexion.close()

# Llamar a la función para inicializar la base de datos
inicializar_base_de_datos()


# Ruta para la página de inicio
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/info_contacto')
def informacion_contacto():
    return render_template('info_contacto.html')

@app.route('/info_empresa')
def informacion_empresa():
    return render_template('info_empresa.html')

@app.route('/seleccionar_destinos')
def seleccionar_destinos():
    conexion = sqlite3.connect('base_de_datos.db')
    cursor = conexion.cursor()
    cursor.execute("SELECT DISTINCT nombre FROM destinos")
    destinos = cursor.fetchall()
    conexion.close()
    return render_template('seleccionar_destinos.html', destinos=destinos)

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
