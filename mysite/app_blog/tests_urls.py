from django.test import TestCase
from django.urls import reverse, resolve

from .views import (HomePageView, ArticleDetail,
ArticleList, ArticleCategoryList)

class HomeTests(TestCase):
    def test_home_view_status_code(self): 
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        
    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func.view_class,HomePageView)
        
    def test_category_view_status_code(self):
        url = reverse('articles-category-list', args=('name',))
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        
    def test_articles_view_status_code(self):
        url = reverse('articles-list')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        
    def test_article_detail_view_status_code(self):
        url = reverse('article-detail', kwargs={'year':2022, 'month':10,'day':13,'slug':'testing'})
        self.assertEquals(resolve(url).func.view_class,ArticleDetail)