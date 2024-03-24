from src.article import Article
from pytest import fixture


@fixture
def list_of_titles():
    Article.insert('test1', 'test1')
    Article.insert('test2', 'test2')
    Article.insert('test3', 'test3')
    Article.insert('test4', 'test4')
    Article.insert('test5', 'test5')
    return Article.insert('test6', 'test6')


def test_article_3(list_of_titles):
    """Тестирование поиска статьи по ID"""
    searchible_article = Article.search(3)
    assert searchible_article.title == 'test3'


def test_article_4(list_of_titles):
    """Тестирование поиска статьи по ID"""
    searchible_article = Article.search(4)
    assert searchible_article.title == 'test4'
