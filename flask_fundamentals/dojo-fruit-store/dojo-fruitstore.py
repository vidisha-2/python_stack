from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    strawberry_quantity = request.form['strawberry']
    raspberry_quantity = request.form['raspberry']
    apple_quantity = request.form['apple']
    user_firstname = request.form['first_name']
    user_lastname = request.form['last_name']
    user_id = request.form['student_id']
    print(user_id)
    total = int(strawberry_quantity)+int(raspberry_quantity)+int(apple_quantity)
    return render_template('checkout.html', total_items=total, strawberry=strawberry_quantity, raspberry=raspberry_quantity, apple=apple_quantity, first_name=user_firstname, last_name=user_lastname, student_id=user_id )

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    