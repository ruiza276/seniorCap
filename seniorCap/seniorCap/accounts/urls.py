from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='acounts-home'),
    path('about/', views.about, name='acounts-about'),
]
