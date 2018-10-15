from flask import Flask, render_template, request, redirect, session, flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = "AlwaysHungry"
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
	print("Got Post Info")
	print(request.form)
	if len(request.form['email']) < 1:
		flash("Email cannot be blank!")
	elif not EMAIL_REGEX.match(request.form['email']):
		flash("Invalid Email Address!")

	if len(request.form['name']) < 1:
		flash("Name cannot be blank!")
	elif len(request.form['name']) <= 3:
		flash("Name must be 3+ characters")

	if len(request.form['textarea']) < 1:
		flash("Comment cannot be blank!")
	elif len(request.form['textarea']) > 100:
		flash("Comment must be less than 100 characters")
	    	
	if '_flashes' in session.keys():
		return redirect("/")
	else:
		return redirect("/result")

	#return redirect('/')

@app.route('/result/danger')
def alert():
	print("a user tried to visit /danger.")
	return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True) 