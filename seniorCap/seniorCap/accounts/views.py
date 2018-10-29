from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'accounts/home.html')

def about(request):
    return HttpResponse(request, 'accounts/about.html')
