from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):

    list_display = ['username', 'tel']

    def username(self, obj):
        return obj.user.username


admin.site.register(Profile, ProfileAdmin)
