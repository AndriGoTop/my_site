from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('article/<int:news_id>', article, name='article'),
    path('add_news/', add_news, name='add_news'),
    path('favorite/', favorite, name='favorite')
]


