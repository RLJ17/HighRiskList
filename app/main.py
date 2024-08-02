from flask import Flask, jsonify, request, make_response
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from scraping import search_offshore_leaks
from flask_cors import CORS
from datetime import timedelta, datetime

app = Flask(__name__)
CORS(app, supports_credentials=True, resources={r"/*": {"origins": "http://localhost:3000"}})

# Configuración de JWT
app.config['JWT_SECRET_KEY'] = 'super-secret-key'
jwt = JWTManager(app)

# Configuración de Rate Limiting
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["20 per minute"]
)

@app.route("/")
def root():
    return "root"

@app.route("/login", methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    
    #Credenciales de prueba
    if username != 'admin' or password != 'password':
        return jsonify({"msg": "Bad username or password"}), 401

    # Crear un nuevo token JWT
    access_token = create_access_token(identity=username)

    response = make_response(jsonify({"msg": "Login successful", "riskToken": access_token}))
    response.set_cookie('riskToken', access_token, httponly=False, samesite='none', secure=True, expires=datetime.utcnow() + timedelta(minutes=180))
    return response

@app.route("/entidad/<entity_name>")
@limiter.limit("20 per minute")
def findEntity(entity_name):
    if not entity_name:
        return jsonify({"error": "Se requiere el nombre de la entidad"}), 400

    result = search_offshore_leaks(entity_name)
    return jsonify(result)

@app.after_request
def apply_cors(response):
    response.headers["Access-Control-Allow-Origin"] = "http://localhost:3000"
    response.headers["Access-Control-Allow-Credentials"] = "true"
    response.headers["Access-Control-Allow-Methods"] = "GET,POST,PUT,DELETE,OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type,Authorization"
    return response

# Manejo de errores de Rate Limiting
@app.errorhandler(429)
def ratelimit_handler(e):
    return jsonify(error="ratelimit exceeded"), 429

if __name__ == '__main__':
    app.run(debug=True, port=3000)