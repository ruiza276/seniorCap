from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm

# urls redirects to views

# HOME is /login
def home(request):
    return render(request, 'login/main_login.html')

# REGISTER is /login/register
def register(request):
	if request.method == "POST":
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get("username") #cleaned_data is a dictionary
			messages.success(request, f"Account created for {username}! Try logging in...")
			# redirect('login-home', {"messages":messages})

	else:
		form = UserRegisterForm()
	return render(request, 'login/student_create_account.html', {"form":form})
