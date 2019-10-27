from flask import render_template
from app import app

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'Welcome to my Blog post website'
    return render_template('index.html', title = title)