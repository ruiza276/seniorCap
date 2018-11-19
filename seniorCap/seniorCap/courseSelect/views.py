from django.shortcuts import render,redirect
from courseSelect.models import *
from django.utils import timezone


from .forms import UserForm

# Create your views here.
# def select(request):
#     return render(request, 'courseselect/select.html')

def get_user(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.user= request.user

            #user.save()
            #form.save_m2m()

            return redirect('/userdash/')
            #return render(request, 'userdash/userdash-home.html', {'form':form})

    else:
        form = UserForm()
    return render(request, 'courseSelect/select.html', {'form':form})

def get_info(request):
    return render(request, 'courseSelect/selected.html')
# def get_user(request):
#     if request.method == 'POST':
#         form = UserForm(request.POST)
#         if form.is_valid():
#             #form.save()
#             #TODO: handle form
#             name = form.cleaned_data["name"]
#             major = form.cleaned_data["major"]
#             course = form.cleaned_data["course"]
#             context = {
#                 "name" : name,
#                 "major" : major,
#                 "course" : course
#             }
#
#             return render(request, 'courseselect/selected.html', context)
#
#     else:
#         form = UserForm()
#     context = {
#
#     'form' : form
#
#     }
#
#     return render(request, 'courseselect/select.html', {"form" : form})
