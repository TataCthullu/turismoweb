import sqlite3

# Conectarse a la base de datos SQLite
conexion = sqlite3.connect('base_de_datos.db')
cursor = conexion.cursor()

# Crear la tabla destinos si no existe
cursor.execute('''CREATE TABLE IF NOT EXISTS destinos (
                    id INTEGER PRIMARY KEY,
                    nombre TEXT,
                    descripcion TEXT
                )''')

# Insertar algunos datos de ejemplo en la tabla destinos
destinos_ejemplo = [
    ('París', 'La ciudad del amor'),
    ('Nueva York', 'La ciudad que nunca duerme'),
    ('Tokio', 'La ciudad más grande del mundo')
]

cursor.executemany("INSERT INTO destinos (nombre, descripcion) VALUES (?, ?)", destinos_ejemplo)

# Guardar los cambios y cerrar la conexión
conexion.commit()
conexion.close()

print("Base de datos creada exitosamente.")
