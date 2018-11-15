from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

def dash(request):
	return HttpResponse("<h1>Admin Dashboard</h1>")