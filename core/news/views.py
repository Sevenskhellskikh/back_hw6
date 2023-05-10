from django.http import HttpResponse
from django.shortcuts import render

from news.models import News, Category, Origin


def index(request):
    news = News.objects.all()
    categories = Category.objects.all()
    context = {'news': news, 'categories': categories, 'title': 'Список новостей'}
    return render(request, template_name='news/index.html', context=context)


def get_category(request, category_id):
    news = News.objects.filter(category=category_id)
    categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    return render(request, 'news/category.html', {'news': news, 'categories': categories, 'category': category})


def get_origin(request, origin_id):
    news = News.objects.filter(origin_id=origin_id)
    categories = Category.objects.all()
    return render(request, 'news/category.html', {'news': news, 'categories': categories})