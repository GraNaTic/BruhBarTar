from bottle import route, template, post, request
from datetime import datetime
import json

@route('/add_product', method='post')
def add_product():
    with open('orders.json') as file:
        data = json.load(file)
    select_product = request.forms.get('product_name')
    return template('orders', title='Вклад капибар в культуру человека', year=datetime.now().year, data=data, select_product=select_product)

