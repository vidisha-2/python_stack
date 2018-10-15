from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/result', methods=['POST'])
def showuser():
	print("Got Post Info")
	print(request.form)
	name = request.form['name']
	dojo_location = request.form['Dojo Location']
	fav_language = request.form['Favourite Language']
	comment = request.form['textarea']
	return render_template('result.html',name=name, dojo_location=dojo_location, fav_language=fav_language, comment=comment)

@app.route('/result/danger')
def alert():
	print("a user tried to visit /danger.")
	return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True) 
