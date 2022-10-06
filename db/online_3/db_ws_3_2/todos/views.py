from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from .models import Todo
from .forms import TodoForm


# Create your views here.
def index(request):
    todos = Todo.objects.all()
    context = {
        'todos': todos,
    }
    return render(request, 'todos/index.html', context)


@require_http_methods(['GET', 'POST'])
def create(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = TodoForm(request.POST)
            if form.is_valid():
                todo = form.save(commit=False)
                todo.author = request.user
                todo.save()
                return redirect('todos:index')
        else:
            form = TodoForm()
        context = {
            'form': form,
        }
        return render(request, 'todos/create.html', context)
    return render(request, 'accounts/login.html', context)