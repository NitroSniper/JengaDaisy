from django.shortcuts import render


# Create your views here.


def index(request):
    return render(request, 'frontend/Home/init.html')


def signup(request):
    return render(request, 'frontend/signup.html')
