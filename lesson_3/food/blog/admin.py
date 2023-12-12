from django.contrib import admin
from .models import News, Author


class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'published_at',
                    'activity_flag']
    list_filter = ['activity_flag']

    actions = ['mark_as_active', 'mark_as_inactive']

    def mark_as_active(self, request, queryset):
        queryset.update(activity_flag='a')

    def mark_as_inactive(self, request, queryset):
        queryset.update(activity_flag='i')

    mark_as_active.short_description = 'Перевести в статус активный'
    mark_as_inactive.short_description = 'Перевести в статус неактивный'


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['username', 'email']


admin.site.register(News, NewsAdmin)
admin.site.register(Author, AuthorAdmin)


