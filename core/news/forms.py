from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import News, Category, Origin


class ContactForm(forms.Form):
    subject = forms.CharField(label='Тема письма', widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(label='Текст', widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label="Имя пользователя", widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class NewsSearch(forms.Form):
    title = forms.CharField(label='Ищите по заголовку', required=False,
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(label='А можете по контентной части', required=False,
                              widget=forms.TextInput(attrs={'class': 'form-control'}))


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'photo', 'category', 'origin', 'is_published']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'category': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'origin': forms.Select(attrs={'class': 'form-control'})
        }

    # title = forms.CharField(max_length=150, label="Название", widget=forms.TextInput(attrs={'class': 'form-control'}))
    # content = forms.CharField(label="Текст", required=False, widget=forms.Textarea(attrs={
    #     'class': 'form-control',
    #     'rows': 5,
    # }))
    # is_published = forms.BooleanField(label="Опубликовано", initial=True)
    # category = forms.ModelMultipleChoiceField(queryset=Category.objects.all(), label="Категория", widget=forms.SelectMultiple({'class': 'form-control'}))
    # origin = forms.ModelChoiceField(Origin.objects.all(), empty_label='Выберите источник...', widget=forms.Select(attrs={'class': 'form-control'}))
