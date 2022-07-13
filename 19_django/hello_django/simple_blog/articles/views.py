from django.shortcuts import render
from django.http import HttpResponse # <- добавил строчку

# Create your views here.

def index(request):
    return render(request, 'articles.html', context={
        'who': 'World',
    })
