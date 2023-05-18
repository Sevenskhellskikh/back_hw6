from django import forms
from .models import News, Category, Origin


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
