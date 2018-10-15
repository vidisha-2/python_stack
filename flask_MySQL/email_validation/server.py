from flask import Flask, render_template, request, redirect, flash, session
from mysqlconnection import connectToMySQL
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = "AlwaysHungry!"

@app.route('/')
def index():
    mysql=connectToMySQL("registration")
    all_users=mysql.query_db("SELECT * from email_addresses;")
    print("-"*80, all_users)
    return render_template('index.html', email_id = all_users)


@app.route('/go', methods=['POST'])
def submit():
    mysql=connectToMySQL("registration")
    all_users=mysql.query_db("SELECT * from email_addresses;")
    if len(request.form['email']) < 1:
        flash("Email cannot be blank!")
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
    else:
       for email in all_users:
        if request.form['email'].lower()==email['email'].lower():
            flash('The email is already taken')

    if '_flashes' not in session:
        mysql=connectToMySQL("registration")
        query= "INSERT INTO email_addresses (email, created_at, updated_at) VALUES (%(email)s, NOW(), NOW());"
        data = {
            'email':request.form['email']
            }
        new_entry = mysql.query_db(query,data)
        return redirect('/success')
    else:
        return redirect('/')

@app.route('/success')
def success():
    mysql=connectToMySQL("registration")
    print_email= mysql.query_db("SELECT email, created_at AS date_time from email_addresses;")
    print(print_email)
    for key in print_email:
        print(key['email'])
        print(key['date_time'])
     
    return render_template('success.html', email_id=print_email)

   

if __name__ == "__main__":
    app.run(debug=True)
