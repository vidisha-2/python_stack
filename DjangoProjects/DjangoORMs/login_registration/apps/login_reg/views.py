from django.shortcuts import render, HttpResponse, redirect
from .models import *
import bcrypt

def index(request):
	return render(request, "login_reg/index.html")


def register(request):
	print('im in register')
	request.session['action'] = 'register'
	errors = User.objects.register_basic_validator(request.POST)
	if len(errors) > 0:
		for key, value in errors.items():
			messages.error(request, value)
		return redirect('/')
	else:
		pw_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
		user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=pw_hash)
		user_id = User.objects.get(email=request.POST['email'])
		print("*"*100,user_id)
		request.session['first_name'] = user_id.first_name
		request.session['user_id']=user_id.id
		#flash(u"You have successfully registered")
		return redirect(f"/the_wall/mainpage/{user_id.id}")


def login(request):
	request.session['action'] = 'login'
	errors = User.objects.login_basic_validator(request.POST)
	print(errors)
	if len(errors) > 0:
		for key, value in errors.items():
			messages.error(request, value)
		return redirect('/')
	else:
		user = User.objects.get(email=request.POST['login_email'])
		request.session['first_name'] = user.first_name
		request.session['user_id']=user.id
		return redirect(f"/the_wall/mainpage/{user.id}")
	# 	# else:
		# 	print("password doesnot match")
	return redirect('/')


def wall(request, id):
	return render(request, "the_wall/mainpage.html", { "user" : User.objects.get(id = id)})


def success(request, id):
	return render(request, "/success.html", { "user" : User.objects.get(id = id)})
