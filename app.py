from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import date

app = Flask(__name__)

# Initialize database
def init_db():
    conn = sqlite3.connect('attendance.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    ''')
    c.execute('''
        CREATE TABLE IF NOT EXISTS attendance (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER,
            date TEXT,
            status TEXT,
            FOREIGN KEY (student_id) REFERENCES students (id)
        )
    ''')
    conn.commit()
    conn.close()

# Home page
@app.route('/')
def index():
    return render_template('index.html')

# Mark attendance
@app.route('/mark', methods=['GET', 'POST'])
def mark_attendance():
    conn = sqlite3.connect('attendance.db')
    c = conn.cursor()

    if request.method == 'POST':
        student_id = request.form['student_id']
        status = request.form['status']
        c.execute('INSERT INTO attendance (student_id, date, status) VALUES (?, ?, ?)',
                  (student_id, date.today(), status))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))

    c.execute('SELECT * FROM students')
    students = c.fetchall()
    conn.close()
    return render_template('mark_attendance.html', students=students)

# View attendance records
@app.route('/view')
def view_attendance():
    conn = sqlite3.connect('attendance.db')
    c = conn.cursor()
    c.execute('''
        SELECT students.name, attendance.date, attendance.status
        FROM attendance
        JOIN students ON students.id = attendance.student_id
        ORDER BY attendance.date DESC
    ''')
    records = c.fetchall()
    conn.close()
    return render_template('view_attendance.html', records=records)

# Run app and initialize database
if __name__ == '__main__':
    init_db()
    app.run(debug=True)
