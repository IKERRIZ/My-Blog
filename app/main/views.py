from flask import render_template
from . import main
from ..request import get_quote

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = "Welcome | Blog Post website"
    quote = get_quote

    return render_template('index.html', title = title quote=quote)