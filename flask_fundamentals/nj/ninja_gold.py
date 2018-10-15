from flask import Flask, session, redirect, request, render_template
import random
import datetime

app = Flask(__name__)
app.secret_key = 'ThisIsASecret'

print(__name__)         

@app.route('/')                       
def index():
   if session['total'] == None:
        session['total'] = 0
    return render_template('index.html', total=session['total'])

@app.route("/processing_money", method=[POST])
def calculateMoney():
# 1) Determine how to decide which form requested the money("hidden"?)
# 2) Create a random gold amount based on which form made the submission
# 3) Add/subtract requested_gold to the users total
# 4) Display new gold total on users web page
  hidden_input = request.form['hidden']
  if hidden_input == 'farm':
      gold_number = randint(10, 20)
      gold_acct_total = gold_acct_total + gold_number
      session['total'] += gold_range
      str = "Earned  " + gold_number + "golds from farm!"  + datetime()
    # return str to website activities box
    # return gold_acct_total to gold summary box
  elif hidden_input == 'cave':
    gold_number = randint(5, 10)
    gold_acct_total = gold_acct_total + gold_number
    session['total'] += gold_range
    str = "Earned  " + gold_number + "golds from cave!"  + datetime()
    # return str to website activities box
    # return gold_acct_total to gold summary box 
  elif hidden_input == 'house':
    old_number = randint(2, 5)
    session['total'] += gold_range
    gold_acct_total = gold_acct_total + gold_number
    str = "Earned  " + gold_number + "golds from house!"  + datetime()
    # return str to website activities box
    # return gold_acct_total to gold summary box
  else hidden_input == 'casino':
    gold_number = randint(-50, 50) 
    session['total'] += gold_range
    gold_acct_total = gold_acct_total + gold_number
    if gold_number > 0: 
      str = "Earned  " + gold_number + "golds from Casino!"  + datetime()
    else: 
      str = "Entered a casino and lost " + gold_number + "golds...ouch." + datetime()
    # return str to website activities box
    # return gold_acct_total to gold summary box
  return render_template('/')



if __name__=="__main__":
  app.run(debug=True) 