import unittest
import json
from azure.functions import HttpRequest
from app.app import hello, echo, health

class TestAzureFunctions(unittest.TestCase):
    def test_hello_function(self):
        # Create a mock HTTP request
        req = HttpRequest(
            method='GET',
            url='/api/hello',
            body=None
        )
        
        # Call the function
        response = hello(req)
        
        # Check the response
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_body())
        self.assertEqual(data['message'], 'Hello from Azure Functions!')

    def test_echo_function(self):
        test_data = {'message': 'test message'}
        
        # Create a mock HTTP request
        req = HttpRequest(
            method='POST',
            url='/api/echo',
            body=json.dumps(test_data).encode('utf-8')
        )
        
        # Call the function
        response = echo(req)
        
        # Check the response
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_body())
        self.assertEqual(data, test_data)

    def test_health_function(self):
        # Create a mock HTTP request
        req = HttpRequest(
            method='GET',
            url='/api/health',
            body=None
        )
        
        # Call the function
        response = health(req)
        
        # Check the response
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_body())
        self.assertEqual(data['status'], 'healthy')

if __name__ == '__main__':
    unittest.main() 