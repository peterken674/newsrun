from flask import render_template, request, url_for, redirect
from . import main


@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    return render_template('index.html')