from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'always hungry' 

@app.route('/')         
def index():
	print("hi")
	# session['visit']
	if 'visit' in session:
		session['visit'] +=1
	else:
		session['visit']=0

	return render_template("index.html", visited=session['visit'])

@app.route('/go', methods=['POST'])
def increment_the_visit():
	print("#"*50)
	print(request.form)
	# session['name'] = request.form['name']
	session['visit'] +=1
	session['decrement'] =session['visit']-1
	return redirect("/")


@app.route('/destroy_session')         
def destroy():
  session.clear()
  return redirect('/')

if __name__=="__main__":   
    app.run(debug=True)    