from flask import Flask, render_template, redirect, url_for
import sqlite3

app = Flask(__name__)

# Definir los datos de los viajes en un diccionario
viajes = {
    "Paiconen": {
        "fecha_inicio": "15/04/2024",
        "fecha_fin": "20/04/2024",
        "min_participantes": 5,
        "max_participantes": 10
    },
    "OtroDestino": {
        "fecha_inicio": "01/05/2024",
        "fecha_fin": "10/05/2024",
        "min_participantes": 3,
        "max_participantes": 8
    }
}

# Ruta para la página de inicio del viaje
@app.route('/')
def index():
    # Inicializar la base de datos
    inicializar_base_de_datos()
    # Obtener destinos desde la base de datos
    conexion = sqlite3.connect('base_de_datos.db')
    cursor = conexion.cursor()
    cursor.execute("SELECT DISTINCT nombre FROM destinos")
    destinos = cursor.fetchall()
    conexion.close()
    return render_template('index.html', viajes=viajes, destinos=destinos)

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

# Rutas para otras páginas
@app.route('/info_contacto')
def informacion_contacto():
    return render_template('info_contacto.html')

@app.route('/info_empresa')
def informacion_empresa():
    return render_template('info_empresa.html')

# Ruta para mostrar información sobre el destino seleccionado
@app.route('/info-destino/<destino>')
def info_destino(destino):
    conexion = sqlite3.connect('base_de_datos.db')
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM destinos WHERE nombre=?", (destino,))
    resultado = cursor.fetchone()
    conexion.close()
    return render_template('info_destino.html', destino=resultado)

@app.route('/seleccionar_destinos')
def seleccionar_destinos():
    conexion = sqlite3.connect('base_de_datos.db')
    cursor = conexion.cursor()
    cursor.execute("SELECT DISTINCT nombre FROM destinos")
    destinos = cursor.fetchall()
    conexion.close()
    return render_template('seleccionar_destinos.html', destinos=destinos, viajes=viajes)


if __name__ == '__main__':
    app.run(debug=True)
