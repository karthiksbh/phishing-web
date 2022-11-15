from django.urls import path
from . import views
urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('login/', views.loginview, name='login'),
    path('login/creds/', views.getParam, name='getparam'),
    path('google/', views.googlePage, name='google')
]
