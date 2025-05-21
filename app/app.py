import os
import json
from flask import Flask, jsonify, request, render_template
import azure.functions as func

app = Flask(__name__)

# Sample data
PRODUCTS = [
    {
        'id': 1,
        'name': 'Smartphone X',
        'description': 'Latest smartphone with advanced features',
        'price': 999.99,
        'category_id': 1,
        'image': 'https://images.unsplash.com/photo-1598327105666-5b89351aff97?w=500&auto=format&fit=crop&q=60'
    },
    {
        'id': 2,
        'name': 'Laptop Pro',
        'description': 'High-performance laptop for professionals',
        'price': 1499.99,
        'category_id': 1,
        'image': 'https://images.unsplash.com/photo-1496181133206-80ce9b88a853?w=500&auto=format&fit=crop&q=60'
    },
    {
        'id': 3,
        'name': 'Wireless Earbuds',
        'description': 'Premium wireless earbuds with noise cancellation',
        'price': 199.99,
        'category_id': 1,
        'image': 'https://images.unsplash.com/photo-1572569511254-d8f925fe2cbb?w=500&auto=format&fit=crop&q=60'
    },
    {
        'id': 4,
        'name': 'Smart Watch',
        'description': 'Feature-rich smartwatch with health monitoring',
        'price': 299.99,
        'category_id': 1,
        'image': 'https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=500&auto=format&fit=crop&q=60'
    },
    {
        'id': 5,
        'name': 'Gaming Console',
        'description': 'Next-gen gaming console for immersive gaming',
        'price': 499.99,
        'category_id': 1,
        'image': 'https://images.unsplash.com/photo-1486401899868-0e435ed85128?w=500&auto=format&fit=crop&q=60'
    },
    {
        'id': 6,
        'name': 'Digital Camera',
        'description': 'Professional digital camera with 4K video',
        'price': 799.99,
        'category_id': 1,
        'image': 'https://images.unsplash.com/photo-1516035069371-29a1b244cc32?w=500&auto=format&fit=crop&q=60'
    }
]

CATEGORIES = [
    {
        'id': 1,
        'name': 'Electronics',
        'image': 'https://images.unsplash.com/photo-1498049794561-7780e7231661?w=500&auto=format&fit=crop&q=60'
    },
    {
        'id': 2,
        'name': 'Clothing',
        'image': 'https://images.unsplash.com/photo-1445205170230-053b83016050?w=500&auto=format&fit=crop&q=60'
    },
    {
        'id': 3,
        'name': 'Books',
        'image': 'https://images.unsplash.com/photo-1495446815901-a7297e633e8d?w=500&auto=format&fit=crop&q=60'
    },
    {
        'id': 4,
        'name': 'Home & Garden',
        'image': 'https://images.unsplash.com/photo-1484154218962-a197022b5858?w=500&auto=format&fit=crop&q=60'
    }
]

# Azure Functions handlers
def hello(req: func.HttpRequest) -> func.HttpResponse:
    return func.HttpResponse(
        json.dumps({"message": "Hello from Flask!"}),
        mimetype="application/json",
        status_code=200
    )

def echo(req: func.HttpRequest) -> func.HttpResponse:
    try:
        req_body = req.get_json()
    except ValueError:
        return func.HttpResponse(
            "Invalid request body",
            status_code=400
        )
    
    return func.HttpResponse(
        json.dumps(req_body),
        mimetype="application/json",
        status_code=200
    )

def health(req: func.HttpRequest) -> func.HttpResponse:
    return func.HttpResponse(
        json.dumps({"status": "healthy"}),
        mimetype="application/json",
        status_code=200
    )

# Flask routes for local development
@app.route('/')
def home():
    return render_template('home.html', 
                         featured_products=PRODUCTS[:4],
                         categories=CATEGORIES)

@app.route('/products')
def products():
    return render_template('products.html', 
                         products=PRODUCTS,
                         categories=CATEGORIES)

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    product = next((p for p in PRODUCTS if p['id'] == product_id), None)
    if product:
        return render_template('product_detail.html', product=product)
    return "Product not found", 404

@app.route('/category/<int:category_id>')
def category(category_id):
    category = next((c for c in CATEGORIES if c['id'] == category_id), None)
    if category:
        products = [p for p in PRODUCTS if p['category_id'] == category_id]
        return render_template('category.html', 
                             category=category,
                             products=products)
    return "Category not found", 404

@app.route('/cart')
def cart():
    return render_template('cart.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5001))
    app.run(host='0.0.0.0', port=port, debug=True) 