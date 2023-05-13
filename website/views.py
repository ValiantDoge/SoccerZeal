from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'nbar': 'home'
    }
    return render(request, 'index.html', context)


def about(request):
    context = {
        'nbar': 'about'
    }
    return render(request, 'about.html', context)

def contact(request):
    context = {
        'nbar': 'contact'
    }
    return render(request, 'contact.html', context)