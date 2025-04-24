from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os

app = Flask(__name__)
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE = os.path.join(BASE_DIR, 'sqa.db')

# Database initialization
def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS bugs (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        title TEXT NOT NULL,
                        description TEXT,
                        steps TEXT,
                        severity TEXT,
                        status TEXT DEFAULT 'Open',
                        assigned_to TEXT
                    )''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS test_cases (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        test_id TEXT,
                        description TEXT,
                        steps TEXT,
                        expected_result TEXT,
                        status TEXT
                    )''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/bugs')
def bugs():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM bugs")
    all_bugs = cursor.fetchall()
    conn.close()
    return render_template('bugs.html', bugs=all_bugs)

@app.route('/add_bug', methods=['GET', 'POST'])
def add_bug():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        steps = request.form['steps']
        severity = request.form['severity']
        assigned_to = request.form['assigned_to']

        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO bugs (title, description, steps, severity, assigned_to) VALUES (?, ?, ?, ?, ?)",
                       (title, description, steps, severity, assigned_to))
        conn.commit()
        conn.close()
        return redirect(url_for('bugs'))
    return render_template('bug_form.html')

@app.route('/test_cases')
def test_cases():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM test_cases")
    all_cases = cursor.fetchall()
    conn.close()
    return render_template('test_cases.html', test_cases=all_cases)

@app.route('/add_test_case', methods=['GET', 'POST'])
def add_test_case():
    if request.method == 'POST':
        test_id = request.form['test_id']
        description = request.form['description']
        steps = request.form['steps']
        expected_result = request.form['expected_result']
        status = request.form['status']

        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO test_cases (test_id, description, steps, expected_result, status) VALUES (?, ?, ?, ?, ?)",
                       (test_id, description, steps, expected_result, status))
        conn.commit()
        conn.close()
        return redirect(url_for('test_cases'))
    return render_template('test_case_form.html')

if __name__ == '__main__':
    init_db()
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
