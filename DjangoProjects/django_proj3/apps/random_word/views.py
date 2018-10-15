from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string


def index(request):
	if 'visit' in request.session:
		request.session['visit'] += 1
	else:
		request.session['visit'] = 0
	context = { 
		"rand_number": get_random_string(length=14) }
	return render(request,"random_word/mainpage.html", context)


def generate(request):
	request.session['visit'] +=1
	context = { 
		"rand_number": get_random_string(length=14) }
	return render(request, "random_word/mainpage.html", context)
	#return render(request, "random_word/mainpage.html")


def reset(request):
	request.session['visit'] = 0
	return render(request, 'random_word/mainpage.html')	


# Create your views here.
