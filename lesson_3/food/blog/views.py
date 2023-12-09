from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, View
from .models import News, Author
from .forms import NewsForm


class NewsListView(ListView):
    model = News
    template_name = 'blog/news-list.html'
    context_object_name = 'news'
    queryset = News.objects.filter(
        activity_flag='a'
    )


class RegisterNews(View):

    def get(self, request):
        news_form = NewsForm()
        return render(request, 'blog/news_form.html',
                      context={'news_form': news_form})

    def post(self, request):
        news_form = NewsForm(request.POST)
        if news_form.is_valid():
            data = news_form.cleaned_data
            new_news = News.objects.create(title=data['title'],
                                           content=data['content'],
                                           activity_flag='i')
            new_news.save()
        return redirect('news-list')







