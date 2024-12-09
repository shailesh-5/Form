from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# MySQL database connection
def get_db_connection():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',  # replace with your MySQL username
        password='Shailesh',  # replace with your MySQL password
        database='student_db'
    )
    return connection

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_student', methods=['POST'])
def add_student():
    name = request.form['name']
    age = request.form['age']
    email = request.form['email']

    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('INSERT INTO students (name, age, email) VALUES (%s, %s, %s)', (name, age, email))
    connection.commit()
    cursor.close()
    connection.close()

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)