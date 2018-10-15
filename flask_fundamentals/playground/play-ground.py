from flask import Flask, render_template  # Import Flask to allow us to create our app, and import
                                          # render_template to allow us to render index.html.
app = Flask(__name__)                     # Global variable __name__ tells Flask whether or not we
@app.route('/')
def home():
	pass

@app.route('/play')
def squirrel():
    	return render_template("index.html", times=3, bg_color=("blue"))  
@app.route('/play/<number>')
def darwin(number):
        return render_template("index.html", times=int(number), bg_color=("blue"))
                            
@app.route('/play/<number>/<color>')                           
def einstein(number,color):
    return render_template("index.html", times=int(number), bg_color=(color))  # Render the template and return it!
if __name__=="__main__":
    app.run(debug=True)                   # Run the app in debug mode.
