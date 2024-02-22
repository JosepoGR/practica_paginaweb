from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def mostrar_estudiantes():
    # Conectar a la base de datos
    conn = sqlite3.connect('estudiantes.db')
    cursor = conn.cursor()

    # Nombre de la tabla que quieres conectar
    nombre_tabla = 'estudiantes'

    # Consultar datos de la tabla
    cursor.execute(f"SELECT * FROM {nombre_tabla}")
    filas = cursor.fetchall()

    # Cerrar la conexión
    conn.close()

    # Renderizar la plantilla HTML con los datos obtenidos
    return render_template('index.html', filas=filas)

if __name__ == '__main__':
    app.run(debug=True)