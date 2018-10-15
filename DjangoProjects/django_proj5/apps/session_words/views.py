from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
def index(request):
#	if 'visit' not in request.session:
#		request.session = 1
	print("hey")
	print(request.session)
	return render(request, "session_words/mainpage.html")


def add(request):
	
		print("Im in add phase")
		if 'enter_here' not in request.session:
			request.session['enter_here'] = []
			print(request.session['enter_here'])
		temp_list=request.session['enter_here']
		x = strftime("%Y-%m-%d %H:%M %p", gmtime())
		temp_list.append({ "enter_here": request.POST['enter_here'],
							"color": request.POST['color'],
							"show_big": request.POST['big_font'],
							"time": x })
		request.session['enter_here'] = temp_list
		return redirect('/')

def clear(request):
	request.session = 0
	return render(request, "session_words/mainpage.html")



