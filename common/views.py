from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from common.forms import UserForm
# Create your views here.

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(usename=username, password=raw_password)
            user = form.save()
            login(request, user)
            return redirect('main:index')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form' : form })

def page_not_found(request, exception):
    return render(request, 'common/404.html', {})