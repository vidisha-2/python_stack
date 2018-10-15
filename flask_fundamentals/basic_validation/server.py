from flask import Flask, render_template, redirect, request, session, flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/process', methods=['Post'])
def process():
    if len(request.form['first_name'])<=1:
        flash("Name cannot be empty")
    else:
        flash(f"Success! Your name is {request.form['first_name']}.")
    if len(request.form['last_name'])<=1:
        flash("Name cannot be empty")
    else:
        flash(f"Success! Your name is {request.form['last_name']}.")
    if len(request.form['email']) < 1:
        flash("Email cannot be blank")
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
    else:
        flash("Success!")
    if len(request.form[''])
    return redirect('/')
if __name__=="__main__":
    app.run(debug=True)
