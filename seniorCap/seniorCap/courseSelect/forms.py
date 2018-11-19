from django import forms
from django.forms.widgets import CheckboxSelectMultiple
from .models import UserProfile, Class

# class UserForm(forms.Form):
#     name = forms.CharField(label='Enter Your Name:', max_length=100)
#     major = forms.CharField(label='Enter Your Major:', max_length=100)
#     course = forms.CharField(label='Enter a Course:', max_length=100)

class UserForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['major', 'courses']

    def __init__ (self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields["courses"].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields["courses"].queryset = Class.objects.all()




# class CourseForm(forms.ModelForm):
#     class Meta:
#         model = Class
#         fields = ['class_name', 'major', 'class_skill1', 'class_skill2', 'class_skill3']
#
# form = CourseForm()
