from django.urls import path
from .import views


urlpatterns = [
    path('', views.search, name='search'),
    path('about/', views.about, name='about'),
    path('career/', views.career, name='career'),
]