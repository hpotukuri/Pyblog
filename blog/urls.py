from django.urls import path
from . import views


urlpatterns = [
    path('', views.main_page,name='main-page'),
    path('home/', views.post, name='blog-home'),
    path('about/', views.about, name='blog-about')
]