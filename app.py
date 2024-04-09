from flask import Flask, render_template, redirect, url_for
import sqlite3

app = Flask(__name__)

# Ruta para la página de inicio del viaje
@app.route('/')
def index():
    # Obtener destinos desde la base de datos
    destinos = seleccionar_destinos()
    return render_template('index.html', destinos=destinos)

# Función para inicializar la base de datos
def inicializar_base_de_datos():
    conexion = sqlite3.connect('base_de_datos.db')
    cursor = conexion.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS destinos (
                    id INTEGER PRIMARY KEY,
                    nombre TEXT,
                    descripcion TEXT,
                    imagen TEXT  -- Nueva columna para almacenar el nombre del archivo de imagen
                )''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS viajes (
                    id INTEGER PRIMARY KEY,
                    destino_id INTEGER,
                    fecha_inicio TEXT,
                    fecha_fin TEXT,
                    min_participantes INTEGER,
                    max_participantes INTEGER,
                    FOREIGN KEY(destino_id) REFERENCES destinos(id)
                )''')
    
    # Agregar la columna destino_id si no existe
    cursor.execute('''PRAGMA table_info(viajes)''')
    columns = cursor.fetchall()
    column_names = [column[1] for column in columns]
    if 'destino_id' not in column_names:
        cursor.execute('''ALTER TABLE viajes ADD COLUMN destino_id INTEGER''')
    
    
    conexion.close()

@app.route('/seleccionar_destinos')
def seleccionar_destinos():
    conexion = sqlite3.connect('base_de_datos.db')
    cursor = conexion.cursor()
     # Consulta para obtener los destinos
    cursor.execute("SELECT nombre, imagen FROM destinos")

    destinos = cursor.fetchall()
    conexion.close()
    return render_template('seleccionar_destinos.html', destinos=destinos)


# Función para obtener los viajes disponibles desde la base de datos
def obtener_viajes_disponibles():
    conexion = sqlite3.connect('base_de_datos.db')
    cursor = conexion.cursor()
    cursor.execute("SELECT nombre, fecha_inicio, fecha_fin, min_participantes, max_participantes FROM viajes")
    viajes = cursor.fetchall()
    conexion.close()
    return viajes

@app.route('/viajes_disponibles')
def viajes_disponibles():
    # Obtener los viajes disponibles desde la base de datos
    viajes = obtener_viajes_disponibles()
    return render_template('viajes_disponibles.html', viajes=viajes)


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

if __name__ == '__main__':
    inicializar_base_de_datos()
    app.run(debug=True)
