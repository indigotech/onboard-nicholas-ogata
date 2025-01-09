from fastapi import FastAPI

app = FastAPI()

PRODUCTS = [
    {'name': 'Laptop', 'price': 1000, 'category': 'Electronics'},
    {'name': 'Chair', 'price': 100, 'category': 'Furniture'},
    {'name': 'Book', 'price': 20, 'category': 'Education'},
]

@app.get('/')
async def welcome():
    return {'message': 'Welcome to our product catalog'}

@app.get('/products')
async def get_all_products():
    return PRODUCTS