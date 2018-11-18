from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from login.models import Major
# Create your views here.

def dash(request):
	context = {'names': Major.objects.all()}
	return render(request, "userdash/userdash-home.html", context)


def resume(request):
	#obj = Major.objects.get(id=2)
	context = {'names': Major.objects.all()}
	return render(request, 'userdash/resume.html', context)
