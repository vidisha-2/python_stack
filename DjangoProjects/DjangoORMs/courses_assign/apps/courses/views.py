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
	errors = Course.objects.basic_validator(request.POST)
	if len(errors)>0:
		for key, value in errors.items():
			messages.error(request, value)
		return redirect('/')
	else:       
		c1 = Course.objects.create(name=request.POST['course_name'])
		d1 = Description.objects.create(desc=request.POST['textarea'], course=c1)
		return redirect('/')


def show(request, id):
	c1=Course.objects.get(id=id)
	print(c1.id)
	d1=Description.objects.get(course_id=id)
	print(d1.course_id)
	if c1.id==d1.course_id:
		print(d1.desc)
	context = { "d" : d1 }
	print("$"*80, context)
	print(d1.course.name)
	return render(request, "courses/destroy.html", context)


def delete(request, id):
	desc = Course.objects.get(id=id)
	desc.delete()
	return redirect('/')





