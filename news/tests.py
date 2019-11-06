from django.test import TestCase

from .models import Editor,Article,tags
import datetime as dt

class EditorTestClass(TestCase):

    #set up method
    def setUp(self):
        self.titus=Editor(first_name = 'Titus', last_name ='Opiyo',email='titusouko@gmail.com')

#Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.titus, Editor))

    #Testing the sve method
    def test_save_method(self):
        self.titus.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)

class ArticleTestClass(TestCase):
    def setUp(self):
        # Creating a new editor and saving it
        self.titus=Editor(first_name = 'Titus', last_name ='Opiyo',email='titusouko@gmail.com')
        self.titus.save_editor()

        #Creating a new tag and saving it
        self.new_tag = tags(name = 'testing')
        self.new_tag.save_tag()

        self.new_article= Article(title = 'Testing Article', post = 'This is a random test Post', editor = self.titus)
        self.new_article.save()

        self.new_article.tags.add(self.new_tag)

    def tearDown(self):
        Editor.objects.all().delete()
        tags.objects.all().delete()
        Article.objects.all().delete()

    def test_get_news_today(self):
        todays_news = Article.todays_news()
        self.assertTrue(len(todays_news)>0)

    def test_get_news_by_date(self):
        testdate = '2017-03-17'
        date = dt.datetime.strptime(testdate, '%Y-%m-%d').date()
        news_by_date = Article.days_news(date)
        self.assertTrue(len(news_by_date) == 0)
