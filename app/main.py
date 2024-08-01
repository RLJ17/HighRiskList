from flask import Flask, jsonify, request
from scraping import search_offshore_leaks

app= Flask(__name__)

@app.route("/")
def root():
    return "root"

@app.route("/entidad/<entity_name>")
def findEntity(entity_name):
    if not entity_name:
        return jsonify({"error": "Se requiere el nombre de la entidad"}), 400
    
    result = search_offshore_leaks(entity_name)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, port=3000)