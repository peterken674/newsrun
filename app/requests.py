import urllib.request, json
from .models import Article, Source

api_key = None
base_url = None
src_articles_base_url = None

def configure_src_request(app):
    global api_key, base_url, src_articles_base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_SRC_API_BASE_URL']
    src_articles_base_url = app.config['ARTICLES_FROM_SRC_BASE_URL']


def get_sources():
    '''
    Function that gets the sources json response to our url request
    '''
    get_src_url = base_url.format(api_key)

    with urllib.request.urlopen(get_src_url) as url:
        get_src_data = url.read()
        get_src_response = json.loads(get_src_data)

        sources_results = None

        if get_src_response['sources']:
            src_results_list = get_src_response['sources']
            sources_results = process_src_results(src_results_list)

    return sources_results

def process_src_results(sources_list):
    '''
    Function that takes in the response from the API and maps it into the Source objects, then populates the list with the sources.
    '''
    sources_results = []
    for source_item in sources_list:
        src_id = source_item.get('id')
        src_name = source_item.get('name')
        src_category = source_item.get('category')
        src_url = source_item.get('url')

        source_object = Source(src_id, src_name, src_category, src_url)
        sources_results.append(source_object)

    return sources_results

def get_src_articles(source):
    '''
    Function that gets all the articles from a given source.
    '''
    get_src_articles_url = src_articles_base_url.format(source, api_key)

    with urllib.request.urlopen(get_src_articles_url) as url:
        src_articles_data = url.read()
        src_articles_response = json.loads(src_articles_data)

        article_object = None
        if src_articles_response:
            article_src = src_articles_response.get('source')
            article_author = src_articles_response.get('author')
            article_title = src_articles_response.get('title')
            article_description = src_articles_response.get('description')
            article_content = src_articles_response.get('content')
            published_at = src_articles_response.get('publishedAt')
            article_url = src_articles_response.get('url')
            article_image_url = src_articles_response.get('urlToImage')

            article_object = Article(article_src, article_author, article_title, article_description, article_content, published_at, article_url, article_image_url)

    return article_object

