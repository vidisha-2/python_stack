from flask import Flask, render_template, request, redirect, flash, session
from mysqlconnection import connectToMySQL
from flask_bcrypt import Bcrypt
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = "AlwaysHungry!"
bcrypt = Bcrypt(app)
@app.route('/')
def index():
      
    return render_template('index.html')


@app.route('/register', methods=['POST'])
def register():
    mysql = connectToMySQL("login_register_db")
    query = "SELECT email from users WHERE email=%(email)s;"
    data={ 'email': request.form['email'] }
    emailcheck=mysql.query_db(query,data)
    if len(request.form['first_name']) < 1 and len(request.form['last_name']) < 1:
        flash(u"Name must be 3+ characters long",'first_name')
    if request.form['first_name'].isalpha()==False and request.form['last_name'].isalpha()==False:
        flash(u"Name must not contain any numbers",'first_name')
    if len(request.form['email']) < 1 and not EMAIL_REGEX.match(request.form['email']):
        flash(u"Please fill this field!",'email')
    if len(emailcheck)>0:
        flash(u"Email is already taken!",'email')
    if len(request.form['password'])<8 or re.search('[0-9]', request.form['password']) is None or re.search('[A-Z]', request.form['password']) is None:
        flash(u"Password must be atleast 8 characters long, should contain one digit and one alphanumeric",'password')
    if request.form['password'] != request.form['confirm_password']:
        flash(u"Passwords do not match",'confirm_password')
    

    if '_flashes' in session.keys():
        return redirect('/')
    else:
        pw_hash = bcrypt.generate_password_hash(request.form['password'])
        mysql = connectToMySQL("login_register_db")
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES(%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        data={
            'first_name':request.form['first_name'],
            'last_name':request.form['last_name'],
            'email':request.form['email'],
            'password':pw_hash
            }
        new_id= mysql.query_db(query,data)
        session['userid']=new_id
        session['first_name']=request.form['first_name']
        flash(u"You have successfully registered!",'success')
        return redirect('/success')


@app.route('/login', methods=['POST'])
def login():
    mysql = connectToMySQL("login_register_db")
    query = "SELECT * FROM users WHERE email= %(email)s;"
    data = { 'email': request.form['login_email'] }
    result = mysql.query_db(query,data)
    #print(request.form['login_email'])
    #print(len(request.form['login_email']))
    if len(request.form['login_email'])<1 or not EMAIL_REGEX.match(request.form['login_email']):
        flash(u"Cannot login", 'login_error')
    if result:
        if bcrypt.check_password_hash(result[0]['password'], request.form['login_password']):
            session['userid'] = result[0]['id']
            session['first_name']= result[0]['first_name']
            return redirect('/success')
        flash(u"You have not logged in",'login_error')
    else:
        flash(u"You have not logged in!",'login_error')
    if '_flashes' in session.keys():
        return redirect('/')


@app.route('/success')
def success(): 
    return render_template("success.html")

   

if __name__ == "__main__":
    app.run(debug=True)
