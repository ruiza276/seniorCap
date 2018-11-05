from django.contrib import admin
from .models import Faculty
from .models import Student
from .models import Skills
# Register your models here.

admin.site.register(Faculty)
admin.site.register(Student)
admin.site.register(Skills)
