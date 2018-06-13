from django.shortcuts import render
from django.http import HttpResponse
from . import models

def index(request):

    aritcles = models.Article.objects.all()
    return render(request, 'blog/index.html',{'aritcles': aritcles})

def add(request):
    return render(request, 'blog/article.html')

def add_action(request):
    title = request.POST['title']
    content = request.POST['content']
    article_id = request.POST['article_id']
    if article_id == '0':
        #新增
        models.Article.objects.create(title=title, name=content)
        aritcles = models.Article.objects.all()
        return render(request, 'blog/index.html', {'aritcles': aritcles})
    #编辑
    article = models.Article.objects.get(pk=article_id)
    article.title = title
    article.name = content
    article.save()
    return render(request, 'blog/article_detail.html', {'aritcle': article})

def article(request, article_id):
    aritcle = models.Article.objects.get(pk=article_id)
    return render(request, 'blog/article_detail.html',{'aritcle': aritcle})

def edit(request, article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'blog/article.html', {'article':article})