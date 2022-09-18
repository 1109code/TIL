import re
from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    # DB에 전체 데이터를 조회
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def new(request):
    form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/new.html', context)


def create(request):
    form = ArticleForm(request.POST) # 저장한게 아니라 값만 가져온거
    if form.is_valid(): # 유효하니?
        article = form.save() # 응 유효해
        return redirect('articles:detail', article.pk)
    print(f'에러요! {form.errors}')
    return redirect('articles:new')


def detail(request, pk):
    # variable routing으로 받은 pk 값으로 데이터를 조회
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)


def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')


def edit(request, pk):
    article = Article.objects.get(pk=pk)
    form = ArticleForm(instance=article)
    context = {
        'article' : article,
        'form' : form,
    }
    return render(request, 'articles/edit.html', context)


def update(request, pk):
    article = Article.objects.get(pk=pk)
    form = ArticleForm(request.POST, instance=article)
    
    if form.is_valid():
        form.save()
        return redirect('articles:detail', article.pk)
    
    context = {
        'article' : article,
        'form' : form, 
    }
    
    return render(request, 'articles/edit.html', context) 