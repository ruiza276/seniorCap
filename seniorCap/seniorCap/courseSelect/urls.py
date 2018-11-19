from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_user, name="userdash-home"),
    #path('/done', views.get_info, name="userdash-home"),
]
