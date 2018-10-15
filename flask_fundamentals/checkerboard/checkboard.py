from flask import Flask, render_template  
app = Flask(__name__)                    
@app.route('/')    
def home():
	return render_template("index.html", x=8, y=8)                    
@app.route('/<num1>/<num2>')                           
def display(num1,num2):
    return render_template("index.html", x=int(num1), y=int(num2))  # Render the template and return it!
if __name__=="__main__":
    app.run(debug=True)                   # Run the app in debug mode.
