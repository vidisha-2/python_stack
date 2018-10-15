from flask import Flask, render_template, request, redirect, session
import random
import datetime

app = Flask(__name__)
app.secret_key = 'always and forever hungry'

@app.route('/')         
def index():
	
	if 'total' not in session:
		session['total']=0
		session['activities']=""
	return render_template("index.html", total=session['total'])

@app.route('/reset')
def reset():
	session.clear()
	return redirect('/')

@app.route('/process_money', methods=['POST'])         
def process_money():
    
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



if __name__=="__main__":   
    app.run(debug=True)    