from django.shortcuts import render
from .models import News, Pictures


def index(request):
    news = News.objects.all()
    context = {'news': news, }
    return render(request, 'news/index.html', context=context)


def article(request, news_id):
    news = News.objects.get(pk=news_id)
    pictures = news.pictures.all()
    context = {'news': news, 'pictures': pictures, }
    return render(request, 'news/article.html', context=context)
