from django.urls import path
from . import views

# urls -> views

urlpatterns = [
    path('', views.home, name='login-home'),
    path('register/', views.register, name="login-register"),
]
