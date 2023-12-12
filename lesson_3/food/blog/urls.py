from django.urls import path
from .views import NewsListView, RegisterNews, NewsDetailView

urlpatterns = [
    path('news-list/', NewsListView.as_view(), name='news-list'),
    path('new_news/', RegisterNews.as_view(), name='register-news'),
    path('news-list/<int:pk>/', NewsDetailView.as_view(), name='news-detail')
]
