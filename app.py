from flask import Flask,jsonify,request
from flask_cors import CORS
import mysql.connector
import json


app = Flask(__name__)
CORS(app)

def cargar_configuracion(ruta_archivo='config.json'):
    with open(ruta_archivo, 'r') as archivo:
        configuracion = json.load(archivo)
    return configuracion

db_config = cargar_configuracion('config.json')
def obtener_conexion():
    return mysql.connector.connect(
        host=db_config['host'],
        user=db_config['user'],
        password=db_config['password'],
        database=db_config['database']
    )

# Endpoint para obtener todos los productos
@app.route('/api/productos', methods=['GET'])
def listar_productos():
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()
    cursor.close()
    conexion.close()
    return jsonify(productos),200

if __name__ == '__main__':
    print("Microservicio de productos está corriendo en http://localhost:5000")
    app.run(host='0.0.0.0', port=5000, debug=True)