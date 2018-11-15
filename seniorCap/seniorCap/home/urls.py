from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name="emploid-home"),
	path('about/', views.about, name="emploid-about"),
]