from flask import render_template, request, url_for, redirect
from . import main
from ..requests import get_sources, get_src_articles, search_articles


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
    categories = [general, entertainment, business, sports, health, technology, science]

    search_articles = request.args.get('query')
    title = 'Home | Newsrun'

    if search_articles:
        return redirect(url_for('main.search', term = search_articles))
    else:
        return render_template('index.html', categories = categories, title = title)

@main.route('/articles/<source_id>')
def source(source_id):
    '''
    View articles page function that returns articles from the specified sources.
    '''
    articles = get_src_articles(source_id)
    title = articles[0].article_src['name'] + ' | Newsrun'

    return render_template('articles.html', articles = articles, title = title)

@main.route('/search/<term>')
def search(term):
    '''
    View function to display the search results
    '''
    terms = term.split(' ')
    query = '+'.join(terms)
    articles_found = search_articles(query)
    title = 'Search Results | Newsrun'
    
    return render_template('search.html', articles = articles_found, title = title)