from django.shortcuts import render, redirect 
from .forms import RegisterForm

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm

from django.contrib.auth import get_user_model
User = get_user_model()

from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes

from core.models import StudentLessons, Students

def register(response):
	form = RegisterForm()

	if response.method == "POST":
		form = RegisterForm(response.POST)

		if form.is_valid():

			form.save()
			# Create lessons 
			email = form.cleaned_data["email"]
			lessons = StudentLessons(name=email)
			lessons.save()
			students = Students(name=email)
			students.save()

			return redirect("/login/")
		else:
			form = RegisterForm

	return render(response, "register/register.html", {"form":form})

def password_reset_request(request):

	if request.method == "POST":

		password_reset_form = PasswordResetForm(request.POST)

		if password_reset_form.is_valid():

			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))

			if associated_users.exists():

				for user in associated_users:

					subject = "Password Reset Requested"
					email_template_name = "password/password_reset_email.txt"
					c = {
					"email":user.email,
					'domain':'127.0.0.1:8000',
					'site_name': 'Website',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, 'admin@example.com' , [user.email], fail_silently=False)
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
					return redirect ("/password_reset/done/")

	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="password/password_reset.html", context={"password_reset_form":password_reset_form})
