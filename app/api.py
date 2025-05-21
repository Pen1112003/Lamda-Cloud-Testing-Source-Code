from flask import Blueprint, jsonify, request

api = Blueprint('api', __name__)

@api.route('/api/hello')
def api_hello():
    return jsonify({"message": "Hello from Flask!"})

@api.route('/api/echo', methods=['POST'])
def api_echo():
    data = request.get_json()
    return jsonify(data)

@api.route('/api/health')
def api_health():
    return jsonify({"status": "healthy"}) 