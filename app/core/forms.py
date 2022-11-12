from django import forms
from django.conf import settings
from .models import Lesson, Students
from django.contrib.auth import get_user_model



class NewLesson(forms.Form):

	date = forms.DateField(
		label = "When was this lesson?",
		widget = forms.DateInput(attrs={'type':'date'})
		)

	#This will be changed into a choice field, need to look for a search widget to save time
	topic1 = forms.CharField(max_length=40, label="What was the main topic covered?")
	topic2 = forms.CharField(max_length=40, label="Additional Topic 1", required=False)
	topic3 = forms.CharField(max_length=40, label="Additional Topic 2", required=False)
	
	ONETOTEN =  (("1",1),("2",2),("3",3),("4",4),("5",5),("6",6),("7",7),("8",8),("9",9),("10",10))
	speed = forms.ChoiceField(choices= ONETOTEN, label="How fast was the student in completing tasks?")
	accuracy = forms.ChoiceField(choices= ONETOTEN, label="Was the student very accurate?")
	understanding = forms.ChoiceField(choices= ONETOTEN, label="What was the general understanding of the topics covered?")

	class Meta:
		model = Lesson


class AssignStudent(forms.Form):

	User = get_user_model()
	users = User.objects.all()
	student = forms.ModelChoiceField(queryset = users, empty_label="Select User", label="Add Student")

