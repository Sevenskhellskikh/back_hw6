from django.urls import path, include


from .views import *

urlpatterns = [
    path('', HomeNews.as_view(), name='home'),
    path('category/<int:category_id>', NewsByCategory.as_view(), name='category'),
    path('origin/<int:origin_id>', NewsByOrigins.as_view(), name='origin')
]