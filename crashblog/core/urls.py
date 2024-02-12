from django.urls import path
from .import views

urlpatterns = [
    path('', views.frontpage, name='front-page'),
    path('about/', views.aboutpage, name='about-page'),
    path('robots.txt', views.robots_txt, name='robots_txt')
]