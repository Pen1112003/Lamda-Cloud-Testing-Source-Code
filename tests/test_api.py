import unittest
import json
from app.app import app, hello, echo, health

class TestAzureFunctions(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_hello_endpoint(self):
        # Test through Flask
        response = self.app.get('/api/hello')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['message'], 'Hello from Flask!')

        # Test through Azure Function
        req = type('HttpRequest', (), {'get_json': lambda: None})()
        response = hello(req)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_body())
        self.assertEqual(data['message'], 'Hello from Azure Functions!')

    def test_echo_endpoint(self):
        test_data = {'message': 'test message'}
        
        # Test through Flask
        response = self.app.post('/api/echo', json=test_data)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data, test_data)

        # Test through Azure Function
        req = type('HttpRequest', (), {'get_json': lambda *args, **kwargs: test_data})()
        response = echo(req)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_body())
        self.assertEqual(data, test_data)

    def test_health_endpoint(self):
        # Test through Flask
        response = self.app.get('/api/health')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['status'], 'healthy')

        # Test through Azure Function
        req = type('HttpRequest', (), {'get_json': lambda: None})()
        response = health(req)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_body())
        self.assertEqual(data['status'], 'healthy')

if __name__ == '__main__':
    unittest.main() 