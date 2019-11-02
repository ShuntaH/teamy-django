from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'teamy'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('signin/', auth_views.LoginView.as_view(
        template_name='teamy/signin.html'), name='signin'),
    path('signout/', auth_views.LogoutView.as_view(
        template_name='teamy/signout.html'), name='signout'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
]
