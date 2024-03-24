from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from .models import User
from .forms import DriverForm
from django.views.decorators.http import require_http_methods, require_POST
from django.contrib.auth.forms import UserCreationForm


# Create your views here.


# def get_user(request, pk):
#     User.objects.get(id=pk)
#     return render(request, 'backend/get_user.html', )

@require_POST
def sign_up(request):
    # create a form instance and populate it with data from the request:
    form = UserCreationForm(request.POST)
    # check whether it's valid:
    if form.is_valid():
        # process the data in form.cleaned_data as required
        # ...

        form.save()
        # redirect to a new URL:
        return redirect('index')
    return redirect('sign_up')

