from django.shortcuts import render


def index(request):
    return render(request, 'index.html', context={
        'who': 'World',
        'about': '/about/',
        'categories': '/simple_blog/categories',
        'articles': '/simple_blog/articles',
    })