import unittest
import json
from app.app import app, hello, echo, health

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_products_page(self):
        response = self.app.get('/products')
        self.assertEqual(response.status_code, 200)

    def test_product_detail(self):
        response = self.app.get('/product/1')
        self.assertEqual(response.status_code, 200)

    def test_category_page(self):
        response = self.app.get('/category/1')
        self.assertEqual(response.status_code, 200)

    def test_cart_page(self):
        response = self.app.get('/cart')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main() 