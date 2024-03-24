from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from .models import User


# Create your views here.


# def get_user(request, pk):
#     User.objects.get(id=pk)
#     return render(request, 'backend/get_user.html', )

def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
