from django.contrib.auth.views import LogoutView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy


def main_page(request, *args, **kwargs):
    return render(request, 'my_auth/base.html')


def login_view(request, *args, **kwargs):
    if request.method == 'GET':
        return render(request, 'my_auth/login.html')

    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('main')

    return render(request, 'my_auth/login.html', {'error': 'auth error'})


class MyLogoutView(LogoutView):
    next_page = reverse_lazy('main')


def logout_view(request):
    logout(request)
    return redirect('main')
