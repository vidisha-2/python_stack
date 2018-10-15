from django.shortcuts import render, HttpResponse, redirect

def index(request):
	if 'total' not in request.session:
		context = { request.session['total'] = 0 , request.session['activities'] = "" }
	return render(request, "ninja_gold/main.html", context)


def process_money(request):
	hidden_input_type = request.form['building']
	if hidden_input_type=='farm':
		gold_get = random.randint(10,20)
		session['total'] +=gold_get
		activity= "Earned  " + str(gold_get) + "golds from farm!"

	elif hidden_input_type=='cave':
		gold_get = random.randint(5,10)
		session['total'] +=gold_get
		activity= "Earned  " + str(gold_get) + "golds from farm!"

	elif hidden_input_type=='house':
		gold_get = random.randint(2,5)
		session['total'] +=gold_get
		activity= "Earned  " + str(gold_get) + "golds from farm!"

	else: #hidden_input_type=='casino':
		gold_get = random.randint(0,50)
		session['total'] +=gold_get
		activity= "Earned  " + str(gold_get) + "golds from farm!"
	
	session['activities'] = activity + "<br>"+session['activities'] 
	print(session['activities'])
	return redirect('/')