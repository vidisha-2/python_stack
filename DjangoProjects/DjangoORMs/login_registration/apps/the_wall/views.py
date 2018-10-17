from django.shortcuts import render, HttpResponse, redirect
from apps.login_reg.models import *
from .models import *

def index(request):
	context = {
		'all_messages' : Message.objects.all().order_by('-created_at'),
		'all_comments' : Comment.objects.all()
	}
	return render(request, "the_wall/mainpage.html", context)

def post_message(request):
	name = request.session['first_name']
	user = User.objects.get(first_name=name)
	messages = Message.objects.create(message=request.POST['message'], user=User.objects.get(id=user.id))
	return redirect('/the_wall')


def post_comment(request):
	print(request.POST['recepient_id'])
	#message = Message.objects.get(id=request.POST['recepient_id'])
	name = request.session['first_name']
	user = User.objects.get(first_name=name)
	comments = Comment.objects.create(comment=request.POST['comment'], user_id=user.id, message_id=request.POST['recepient_id'])
	return redirect('/the_wall')


def delete_comment(request, id):
	message = Message.objects.get(id=id)
	message.delete()
	return redirect('/the_wall')

	

