from flask import Flask, render_template, request, jsonify
import time  # Importamos time para simular que la base de datos "piensa"

app = Flask(__name__)

# --- Rutas de Vistas (HTML) ---

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/mapa')
def mapa():
    return render_template('map.html')

# --- NUEVA RUTA (API) PARA LA ACTIVIDAD 3 ---
# Esta ruta no devuelve HTML, sino que recibe datos y devuelve JSON.
@app.route('/guardar_punto', methods=['POST'])
def guardar_punto():
    # 1. Recibir los datos que manda Javascript
    data = request.get_json()
    lat = data.get('lat')
    lng = data.get('lng')
    
    print(f"📍 Recibido punto: {lat}, {lng}") # Esto saldrá en tu terminal negra
    
    # 2. Simular un retraso (1 segundo) para que puedas ver el spinner de "Cargando..."
    # Esto es clave para la UX que pide la guía.
    time.sleep(1)
    
    # 3. Responder que todo salió bien
    return jsonify({
        "status": "success", 
        "message": "Punto guardado en el servidor"
    })

if __name__ == '__main__':
    app.run(debug=True)