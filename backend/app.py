from flask import Flask, render_template, request, redirect, url_for
import random
import mysql.connector
from questions import questions
import os

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv('MYSQL_HOST', 'mysql'),  # Default to 'mysql' service name
        user=os.getenv('MYSQL_USER', 'root'),
        password=os.getenv('MYSQL_PASSWORD', 'rootpass'),
        database=os.getenv('MYSQL_DATABASE', 'devops_exam')
    )

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start_exam():
    name = request.form['name']
    gender = request.form['gender']
    email = request.form['email']
    selected_questions = random.sample(questions, 15)
    return render_template('exam.html', name=name, gender=gender, email=email, questions=selected_questions)

@app.route('/submit', methods=['POST'])
def submit_exam():
    try:
        db = get_db_connection()
        cursor = db.cursor()
        
        name = request.form['name']
        gender = request.form['gender']
        email = request.form['email']
        score = sum(1 for i in range(15) if request.form.get(f'q{i}') == request.form.get(f'ans{i}'))

        cursor.execute(
            "INSERT INTO results (username, gender, email, score) VALUES (%s, %s, %s, %s)",
            (name, gender, email, score)
        )
        db.commit()
        return render_template('result.html', name=name, score=score)
    except Exception as e:
        app.logger.error(f"Database error: {str(e)}")
        return "Database error occurred", 500
    finally:
        if 'db' in locals():
            db.close()

@app.route('/admin')
def admin_view():
    try:
        db = get_db_connection()
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT username, gender, email, score FROM results")
        records = cursor.fetchall()
        return render_template('admin.html', records=records)
    except Exception as e:
        app.logger.error(f"Database error: {str(e)}")
        return "Database error occurred", 500
    finally:
        if 'db' in locals():
            db.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
