import sqlite3

# Conectar a la base de datos (asegúrate de tener el archivo SQLite presente)
conn = sqlite3.connect('estudiantes.db')

# Crear un cursor para ejecutar comandos SQL
cursor = conn.cursor()

# Nombre de la tabla que quieres conectar
nombre_tabla = 'estudiantes'

# Consultar datos de la tabla
cursor.execute(f"SELECT * FROM {nombre_tabla}")
filas = cursor.fetchall()

# Imprimir resultados
print(f"Contenido de la tabla {nombre_tabla}:")
for fila in filas:
    print(f"ID: {fila[0]}, nombre1: {fila[1]}, nombre2: {fila[2]}, apellido1: {fila[3]}, apellido2: {fila[4]} telefono: {fila[5]}")

# Cerrar la conexión
conn.close()