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

def achivements(request):
    context = {
        'nbar': 'achivement'
    }
    return render(request, 'achivement_details.html', context)

def blog(request):
    context = {
        'nbar': 'blog'
    }
    return render(request, 'blog.html', context)

def blogDetails(request):
    context = {
        'nbar': 'blogDetails'
    }
    return render(request, 'blogDetails.html', context)

def clubHistory(request):
    context = {
        'nbar': 'clubHistory'
    }
    return render(request, 'clubHistory.html', context)

def gallery(request):
    context={
        'nbar': 'gallery'
    }
    return render(request, 'gallery02.html', context)

def playerDetails(request):
    context={
        'nbar': 'playerDetails'
    }
    return render(request, 'playerDetails.html', context)

def user_login(request):
    context={
        'nbar': 'login'
    }
    return render(request, 'login.html', context)

def user_register(request):
    context={
        'nbar': 'register'
    }
    return render(request, 'register.html', context)



