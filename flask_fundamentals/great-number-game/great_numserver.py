from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'always and forever hungry'

@app.route('/') 
def index():

	if 'key' not in session:
		session['key'] = random.randrange(0,101)
	return render_template("index.html")

@app.route('/go', methods=['POST']) 
def check():
	print(request.form)
	if (int(request.form['name'])<session['key']):
		result="too low"
		color = 'orange'
	elif(int(request.form['name'])>session['key']):
		result="too high"
		color = 'orange'
	else:
		result="That's right!"
		color = 'green'
	
	return render_template("index.html",value=result)
	#return redirect('/')


if __name__=="__main__":   
    app.run(debug=True)    