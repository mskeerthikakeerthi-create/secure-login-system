from flask import Flask, render_template, request, redirect, url_for, session
from flask_bcrypt import Bcrypt
from datetime import datetime
import sqlite3

app = Flask(__name__)
app.secret_key = "secureloginproject"

bcrypt = Bcrypt(app)

def init_db():
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        email TEXT,
        password TEXT
    )
    """)

    conn.commit()
    conn.close()

init_db()

@app.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':

        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        if len(username) < 3:
            return "Username must be at least 3 characters"

        if len(password) < 8:
            return "Password must be at least 8 characters"

        hashed = bcrypt.generate_password_hash(password).decode('utf-8')

        try:
            conn = sqlite3.connect("database.db")
            cur = conn.cursor()

            cur.execute(
                "INSERT INTO users(username,email,password) VALUES(?,?,?)",
                (username, email, hashed)
            )

            conn.commit()
            conn.close()

            return redirect('/login')

        except:
            return "Username already exists"

    return render_template("register.html")

@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect("database.db")
        cur = conn.cursor()

        cur.execute(
            "SELECT * FROM users WHERE username=?",
            (username,)
        )
        user = cur.fetchone()
        conn.close()

        if user and bcrypt.check_password_hash(user[3], password):
            session['user'] = username
            return redirect('/dashboard')
        return "Invalid Credentials"
    return render_template("login.html")

@app.route('/dashboard')
def dashboard():

    if 'user' not in session:
        return redirect('/login')

    conn = sqlite3.connect("database.db")
    cur = conn.cursor()

    cur.execute("SELECT COUNT(*) FROM users")
    total_users = cur.fetchone()[0]

    conn.close()

    return render_template(
        "dashboard.html",
        username=session['user'],
        total_users=total_users
    )

@app.route('/security')
def security():

    if 'user' not in session:
        return redirect('/login')

    return render_template("security.html")

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')
if __name__ == '__main__':
    app.run(debug=True)