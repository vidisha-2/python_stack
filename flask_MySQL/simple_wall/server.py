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
    if len(request.form['first_name'])<1 and len(request.form['last_name'])<1:
        flash(u"Name must be 3+ characters long",'first_name')
    if request.form['first_name'].isalpha()==False and request.form['last_name'].isalpha()==False:
        flash(u"Name must not contain any numbers",'first_name')
    if len(request.form['email'])<1 and not EMAIL_REGEX.match(request.form['email']):
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
        return redirect('/main-page')

@app.route('/login', methods=['POST'])
def login():
    mysql = connectToMySQL("login_register_db")
    query = "SELECT * FROM users WHERE email= %(email)s;"
    data = { 'email': request.form['login_email'] }
    result = mysql.query_db(query,data)
    if len(request.form['login_email'])<1 or not EMAIL_REGEX.match(request.form['login_email']):
        flash(u"Cannot login", 'login_error')
    if result:
        if bcrypt.check_password_hash(result[0]['password'], request.form['login_password']):
            session['userid'] = result[0]['id']
            session['first_name']= result[0]['first_name']
            return redirect('/main-page')
        flash(u"You have not logged in",'login_error')
    else:
        flash(u"You have not logged in!",'login_error')

    if '_flashes' in session.keys():
        return redirect('/')

@app.route('/create_message', methods=['POST'])
def create():
    
    #Inserting messages in the database
    mysql = connectToMySQL("login_register_db")
    query = "INSERT INTO messages (content, to_user_id, from_user_id, created_at, updated_at) VALUES(%(content)s, %(to_user_id)s, %(from_user_id)s, NOW(), NOW());"
    data = {
        'content':request.form['message'],
        'to_user_id':request.form['recepient_id'],
        'from_user_id':session['userid']
    }
    new_message = mysql.query_db(query,data)


    return redirect('/main-page')

   





@app.route('/main-page')
def main_page(): 
    #display total messages
    mysql = connectToMySQL("login_register_db")
    query = "SELECT COUNT(messages.id) AS number_of_messages FROM users JOIN messages ON users.id=messages.from_user_id WHERE users.id=%(value)s GROUP BY users.id;"
    data = { 'value': session['userid'] }
    total = mysql.query_db(query,data)
    if total == ():
        total = 0
    else:
        total = total[0]['number_of_messages']

    #total messages logged in user received
    mysql = connectToMySQL("login_register_db")
    query = "SELECT COUNT(messages.from_user_id) AS msgs FROM users JOIN messages ON users.id=messages.from_user_id WHERE messages.to_user_id=%(user_id)s;"
    data ={
            'user_id': session['userid']
    }
    msgs_received = mysql.query_db(query,data)
    if msgs_received ==():
        msgs_received=0
    else:
        msgs_received=msgs_received[0]['msgs']

    #displaying messages from friends    
    mysql = connectToMySQL("login_register_db")
    query = "SELECT messages.content, users.first_name, users.id, messages.id as m_id, messages.created_at FROM messages JOIN users ON users.id = messages.from_user_id WHERE messages.to_user_id = %(user_id)s;"
    data = { 'user_id': session['userid'] }
    friends = mysql.query_db(query,data)

    #displaying list of friends
    mysql = connectToMySQL("login_register_db")
    query = "SELECT users.id, users.first_name FROM users WHERE id != %(userid)s;"
    data = { 'userid':session['userid'] }
    msg = mysql.query_db(query,data)  
    print(msg)
    return render_template("main-page.html", totalmessages=total, msg_count=msgs_received, myfriends=friends, messages_from=msg)

@app.route('/delete/<id>')
def delete(id):
    mysql = connectToMySQL("login_register_db")
    query = "DELETE from messages where messages.id=%(id)s"
    data = { 'id' : id }
    result= mysql.query_db(query,data)

    return redirect('/main-page') 



if __name__ == "__main__":
    app.run(debug=True)
