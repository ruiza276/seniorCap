from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

def dash(request):
	return render(request, "userdash/userdash-home.html")

def resume(request):
	return HttpResponse("<h1>User Resume</h1>")