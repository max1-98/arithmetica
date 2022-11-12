from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import login
from django.contrib import messages
from django.views.generic.base import TemplateView

from .forms import NewLesson, AssignStudent
from django.contrib.auth import get_user_model
from .models import Students, StudentLessons

#
# Portal 
#

def assign(response):

	User = get_user_model()
	users = User.objects.all()

	if response.method == "POST":
		if response.POST.get("save"):
			for user in User.objects.all():
				if response.POST.get("c" + str(user.id))=="clicked":
					user.is_tutor = True
				else:
					user.is_tutor = False

				user.save()

	context = {
		'users':users
	}

	return render(response, "core/assign.html", context=context)


def students(response):

	User = get_user_model()
	s = Students.objects.get(name=response.user.email)
	studentemails = s.onestudent_set.all()

	students = []
	for email in studentemails:
		student1 = User.objects.filter(email=email.studentemail)
		for student in student1:

			students.append(student)

	
	context = {
		'students':students
	}

	return render(response, "core/students.html", context=context)

def student(response, id):
	
	User = get_user_model()
	student = User.objects.get(id=id)
	students = Students.objects.get(name=student.email)
	lessons = StudentLessons.objects.get(name=student.email)

	form = NewLesson()
	form2 = AssignStudent()
	if response.method =="POST":

		form = NewLesson(response.POST)
		form2 = AssignStudent(response.POST)

		if response.POST.get("save"):
			for lesson in lessons.lesson_set.all():

				if response.POST.get("c"+str(lesson.id))=="clicked":
					lesson.homework_complete = True
				else:
					lesson.homework_complete = False
				lesson.save()

		if form2.is_valid():

			newstudent = form2.cleaned_data["student"]
			email = newstudent.email
			students.onestudent_set.create(studentemail=email)
			student1 = User.objects.filter(email=email)
			for student2 in student1:
				student2.tutor_email = student.email
				student2.save()


		if form.is_valid():

			date = form.cleaned_data["date"]
			topic1 = form.cleaned_data["topic1"]
			topic2 = form.cleaned_data["topic2"]
			topic3 = form.cleaned_data["topic3"]
			accuracy = form.cleaned_data["accuracy"]
			speed = form.cleaned_data["speed"]
			understanding = form.cleaned_data["understanding"]

			lessons.lesson_set.create(
				date=date, 
				topic1 = topic1,
				topic2 = topic2,
				topic3 = topic3,
				accuracy = accuracy,
				speed = speed,
				understanding = understanding
				)

			student.numberoflessons += 1
			response.user.numberoflessons += 1
			response.user.save()
			student.save()

			return redirect("/students/")
		else:
			form = NewLesson


	
	context = {
		'form' : form,
		'form2' : form2,
		'lessons' : lessons,
		'student' : student,
	}

	if student.is_tutor:
		return render(response, "core/tutor.html", context=context)
	else: 
		return render(response, "core/student.html", context=context)



def dashboard(response):
	return render(response, "core/dashboard.html", {})

def progress(response):

	lessons = StudentLessons.objects.get(name=response.user.email)

	scores = []
	dates = []
	for lesson in lessons.lesson_set.all():
		dates.append(str(lesson.date))
		scores.append(str((lesson.accuracy+lesson.speed+lesson.understanding)/3))

	context = {
		'dates':dates,
		'scores':scores,
	}


	return render(response, "core/progress.html", context)

def lessons(response):

	lessons = StudentLessons.objects.get(name=response.user.email)
	context = {
		'lessons':lessons

	}
	return render(response, "core/lessons.html", context=context)


#
# Templates 
#

def base(response):
	return render(response, "core/base.html", {})