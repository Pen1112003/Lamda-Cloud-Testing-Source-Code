import os
import sys

# Add the app directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from app.app import app

if __name__ == '__main__':
    app.run() 