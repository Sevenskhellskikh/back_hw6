from django.urls import path, include


from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('category/<int:category_id>', get_category, name='category'),
    path('origin/<int:origin_id>', get_origin, name='origin')
]