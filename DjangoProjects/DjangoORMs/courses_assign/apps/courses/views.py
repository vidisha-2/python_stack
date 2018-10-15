from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse
from .models import *


def index(request):
	courses = Course.objects.all()
	descriptions = Description.objects.all()
	context = {
		"courses": courses,
		"descriptions": descriptions
	}
	for course in courses:
		print(course)
		if hasattr(course, 'description'):
			print(course.description)

	for desc in descriptions:
		print(desc)
		print("super descriptive description", desc.course)
	return render(request, "courses/mainpage.html", context)


def create(request):
	c1 = Course.objects.create(name=request.POST['course_name'])
	d1 = Description.objects.create(desc=request.POST['textarea'], course=c1)
	return redirect('/')


def show(request):
	return render(request, "/courses/destroy.html")


def destroy(request, id):
	desc = Description.objects.get(id=id)
	desc.delete()
	return redirect('/')





