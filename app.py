from flask import Flask, request, jsonify  # Importar las bibliotecas necesarias
import mysql.connector  # Importar el conector de MySQL

app = Flask(__name__)  # Crear una instancia de la aplicación Flask

# Configurar la conexión a la base de datos MySQL
db = mysql.connector.connect(
    host="localhost",  # Dirección del host donde se encuentra la base de datos
    user="root",       # Nombre de usuario para acceder a la base de datos
    password="aderly",   # Contraseña para el usuario de la base de datos
    database="mysql"  # Nombre de la base de datos a la que se va a conectar
)
cursor = db.cursor()  # Crear un cursor para interactuar con la base de datos

# Definir una ruta para obtener datos desde la base de datos
@app.route('/data', methods=['GET'])
def get_data():
    cursor.execute("SELECT * FROM test_table")  # Ejecutar una consulta SQL
    result = cursor.fetchall()  # Obtener todos los resultados de la consulta
    return jsonify(result)  # Devolver los resultados en formato JSON

if __name__ == '_main_':
    app.run(debug=True, port=5001)