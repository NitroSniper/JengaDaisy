from django.shortcuts import render
import backend
from django.contrib.auth.forms import UserCreationForm


# Create your views here.


def index(request):
    return render(request, 'frontend/Home/init.html')


def signup(request):
    # if a GET (or any other method) we'll create a blank form
    form = UserCreationForm()
    return render(request, 'frontend/sign_up.html', {'form': form})
