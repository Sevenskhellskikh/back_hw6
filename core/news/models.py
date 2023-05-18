from django.db import models
from django.urls import reverse_lazy


class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование')
    content = models.TextField(blank=True, verbose_name='Контент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата публикации')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    category = models.ManyToManyField('Category', verbose_name='Категория')
    origin = models.ForeignKey('Origin', on_delete=models.PROTECT, verbose_name='Источник')

    def get_absolute_url(self):
        return reverse_lazy('view_news', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Наименование категории')

    def get_absolute_url(self):
        return reverse_lazy('category', kwargs={'category_id': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']


class Origin(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование источника')

    def get_absolute_url(self):
        return reverse_lazy('origin', kwargs={'origin_id': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Источник'
        verbose_name_plural = 'Источники'
        ordering = ['title']