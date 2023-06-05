from django.contrib import messages
from django.contrib.auth import login, logout
from django.core.mail import send_mail
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from news import forms
from news.forms import NewsForm, UserRegisterForm, UserLoginForm, ContactForm
from news.models import News, Category, Origin


class HomeNews(ListView):
    model = News
    template_name = 'news/index.html'
    context_object_name = 'news'

    def get_queryset(self):
        if not self.request.GET:
            return News.objects.all()
        filters = Q()
        for key in ['title', 'content']:
            value = self.request.GET.get(key)
            if value:
                filters &= Q(**{f'{key}__iregex': value})
        return News.objects.filter(filters)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = forms.NewsSearch(self.request.GET or None)
        return context


class NewsByCategory(ListView):
    model = News
    template_name = 'news/index.html'
    context_object_name = 'news'
    allow_empty = False

    def get_queryset(self):
        return News.objects.filter(category=self.kwargs['category_id'])


class NewsByOrigins(ListView):
    model = News
    template_name = 'news/index.html'
    context_object_name = 'news'

    def get_queryset(self):
        return News.objects.filter(origin_id=self.kwargs['origin_id'])


class ViewNews(DetailView):
    model = News
    template_name = 'news/news_detail.html'
    # pk_url_kwarg = 'news_id'
    context_object_name = 'news_item'


class CreateNews(CreateView):
    form_class = NewsForm
    template_name = 'news/add_news.html'
    # success_url = reverse_lazy('home')


class UpdateNews(UpdateView):
    model = News
    form_class = NewsForm
    template_name = 'news/update_news.html'


class DeleteNews(DeleteView):
    model = News
    template_name = 'news/delete_news.html'
    success_url = reverse_lazy('home')


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'news/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Вы успешно зарегистрировались!')
            return redirect('home')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'news/register.html', {'form': form})


def message_send(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            mail = send_mail(
                form.cleaned_data['subject'],
                form.cleaned_data['content'],
                'mukhitov.aaa@list.ru',
                ['arsen.mukhitov@yandex.ru'],
                fail_silently=True
            )
            if mail:
                messages.success(request, 'Письмо успешно отправлено!')
                return redirect('mail')
            else:
                messages.error(request, 'Ошибка отправки')
    else:
        form = ContactForm()
    return render(request, 'news/mail.html', {'form': form})

# ===== FUNC VIEWS =====

# def index(request):
#     news = News.objects.all()
#     categories = Category.objects.all()
#     context = {'news': news, 'categories': categories, 'title': 'Список новостей'}
#     return render(request, template_name='news/index.html', context=context)


# def get_category(request, category_id):
#     news = News.objects.filter(category=category_id)
#     categories = Category.objects.all()
#     category = Category.objects.get(pk=category_id)
#     return render(request, 'news/index.html', {'news': news, 'categories': categories, 'category': category})


# def get_origin(request, origin_id):
#     news = News.objects.filter(origin_id=origin_id)
#     categories = Category.objects.all()
#     return render(request, 'news/index.html', {'news': news, 'categories': categories})


# def add_news(request):
#     if request.method == 'POST':
#         form = NewsForm(request.POST, request.FILES)
#         if form.is_valid():
#             title = form.cleaned_data['title']
#             content = form.cleaned_data['content']
#             is_published = form.cleaned_data['is_published']
#             origin = form.cleaned_data['origin']
#             photo = form.cleaned_data['photo']
#             news = News.objects.create(
#                 title=title,
#                 content=content,
#                 photo=photo,
#                 is_published=is_published,
#                 origin=origin
#             )
#             news.category.set(form.cleaned_data['category']) -- for Many-To-Many field
#             news = form.save()
#             return redirect(news)
#     else:
#         form = NewsForm()
#     return render(request, 'news/add_news.html', {'form': form})
