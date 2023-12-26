from django.contrib.auth.views import LoginView
from django.urls import path
from .views import main_page, login_view, logout_view, MyLogoutView, \
    register_view

urlpatterns = [
    path('', main_page, name='main'),
    # path('login', login_view, name='login'),
    path('login/', LoginView.as_view(
        template_name='my_auth/login.html',
        redirect_authenticated_user=True
    ), name='login'),
    path('logout/', MyLogoutView.as_view(), name='logout'),
    path('register', register_view, name='register')
]
