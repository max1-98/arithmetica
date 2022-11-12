from django.contrib.auth import login, authenticate 
from django.contrib.auth.forms import UserCreationForm
from django import forms  
from django.contrib.auth import get_user_model

User = get_user_model()



class RegisterForm(UserCreationForm):

	GRADES = (("A*","A*"),("A","A"),("B","B"),("C","C"),("D","D"),("E","E"), ("U","U"))
	EXAMBOARDS = (("AQA","AQA"),("OCR A","OCR A"),("OCR Mei B","OCR Mei B"),("Edexcel","Edexcel"))

	parent_name = forms.CharField(max_length=480, label="Parent's First Name")
	email = forms.EmailField(label="Parent's Email")
	phonenumber = forms.CharField(max_length=40, label="Parent's Mobile Number")
	intialgrade =forms.ChoiceField(choices=GRADES, label="What is the Student's current predicted grade?")
	examboard = forms.ChoiceField(choices=EXAMBOARDS, label="What is the Student's examboard for A-Level maths?")
	first_name = forms.CharField(max_length=200, label="Student's First Name")
	last_name = forms.CharField(max_length=200, label="Student's Last Name")

	class Meta:
		model = User 
		fields = ["parent_name", "first_name","last_name", "email", "phonenumber", "password1","password2","intialgrade","examboard"]
