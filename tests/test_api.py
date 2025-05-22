import pytest
import requests
from app.app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    """Test home page endpoint"""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Smartphone X' in response.data

def test_products_page(client):
    """Test products page endpoint"""
    response = client.get('/products')
    assert response.status_code == 200
    assert b'Laptop Pro' in response.data

def test_product_detail(client):
    """Test product detail endpoint"""
    response = client.get('/product/1')
    assert response.status_code == 200
    assert b'Smartphone X' in response.data

def test_category_page(client):
    """Test category page endpoint"""
    response = client.get('/category/1')
    assert response.status_code == 200
    assert b'Electronics' in response.data

def test_health_check(client):
    """Test health check endpoint"""
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json == {"status": "healthy"}

def test_api_hello(client):
    """Test API hello endpoint"""
    response = client.get('/api/hello')
    assert response.status_code == 200
    assert response.json == {"message": "Hello from Flask!"}

def test_api_echo(client):
    """Test API echo endpoint"""
    test_data = {"message": "test"}
    response = client.post('/api/echo', json=test_data)
    assert response.status_code == 200
    assert response.json == test_data 