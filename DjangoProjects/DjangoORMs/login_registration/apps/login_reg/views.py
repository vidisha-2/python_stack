from django.shortcuts import render, HttpResponse, redirect
from .models import *
import bcrypt

def index(request):
	return render(request, "login_reg/index.html")


def wall(request):
	return render(request, "the_wall/mainpage.html")

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
		#request.session['first_name'] = user_id.first_name
		#flash(u"You have successfully registered")
		return redirect(f"/success/{user_id.id}")


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
		return redirect(f"/success/{user.id}")
	# 	# else:
		# 	print("password doesnot match")
	return redirect('/')


	

def success(request, id):

	return render(request, "login_reg/success.html", { "user" : User.objects.get(id = id)})
