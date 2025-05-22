import pytest
import requests
import os

# Use environment variable for base URL, default to GCP app URL
BASE_URL = os.getenv('APP_URL', 'https://lamda-cloud-tes.uc.r.appspot.com')

def test_home_page():
    """Test home page endpoint"""
    response = requests.get(f'{BASE_URL}/')
    assert response.status_code == 200
    assert 'Smartphone X' in response.text

def test_products_page():
    """Test products page endpoint"""
    response = requests.get(f'{BASE_URL}/products')
    assert response.status_code == 200
    assert 'Laptop Pro' in response.text

def test_product_detail():
    """Test product detail endpoint"""
    response = requests.get(f'{BASE_URL}/product/1')
    assert response.status_code == 200
    assert 'Smartphone X' in response.text

def test_category_page():
    """Test category page endpoint"""
    response = requests.get(f'{BASE_URL}/category/1')
    assert response.status_code == 200
    assert 'Electronics' in response.text

def test_health_check():
    """Test health check endpoint"""
    response = requests.get(f'{BASE_URL}/health')
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_api_hello():
    """Test API hello endpoint"""
    response = requests.get(f'{BASE_URL}/api/hello')
    assert response.status_code == 200
    assert response.json() == {"message": "Hello from Flask!"}

def test_api_echo():
    """Test API echo endpoint"""
    test_data = {"message": "test"}
    response = requests.post(f'{BASE_URL}/api/echo', json=test_data)
    assert response.status_code == 200
    assert response.json() == test_data 