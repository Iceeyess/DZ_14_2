class Article:
    """Класс для хранения статьи"""
    article_id: int
    title: str
    content: str

    articles = dict()

    def __init__(self, title, content):
        """Конструктор для статьи"""
        self.title = title
        self.content = content
        self.article_id = self.get_new_id()

    def get_new_id(self) -> (int, None):
        """Констуктор для получения ID следующей статьи"""
        if self.articles:
            return max(self.articles) + 1
        return 1

    @classmethod
    def insert(cls, title, content):
        """Метод для добавляния словаря"""
        new_instance = cls(title, content)
        cls.articles[new_instance.article_id] = new_instance
        return new_instance

    @classmethod
    def search(cls, index):
        return cls.articles[index]




if __name__ == '__main__':
    new_article = Article.insert('test1', 'test1')
    print(new_article.article_id)
    new_article2 = Article.insert('test2', 'test2')
    print(new_article2.article_id)
    new_article3 = Article.insert('test3', 'test3')
    print(new_article3.article_id)
    print(new_article.articles) # Список всех индексов