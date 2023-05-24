import factory
from django.test import TestCase, Client
from django.urls import reverse_lazy

from news import factories


class NewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.origin = factories.OriginFactory()
        self.news_item = factories.NewsFactory.create(origin=self.origin)

    def test_news_list(self):
        response = self.client.get(reverse_lazy('home'))
        self.assertEquals(response.status_code, 200)

    def test_news_detail(self):
        response = self.client.get(reverse_lazy('view_news', kwargs={'pk': self.news_item.pk}))
        self.assertEquals(response.status_code, 200)

    def test_news_create(self):
        data = {
            'title': 'News 1',
            'content': 'Some text...',
            'origin': self.origin
        }
        response = self.client.post(path=reverse_lazy('add_news'), data=data, follow=True)
        self.assertEquals(response.status_code, 200)

    def test_news_update(self):
        data = {
            'title': self.news_item.title,
            'content': self.news_item.content,
            'origin': self.news_item.origin,
            'category': self.news_item.category,
        }
        response = self.client.post(reverse_lazy('update_news', args=[self.news_item.pk]),
                                    data=data,
                                    follow=True)

        self.assertEqual(response.status_code, 200)

    def test_news_delete(self):
        response = self.client.post(path=reverse_lazy("delete_news", args=[self.news_item.pk]), follow=True)
        self.assertEqual(response.status_code, 200)
