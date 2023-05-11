from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from news.models import News, Category, Origin


class HomeNews(ListView):
    model = News
    template_name = 'news/index.html'
    context_object_name = 'news'

    def get_queryset(self):
        return News.objects.filter(is_published=True)


class NewsByCategory(ListView):
    model = News
    template_name = 'news/category.html'
    context_object_name = 'news'
    allow_empty = False

    def get_queryset(self):
        return News.objects.filter(category=self.kwargs['category_id'])


class NewsByOrigins(ListView):
    model = News
    template_name = 'news/category.html'
    context_object_name = 'news'

    def get_queryset(self):
        return News.objects.filter(origin_id=self.kwargs['origin_id'])

# def index(request):
#     news = News.objects.all()
#     categories = Category.objects.all()
#     context = {'news': news, 'categories': categories, 'title': 'Список новостей'}
#     return render(request, template_name='news/index.html', context=context)


# def get_category(request, category_id):
#     news = News.objects.filter(category=category_id)
#     categories = Category.objects.all()
#     category = Category.objects.get(pk=category_id)
#     return render(request, 'news/category.html', {'news': news, 'categories': categories, 'category': category})


# def get_origin(request, origin_id):
#     news = News.objects.filter(origin_id=origin_id)
#     categories = Category.objects.all()
#     return render(request, 'news/category.html', {'news': news, 'categories': categories})
