from django.urls import path
from django.views.generic import TemplateView

from . import views 

urlpatterns = [

	path("", TemplateView.as_view(template_name="core/home.html")),
	path("pricing/", TemplateView.as_view(template_name="core/price.html")),


	# Function Based Views
	path("dashboard/", views.dashboard, name="dashboard"),
	path("progress/", views.progress, name="progress"),
	path("lessons/", views.lessons, name="lessons"),
	path("students/", views.students, name="students"),
	path("assign/", views.assign, name="assign"),

	# Dynamic Pages
	path("<int:id>/", views.student, name="student"),
]

