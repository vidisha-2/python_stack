from django.shortcuts import render, HttpResponse, redirect

def index(request):
	if 'visit' not in request.session:
		request.session['visit'] = 1
	print(request.session['visit'])
	
	return render(request,"survey_form/index.html")


def process(request):
	print("Hitting post route")
	if 'visit' in request.session:
		request.session['name']= request.POST['name']
		request.session['Dojo_Location']= request.POST['Dojolocation']
		request.session['Favorite_Language']= request.POST['Favoritelanguage']
		request.session['comment']= request.POST['textarea'] 
		print("right before post redirect")
	return redirect('/results')

def results(request):
	return render(request,"survey_form/result.html")

def goback(request):
	return render(request,"survey_form/index.html")
	




# Create your views here.
