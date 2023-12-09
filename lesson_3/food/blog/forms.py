from django import forms
from .models import News


class NewsForm(forms.ModelForm):

    class Meta:
        model = News
        # fields = '__all__'
        exclude = ['activity_flag']


