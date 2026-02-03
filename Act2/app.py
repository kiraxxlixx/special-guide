from flask import Flask, render_template

app = Flask(__name__)

# Ruta de la Landing Page (viene de la Actividad 1)
@app.route('/')
def home():
    return render_template('map.html')

# --- NUEVA RUTA PARA LA ACTIVIDAD 2 ---
# Esta ruta se encargará de mostrar el mapa de Leaflet
@app.route('/mapa')
def mapa():
    return render_template('map.html')

if __name__ == '__main__':
    app.run(debug=True)