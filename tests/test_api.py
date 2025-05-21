import unittest
import json
from app.app import app, lambda_handler

class TestLambdaAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_hello_endpoint(self):
        # Test through Flask
        response = self.app.get('/api/hello')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['message'], 'Hello from Flask!')

        # Test through Lambda
        event = {
            'path': '/api/hello',
            'httpMethod': 'GET'
        }
        response = lambda_handler(event, {})
        self.assertEqual(response['statusCode'], 200)
        data = json.loads(response['body'])
        self.assertEqual(data['message'], 'Hello from Flask!')

    def test_echo_endpoint(self):
        test_data = {'message': 'test message'}
        
        # Test through Flask
        response = self.app.post('/api/echo', json=test_data)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data, test_data)

        # Test through Lambda
        event = {
            'path': '/api/echo',
            'httpMethod': 'POST',
            'body': json.dumps(test_data)
        }
        response = lambda_handler(event, {})
        self.assertEqual(response['statusCode'], 200)
        data = json.loads(response['body'])
        self.assertEqual(data, test_data)

    def test_health_endpoint(self):
        # Test through Flask
        response = self.app.get('/api/health')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['status'], 'healthy')

        # Test through Lambda
        event = {
            'path': '/api/health',
            'httpMethod': 'GET'
        }
        response = lambda_handler(event, {})
        self.assertEqual(response['statusCode'], 200)
        data = json.loads(response['body'])
        self.assertEqual(data['status'], 'healthy')

if __name__ == '__main__':
    unittest.main() 