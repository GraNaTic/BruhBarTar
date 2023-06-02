from bottle import route, template
from datetime import datetime

@route('/orders')
def orders():
    return template('orders', orders=orders, title='Вклад капибар в культуру человека', year=datetime.now().year)
