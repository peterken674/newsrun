from flask import render_template, request, url_for, redirect
from . import main
from ..requests import get_sources


@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    sources = get_sources()
    return render_template('index.html', sources = sources)