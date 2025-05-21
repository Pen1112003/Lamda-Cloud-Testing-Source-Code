from flask import jsonify, request
from app.app import app

@app.route('/api/hello')
def api_hello():
    return jsonify({"message": "Hello from Flask!"})

@app.route('/api/echo', methods=['POST'])
def api_echo():
    data = request.get_json()
    return jsonify(data)

@app.route('/api/health')
def api_health():
    return jsonify({"status": "healthy"}) 