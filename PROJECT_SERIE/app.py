from flask import Flask, render_template, request, redirect, url_for, flash
from api import init_api
from models import init_db

app = Flask(__name__)
app.secret_key = 'your_secret_key' # Cambia esto por una clave secreta real

# Inicializa la API
init_api(app)

# Inicializa la base de datos al inicio
with app.app_context():
    init_db()

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)