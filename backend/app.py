# backend/app.py

from flask import Flask, render_template, request, redirect, url_for
import random
import mysql.connector
from questions import questions

app = Flask(__name__)

# DB Config
db = mysql.connector.connect(
    host="db",           # service name from docker-compose
    user="root",
    password="rootpass",
    database="devops_exam"
)
cursor = db.cursor()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start_exam():
    name = request.form['name']
    gender = request.form['gender']
    email = request.form['email']

    # Store session data in hidden form for exam
    selected_questions = random.sample(questions, 15)

    return render_template('exam.html', name=name, gender=gender, email=email, questions=selected_questions)

@app.route('/submit', methods=['POST'])
def submit_exam():
    name = request.form['name']
    gender = request.form['gender']
    email = request.form['email']
    score = 0

    for i in range(15):
        q = request.form.get(f'q{i}')
        a = request.form.get(f'ans{i}')
        if q == a:
            score += 1

    # Store result in MySQL
    cursor.execute("INSERT INTO results (username, gender, email, score) VALUES (%s, %s, %s, %s)", (name, gender, email, score))
    db.commit()

    return render_template('result.html', name=name, score=score)

@app.route('/admin')
def admin_view():
    cursor.execute("SELECT username, gender, email, score FROM results")
    records = cursor.fetchall()
    return render_template('admin.html', records=records)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
