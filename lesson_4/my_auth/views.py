from django.contrib.auth.views import LogoutView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from .forms import UserForm, ProfileForm
from .models import Profile
from django.contrib import messages

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


def register_view(request, *args, **kwargs):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            birthday = profile_form.cleaned_data['birthday']
            tel = profile_form.cleaned_data['tel']
            Profile.objects.create(
                user=user,
                birthday=birthday,
                tel=tel
            )
            username = user_form.cleaned_data['username']
            raw_password = user_form.cleaned_data['password1']
            auth_user = authenticate(username=username, password=raw_password)
            login(request, auth_user)
            return redirect('main')
        else:
            print(profile_form.errors)
            messages.add_message(request, messages.ERROR, 'Invalid fields')

    user_form = UserForm()
    profile_form = ProfileForm()
    return render(request, 'my_auth/register.html', context={
        'user_form': user_form,
        'profile_form': profile_form
    })
