from django.shortcuts import render, HttpResponse, redirect

def index(request):
	
	return render(request, "the_wall/mainpage.html")