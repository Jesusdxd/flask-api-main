from flask import Flask, jsonify
from config import Config
from models import db
from routes import init_routes
from flask_swagger_ui import get_swaggerui_blueprint
from swagger import swagger_template

app = Flask(__name__)

# Cargar configuración de base de datos y otros parametros
app.config.from_object(Config)

# Inicializar la base de datos con la app
db.init_app(app)

# Crear las tablas si no existen
with app.app_context():
    db.create_all()

# Registrar las rutas de la aplicación
init_routes(app)


#Configuracion de Swagger UI
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json' # Archivo que contiene la documentación de la API

swagger_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={ 'app_name': "API 101" },
)
app.register_blueprint(swagger_blueprint, url_prefix=SWAGGER_URL)

@app.route('/')
def home():
    return {'message': 'Bienvenido a la API 101'}

@app.route('/static/swagger.json')
def swagger_json():
    return jsonify(swagger_template)


if __name__ == '__main__':
    app.run(debug=True)