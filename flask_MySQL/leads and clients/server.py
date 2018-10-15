from flask import Flask, render_template, request, redirect
from mysqlconnection import connectToMySQL
app = Flask(__name__)

@app.route('/')
def index():
    mysql=connectToMySQL("lead_gen_business")
    all_friends=mysql.query_db("SELECT clients.first_name, clients.last_name, COUNT(leads.leads_id) AS number_of_leads FROM leads JOIN sites ON sites.site_id = leads.site_id JOIN clients on clients.client_id = sites.client_id GROUP BY(clients.first_name)")
    print("Display CLients And Leads", all_friends)
    return render_template('index.html', clientsandleads = all_friends)

# invoke the connectToMySQL function and pass it the name of the database we're using
# connectToMySQL returns an instance of MySQLConnection, which we will store in the variable 'mysql'
@app.route('/update', methods=['POST'])
def update():
    print(request.form)
    mysql=connectToMySQL("lead_gen_business")
    query= "SELECT clients.first_name, clients.last_name, COUNT(leads.leads_id) AS number_of_leads FROM leads JOIN sites ON sites.site_id = leads.site_id JOIN clients on clients.client_id = sites.client_id Where leads.registered_datetime Between %(start_date)s AND %(end_date)s GROUP BY clients.first_name;"
    data = {
            'start_date':request.form['start_date'],
            'end_date':request.form['end_date']
    }
    all_friends = mysql.query_db(query,data)

    print("Update CLients And Leads", all_friends)
    return render_template('index.html', clientsandleads = all_friends)

if __name__ == "__main__":
    app.run(debug=True)
