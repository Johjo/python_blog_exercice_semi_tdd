class Controller:
    def __init__(self, model):
        self.model = model

    def get_all_articles(self):
        return self.model.get_all_articles()

    def __str__(self):
        return "Controller ( {} )".format(self.model)

    def create_article(self, title, text):
        self.model.create_article(title=title, text=text)

    def update_article(self, title, new_text):
        self.model.update_article(title=title, new_text=new_text)