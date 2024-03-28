from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render, reverse
from django.views import generic
from django.views.decorators.http import require_http_methods, require_POST

from .models import Driver

# Create your views here.


# def get_user(request, pk):
#     User.objects.get(id=pk)
#     return render(request, 'backend/get_user.html', )


@require_POST
def login(request):
    form = auth.forms.AuthenticationForm(request, data=request.POST)
    if form.is_valid():
        user = form.get_user()
        auth.login(request, user)
        return redirect('index')
    return redirect('login')


@require_POST
def signup(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        user = form.save()
        driver = Driver.objects.create(user=user)
        driver.save()
        auth.login(request, user)

        # redirect to a new URL:
        return redirect("index")
    return render(request, reverse('/signup'), {"form": form})


@require_POST
def logout(request):
    auth.logout(request)
    return redirect("index")
