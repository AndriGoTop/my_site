from django.shortcuts import render, redirect
from .models import News, Pictures
from .forms import NewsForm
from django.core.paginator import Paginator


def index(request):
    news = News.objects.filter(is_published=True)
    paginator = Paginator(news, 5)
    page_num = request.GET.get('page', 1)
    page_objects = paginator.get_page(page_num)
    context = {'news': news,
               'page_obj': page_objects,
               }
    return render(request, 'news/index.html', context=context)


def article(request, news_id):
    news = News.objects.get(pk=news_id)
    pictures = news.pictures.all()
    context = {'news': news, 'pictures': pictures, }
    return render(request, 'news/article.html', context=context)


def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            news = form.save()
            return redirect('home')
    else:
        form = NewsForm()
    return render(request, 'news/create.html', {'form': form})


def favorite(request):
    news = News.objects.filter(is_favorite=True)
    paginator = Paginator(news, 20)
    page_num = request.GET.get('page', 1)
    page_objects = paginator.get_page(page_num)
    context = {'news': news,
               'page_obj': page_objects,
               }
    return render(request, 'news/favorite.html', context=context)
