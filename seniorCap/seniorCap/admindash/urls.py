from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
	path('', views.dash, name="admin-dash"),
	path('edit-db/', admin.site.urls),
]