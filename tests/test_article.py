import unittest
from app.models import Article

class ArticleTest(unittest.TestCase):
    '''
    Test the article class.
    '''
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Article({'id':'bbc-uk', 'name' : 'BBC News'}, 'John Doe', 'The Life of The Real Pie', 'Lorem ipsum dolo sit amet', 'Lorem impsum dolo sit amet...', '2021-05-12T20:17:46.384Z', 'https://www.bbc.com/hahaha', 'https://www.bbc.com/hahaha.jpg')  

    def test_init(self):
        self.assertTrue(isinstance(self.new_article, Article))    