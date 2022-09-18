from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    # DB에 전체 데이터를 조회
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    # 사용자의 데이터를 받아서 DB에 저장
    title = request.GET.get('title')
    content = request.GET.get('content')

    # DB에 저장
    # 1
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()

    # 2 검증할 시간이 필요! save만 안하면 그전에 조작 가능!
    article = Article(title=title, content=content)
    article.save()


    # 3 편해 보이지만 나중 생각하면 2번이 남
    # Article.objects.create(title=title, content=content)

    return render(request, 'articles/create.html')