from .models import Movie

from django.shortcuts import render, redirect
from django.views.decorators.http import require_safe


# Create your views here.
@require_safe
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(request, 'movies/index.html', context)


@require_safe
def detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    context = {
        'movie': movie,
    }
    return render(request, 'movies/detail.html', context)

# @require_safe
# def favorite(request):
#     if request.user.is_authenticated:
#         favorite = 


@require_safe
def recommended(request):
    if request.user.is_authenticated:
        movies = Movie.objects.filter(vote_average__gte=8.5, vote_count__gte=5000)[:10]
        context = {
            'movies': movies,
        }
        return render(request, 'movies/recommended.html', context)
    return redirect('accounts:login')