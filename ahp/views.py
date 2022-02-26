from django.shortcuts import render, redirect

def index(request):
    context = {
        'title' : 'Home'
    }
    return render(request, 'index.html', context)