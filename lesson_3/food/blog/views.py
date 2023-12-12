from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, View, DetailView
from .models import News, Author
from .forms import PostForm, CommentForm


class NewsListView(ListView):
    model = News
    template_name = 'blog/news-list.html'
    context_object_name = 'news'
    queryset = News.objects.filter(
        activity_flag='a'
    )


class NewsDetailView(DetailView):

    def get(self, request, *args, **kwargs):
        news_id = self.kwargs['pk']
        news = get_object_or_404(News, pk=news_id)

        comment_form = CommentForm()

        return render(request, 'blog/news_detail.html',
                      context={'news': news, 'comment_form': comment_form})


class RegisterNews(View):

    def get(self, request):
        news_form = PostForm()
        return render(request, 'blog/news_form.html',
                      context={'news_form': news_form})

    def post(self, request):
        news_form = PostForm(request.POST)
        if news_form.is_valid():
            data = news_form.cleaned_data

            new_author = Author.objects.create(
                username=data['username'],
                last_name=data['last_name'],
                first_name=data['first_name'],
                email=data['email']
            )
            new_author.save()

            new_news = News.objects.create(title=data['title'],
                                           content=data['content'],
                                           activity_flag='i',
                                           author=new_author)
            new_news.save()

        return redirect('news-list')







