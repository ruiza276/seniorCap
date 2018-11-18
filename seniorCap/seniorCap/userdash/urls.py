from django.urls import path
from . import views

urlpatterns = [
	path('', views.dash, name="userdash-home"),
	path('resume/', views.resume, name="resume"),
]
