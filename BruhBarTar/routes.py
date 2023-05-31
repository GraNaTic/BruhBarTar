"""
Routes and views for the bottle application.
"""

from turtle import title
from bottle import route, view, template
from datetime import datetime
import json

@route('/')
@route('/home')
@view('index')
def home():
    """Renders the home page."""
    return dict(
        year=datetime.now().year
    )

@route('/contribution')
@view('contact')
def contact():
    """Renders the contact page."""
    return dict(
        title='Вклад капибар в культуру человека',
        message='Капибара принимает ванну:',
        year=datetime.now().year
    )

@route('/partners')
@view('partners')
def contact():
        # Открываем файл JSON и считываем его содержимое
        with open('partners.json') as json_file:
            data = json.load(json_file)
        title='Партнерские компании',
        year=datetime.now().year
        return template('partners', title=title, year=year, data=data)
    

@route('/about')
@view('about')
def about():
    """Renders the capibara info page."""
    return dict(
        title='About',
        message='Your application description page.',
        year=datetime.now().year
    )

@route('/companies', method = 'post')
def companies():
    return dict(
        title='About',
        year=datetime.now().year
    )

@route('/orders')
def orders():
    with open('orders.json') as file:
        data = json.load(file)
    return template('orders', orders=orders, title='Вклад капибар в культуру человека', year=datetime.now().year, data=data)

