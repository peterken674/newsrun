from flask import render_template, request, url_for, redirect
from . import main
from ..requests import get_sources


@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    sports = []
    business = []
    entertainment = []
    general = []
    health = []
    science = []
    technology = []
    sources = get_sources()
    for source in sources:
        if source.src_category == 'sports':
            sports.append(source)
        elif source.src_category == 'business':
            business.append(source)
        elif source.src_category == 'entertainment':
            entertainment.append(source)
        elif source.src_category == 'general':
            general.append(source)
        elif source.src_category == 'health':
            health.append(source)
        elif source.src_category == 'science':
            science.append(source)
        elif source.src_category == 'technology':
            technology.append(source)
    categories = [general, entertainment, business, entertainment, business, sports, health, technology, science]

    return render_template('index.html', categories = categories)