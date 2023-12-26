from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthday = models.DateField(verbose_name='birthdate')
    tel = models.CharField(max_length=16)
    news_num = models.IntegerField(default=0, verbose_name='кол-во публикаций')

    def __str__(self):
        return f'{self.user.email}'

