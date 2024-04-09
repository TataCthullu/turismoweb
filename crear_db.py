import sqlite3

# Conectarse a la base de datos SQLite
conexion = sqlite3.connect('base_de_datos.db')
cursor = conexion.cursor()

# Guardar los cambios y cerrar la conexión
conexion.commit()
conexion.close()

print("Base de datos creada exitosamente.")
