from django.urls import path
from . import views
from django.contrib.auth import views as dj_views

urlpatterns = [
    path('', views.index, name='menu'),
    path('login/', dj_views.LoginView.as_view(extra_context={'pagename': 'Авторизация'}), name='login'),
    path('logout/', dj_views.LogoutView.as_view(), name='logout'),
    path('registration/', views.registration_page, name='regist'),
]