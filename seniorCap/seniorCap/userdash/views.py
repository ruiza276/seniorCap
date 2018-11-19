from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from login.models import Job
from login.models import UserProfile
from login.models import Major
from django.contrib.auth.models import User
import operator

# Create your views here.

def dash(request):
	print("BEFORE TRY")
	#try:
	print("After TRY")
	user1 = request.user
	print("FUCK YOU SYED")
	profile = UserProfile.objects.filter(user=user1).first()
	print(user1)
	print("FUCK YOU SYED2")
	#testing = profile.user.username
	print("FUCK YOU SYED3")
	skills = profile.skills
	print("FUCK YOU SYED4")

	uskills = []

	try:
		if skills.skill1.skill_name != None:
			uskills.append(skills.skill1.skill_name)
			print("APPENDED: "+skills.skill1.skill_name)
		if skills.skill2.skill_name != None:
			uskills.append(skills.skill2.skill_name)
			print("APPENDED: "+skills.skill2.skill_name)
		if skills.skill3.skill_name != None:
			uskills.append(skills.skill3.skill_name)
			print("APPENDED: "+skills.skill3.skill_name)
		if skills.skill4.skill_name != None:
			uskills.append(skills.skill4.skill_name)
			print("APPENDED: "+skills.skill4.skill_name)
		if skills.skill5.skill_name != None:
			uskills.append(skills.skill5.skill_name)
			print("APPENDED: "+skills.skill5.skill_name)
		if skills.skill6.skill_name != None:
			uskills.append(skills.skill6.skill_name)
			print("APPENDED: "+skills.skill6.skill_name)
		if skills.skill7.skill_name != None:
			uskills.append(skills.skill7.skill_name)
			print("APPENDED: "+skills.skill7.skill_name)
		if skills.skill8.skill_name != None:
			uskills.append(skills.skill8.skill_name)
			print("APPENDED: "+skills.skill8.skill_name)
		if skills.skill9.skill_name != None:
			uskills.append(skills.skill9.skill_name)
			print("APPENDED: "+skills.skill9.skill_name)
	except:
		print ("you did it bitch you broke it")

	all_jobs = Job.objects.all()
	major_jobs = all_jobs.filter(job_major=profile.major)

	result1 =[]

	for skill in uskills:
		save= []
		print ("SKILL ="+ skill)
		if skill == None:
			continue
		for job in major_jobs:
			if job.job_skill1.skill_name == skill:
				save.append(job)
				continue
			try:
				if job.job_skill2.skill_name == skill:
					save.append(job)
					continue
				elif job.job_skill3.skill_name == skill:
					save.append(job)
					continue
				elif job.job_skill4.skill_name == skill:
					save.append(job)
					continue
				elif job.job_skill5.skill_name == skill:
					save.append(job)
					continue
			except:
				print()
		result1.append(save)

	result2 = {}
	for result in result1:
		for job in result:
			if job not in result2:
				result2.update({job:1})
			else:
				int = result2.get(job)
				result2.update({job:int+1})

	FUCK = sorted(result2.values(),reverse=True)
	result3= []
	for i in range(0,len(result2)):
		result3.append(max(result2.items(), key=operator.itemgetter(1))[0])
		del result2[max(result2.items(), key=operator.itemgetter(1))[0]]

	print(result2)
	print(result3)

	context = {"len":len(result3), "results":result3, "Jobs":True}

	return render(request, "userdash/userdash-home.html", context)
#except:
#	context = {"len":0, "results":[], "Jobs":False}

#	return render(request, "userdash/userdash-home.html", context)


def resume(request):
	#obj = Major.objects.get(id=2)
	context = {'names': Major.objects.all()}
	return render(request, 'userdash/resume.html', context)
