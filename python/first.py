from flask import Flask, request, render_template
import mysql.connector

app = Flask(__name__)

# MySQL connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Meet1326",
    database="employeedata"
)

cursor = db.cursor()

@app.route('/')
def form():
    return render_template('index.html')  # your HTML file

@app.route('/submit', methods=['POST'])
def submit():
    empid = request.form['empid']
    name = request.form['name']
    department = request.form['department']
    number = request.form['number']
    address = request.form['address']
    gender = request.form['gender']

    sql = """
    INSERT INTO empdata (empid, name, department, number, address, gender)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    values = (empid, name, department, number, address, gender)

    cursor.execute(sql, values)
    db.commit()

    return "Data Inserted Successfully!"

if __name__ == '__main__':
    app.run(debug=True)
