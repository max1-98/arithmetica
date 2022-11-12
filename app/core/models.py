from django.db import models

class Sample(models.Model):
	attachment = models.FileField()
	
from django.conf import settings




class StudentLessons(models.Model):

	name = models.EmailField()
	# Next time add unique = True
	student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name="studentlessons", null=True)


	def __str__(self):
		return self.name 

class Lesson(models.Model):

	studentlessons = models.ForeignKey(StudentLessons, on_delete = models.CASCADE)
	date = models.DateField()

	topic1 = models.CharField(max_length=40)
	topic2 = models.CharField(max_length=40)
	topic3 = models.CharField(max_length=40)

	speed = models.IntegerField()
	accuracy = models.IntegerField()
	understanding = models.IntegerField()

	homework_complete = models.BooleanField(default=False)

	def __str__(self):
		return self.date

class Students(models.Model):

	# Next time add unique = True 

	name = models.EmailField()
	tutor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name="students", null=True)

	def __str__(str):
		return self.name


class OneStudent(models.Model):

	studentemail = models.EmailField()
	students = models.ForeignKey(Students, on_delete = models.CASCADE)