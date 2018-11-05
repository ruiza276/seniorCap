from django.db import models
from django.contrib.auth.models import User

# Extension of the User Object
class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	def __str__(self):
		return self.user.username

class Faculty(models.Model):
	faculty_id = models.IntegerField()
	faculty_name_first = models.CharField(max_length=50)
	faculty_name_last = models.CharField(max_length=50)
	faculty_email = models.CharField(max_length=50)
	def __str__(self):
		return self.faculty_name_last

class Student(models.Model):
	student_id = models.IntegerField()
	student_name_first = models.CharField(max_length=50)
	student_name_last = models.CharField(max_length=50)
	student_email = models.CharField(max_length=50)

	def __str__(self):
		return self.student_name_last

class Skills(models.Model):
    tech_Stack = models.CharField(max_length=50)
    gen_skills = models.CharField(max_length=50)
    major = models.CharField(max_length=50)
    tech_Stack = models.CharField(max_length=50)
