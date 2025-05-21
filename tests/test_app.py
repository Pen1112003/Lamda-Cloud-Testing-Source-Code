import json
import pytest
from app.app import app, lambda_handler

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_hello_endpoint(client):
    """Test the /api/hello endpoint"""
    response = client.get('/api/hello')
    data = json.loads(response.data)
    
    assert response.status_code == 200
    assert data['message'] == 'Hello from Lambda Cloud Testing Demo!'
    assert data['status'] == 'success'

def test_echo_endpoint(client):
    """Test the /api/echo endpoint"""
    test_data = {'key': 'value', 'test': 123}
    response = client.post('/api/echo', json=test_data)
    data = json.loads(response.data)
    
    assert response.status_code == 200
    assert data['message'] == 'Echo service'
    assert data['data'] == test_data
    assert data['status'] == 'success'

def test_health_endpoint(client):
    """Test the /api/health endpoint"""
    response = client.get('/api/health')
    data = json.loads(response.data)
    
    assert response.status_code == 200
    assert data['status'] == 'healthy'
    assert 'version' in data

def test_lambda_handler():
    """Test the Lambda handler function"""
    # Test GET request
    event = {
        'path': '/api/hello',
        'httpMethod': 'GET'
    }
    response = lambda_handler(event, {})
    
    assert response['statusCode'] == 200
    body = json.loads(response['body'])
    assert body['message'] == 'Hello from Lambda Cloud Testing Demo!'
    
    # Test POST request
    event = {
        'path': '/api/echo',
        'httpMethod': 'POST',
        'body': json.dumps({'test': 'data'})
    }
    response = lambda_handler(event, {})
    
    assert response['statusCode'] == 200
    body = json.loads(response['body'])
    assert body['data'] == {'test': 'data'} 