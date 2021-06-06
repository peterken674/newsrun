class Source:
    '''
    Source class to define sources.
    '''
    def __init__(self, src_id, src_name, src_category, src_url):
        self.src_id = src_id
        self.src_name = src_name
        self.src_category = src_category
        self.src_url = src_url

class Article:
    '''
    Article class to define articles.
    '''
    def __init__(self, article_src, article_author, article_title, article_description, article_content, published_at, article_url, article_image_url):
        self.article_src = article_src
        self.article_author = article_author
        self.article_title = article_title
        self.article_description = article_description
        self.article_content = article_content
        self.published_at = published_at
        self.article_url = article_url
        self.article_image_url = article_image_url