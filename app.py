import os
import sys
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

try:
    # Add the app directory to the Python path
    sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
    
    # Import Flask app
    from app.app import app
    
    logger.info("Successfully imported app from app.app")
    
    if __name__ == '__main__':
        port = int(os.environ.get('PORT', 5000))
        logger.info(f"Starting app on port {port}")
        app.run(host='0.0.0.0', port=port, debug=True)
except Exception as e:
    logger.error(f"Error importing app: {str(e)}")
    
    # Create a simple Flask app as fallback
    from flask import Flask, jsonify
    
    app = Flask(__name__)
    
    @app.route('/')
    def home():
        return jsonify({"status": "error", "message": f"Error in app initialization: {str(e)}"})
    
    if __name__ == '__main__':
        port = int(os.environ.get('PORT', 5000))
        app.run(host='0.0.0.0', port=port, debug=True) 