"""
Routes and views for the bottle application.
"""

from turtle import title
from bottle import route, view, template
from datetime import datetime
import json
import companies
import orders
import Grisha
import os

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
def parteners():
        # Открываем файл JSON и считываем его содержимое
        with open('partners.json', 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
        year=datetime.now().year
        return template('partners', year=year, data=data, error='')
    

@route('/about')
@view('about')
def about():
    """Renders the capibara info page."""
    return dict(
        title='About',
        message='Your application description page.',
        year=datetime.now().year
    )

@route('/reviews')
@view('reviews')
def reviews():
    """Renders the reviews page."""
    content = ""
    
    if os.path.isfile('C:\\Users\\Grisha\\source\\repos\\BruhBarTar\\BruhBarTar\\reviews.json'):
        with open('reviews.json', 'r', encoding='utf-8') as file:
            data = json.load(file)  
        for key in data:
            for arr in data[key]:
                content+="<div class = \"cardReview\"><h3>"+key+"</h3><p>"+arr[1]+"</p><p class=\"reviewText\">"+arr[0]+"</p></div>"
    return template('reviews', title = "Отзывы", year=datetime.now().year, error = '', cont = content)

@route('/orders')
def orders():
    with open('orders.json') as file:
        data = json.load(file)
    with open('orders_history.json') as file:
        history = json.load(file)
    return template('orders', title='Вклад капибар в культуру человека', year=datetime.now().year, data=data, history=history, select_product=None)

