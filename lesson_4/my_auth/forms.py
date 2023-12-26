from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Profile


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email',
                  'last_name', 'first_name',
                  'password1', 'password2'
                  )


class ProfileForm(forms.ModelForm):

    birthday = forms.DateField(widget=forms.DateInput)

    class Meta:
        model = Profile
        fields = ('birthday', 'tel')
