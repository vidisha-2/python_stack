from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse

from .models import *

def index(request):
    
    return render(request, "restful_users/index.html", { "users" : User.objects.all()} )


def new(request):
	return render(request, "restful_users/new.html")


def create(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/restful_users/new')
    else:       
        user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'])
        user_id = User.objects.get(last_name=request.POST['last_name'])
        return redirect(f"/restful_users/show/{user_id.id}")


def show(request, id):
	return render(request, "restful_users/show.html", { "user" : User.objects.get(id = id)} )


def edit(request, id):
	return render(request, "restful_users/edit.html", { "user" : User.objects.get(id = id)} )


def update(request, id):
    errors = User.objects.basic_validator(request.POST)
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/restful_users/edit/'+id)
    else:         
        user = User.objects.get(id = id)
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()
        messages.success(request, "User successfully updated")
        return redirect('/restful_users')


def destroy(request, id):
	user = User.objects.get(id=id)
	user.delete()
	return redirect('/restful_users')