from django.urls import path, include


from .views import *

urlpatterns = [
    path('', HomeNews.as_view(), name='home'),
    path('category/<int:category_id>', NewsByCategory.as_view(), name='category'),
    path('origin/<int:origin_id>', NewsByOrigins.as_view(), name='origin'),
    path('news/<int:pk>', ViewNews.as_view(), name='view_news'),
    path('news/add-news', CreateNews.as_view(), name='add_news'),
    path('news/update-news/<int:pk>', UpdateNews.as_view(), name='update_news'),
    path('news/delete-news/<int:pk>', DeleteNews.as_view(), name='delete_news'),
]