from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('experience/', views.experience, name='experience'),
    path('projects/', views.projects, name='projects'),
    path('education/', views.education, name='education'),
    path('contact/', views.contact, name='contact'),
    path('show/', views.show_data, name='show'),
    path('edit/<int:id>/', views.edit_data, name='edit'),
    path('delete/<int:id>/', views.delete_data, name='delete'),
]