from django.shortcuts import render

# Create your views here.
def greeting(requests):
    return render(requests, 'greeting.html', {'name': 'Alice'})