"""
Routes and views for the bottle application.
"""

from turtle import title
from bottle import route, view
from datetime import datetime

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

@route('/about')
@view('about')
def about():
    """Renders the capibara info page."""
    return dict(
        title='About',
        message='Your application description page.',
        year=datetime.now().year
    )


