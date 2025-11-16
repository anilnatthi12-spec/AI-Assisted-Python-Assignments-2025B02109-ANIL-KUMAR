# insecure_login.py  <-- BAD: example of insecure AI output
from flask import Flask, request, session, redirect

app = Flask(__name__)
app.secret_key = "supersecret"  # hardcoded secret — bad

# AI has hardcoded credentials:
USER = {"username": "admin", "password": "Admin123"}  # plain-text password — terrible

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        u = request.form.get("username")
        p = request.form.get("password")
        # insecure check: compares plaintext password directly
        if u == USER["username"] and p == USER["password"]:
            session["user"] = u
            return "Logged in!"
        return "Invalid"
    return '''
      <form method="post">
        <input name="username">
        <input name="password" type="password">
        <input type="submit">
      </form>
    '''

@app.route("/secret")
def secret():
    if session.get("user"):
        return "Secret data!"
    return redirect("/login")

if __name__ == "__main__":
    app.run(debug=True)
# secure_app.py  -- improved, but still a simple example for learning/testing
import os
import sqlite3
import time
from datetime import timedelta
from flask import Flask, request, session, redirect, g, render_template_string, flash
from werkzeug.security import generate_password_hash, check_password_hash

# Configuration - do NOT hardcode secrets in production.
# Set environment variables before running:
#   export FLASK_SECRET_KEY="replace-with-strong-random-value"
#   export DATABASE="auth.db"
SECRET_KEY = os.getenv("FLASK_SECRET_KEY")
if not SECRET_KEY:
    # Small convenience fallback for local testing only.
    # In real deployments, fail hard if SECRET_KEY not set.
    SECRET_KEY = "dev-fallback-secret-key"
    print("WARNING: using fallback secret key. Set FLASK_SECRET_KEY in production!")

DATABASE = os.getenv("DATABASE", "auth.db")
LOCKOUT_THRESHOLD = 5       # failed attempts before temporary lockout
LOCKOUT_WINDOW_SECONDS = 300  # 5 minutes lockout

app = Flask(__name__)
app.secret_key = SECRET_KEY
app.permanent_session_lifetime = timedelta(hours=1)

# Session cookie config - ensure these are set when running under HTTPS
app.config.update(
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SECURE=False,  # Set to True when serving over HTTPS
    SESSION_COOKIE_SAMESITE="Lax"
)

# Simple in-memory failed login tracker (demo). Use persistent store in prod.
failed_logins = {}  # { username_or_ip : {"count": int, "first_fail_ts": float, "locked_until": float} }

# --- DB helpers --------------------------------------------------------------
def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(DATABASE, detect_types=sqlite3.PARSE_DECLTYPES)
        g.db.row_factory = sqlite3.Row
    return g.db

@app.teardown_appcontext
def close_db(exc):
    db = g.pop("db", None)
    if db:
        db.close()

def init_db():
    db = get_db()
    db.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)
    db.commit()

# --- Security helpers -------------------------------------------------------
def is_locked(key):
    info = failed_logins.get(key)
    if not info:
        return False
    locked_until = info.get("locked_until", 0)
    if locked_until and time.time() < locked_until:
        return True
    # cleanup expired lock
    if locked_until and time.time() >= locked_until:
        failed_logins.pop(key, None)
    return False

def record_failed(key):
    info = failed_logins.setdefault(key, {"count": 0, "first_fail_ts": time.time(), "locked_until": 0})
    info["count"] += 1
    # apply lockout
    if info["count"] >= LOCKOUT_THRESHOLD:
        info["locked_until"] = time.time() + LOCKOUT_WINDOW_SECONDS

def reset_failed(key):
    failed_logins.pop(key, None)

# --- Routes ------------------------------------------------------------------
@app.route("/")
def index():
    user = session.get("user")
    return f"Hello, {user or 'guest'}! <a href='/login'>Login</a> | <a href='/register'>Register</a> | <a href='/secret'>Secret</a>"

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")
        if not username or not password:
            flash("username and password required", "error")
            return redirect("/register")

        # Basic password policy check (example)
        if len(password) < 8:
            flash("Password must be at least 8 characters", "error")
            return redirect("/register")

        password_hash = generate_password_hash(password)  # PBKDF2 by default

        db = get_db()
        try:
            db.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)", (username, password_hash))
            db.commit()
        except sqlite3.IntegrityError:
            flash("username already exists", "error")
            return redirect("/register")

        flash("registration successful, please login", "success")
        return redirect("/login")

    return render_template_string("""
    <h2>Register</h2>
    <form method="post">
      <input name="username" placeholder="username" required><br>
      <input type="password" name="password" placeholder="password" required><br>
      <button type="submit">Register</button>
    </form>
    """)

@app.route("/login", methods=["GET", "POST"])
def login():
    client_ip = request.remote_addr or "unknown"
    key = f"{client_ip}"  # use username+ip for more refined tracking
    if is_locked(key):
        return "Too many failed attempts. Try again later.", 429

    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")

        # Parameterized query -> avoids SQL injection
        db = get_db()
        cur = db.execute("SELECT id, username, password_hash FROM users WHERE username = ?", (username,))
        row = cur.fetchone()

        if row and check_password_hash(row["password_hash"], password):
            # Successful login
            session.permanent = True
            session["user"] = row["username"]
            # reset failure counter
            reset_failed(key)
            flash("Logged in", "success")
            return redirect("/")
        else:
            # record failure (use username+ip as key in production)
            record_failed(key)
            flash("Invalid credentials", "error")
            return redirect("/login")

    return render_template_string("""
    <h2>Login</h2>
    {% with messages = get_flashed_messages(with_categories=true) %}
      {% for cat, msg in messages %}
        <div>{{ msg }}</div>
      {% endfor %}
    {% endwith %}
    <form method="post">
      <input name="username" placeholder="username" required><br>
      <input type="password" name="password" placeholder="password" required><br>
      <button type="submit">Login</button>
    </form>
    """)

@app.route("/logout")
def logout():
    session.pop("user", None)
    flash("Logged out", "info")
    return redirect("/")

@app.route("/secret")
def secret():
    if not session.get("user"):
        return redirect("/login")
    return "Very secret data for authenticated users only."

# --- convenience run --------------------------------------------------------
if __name__ == "__main__":
    with app.app_context():
        init_db()
    # In production: run with a real WSGI server and set SESSION_COOKIE_SECURE=True and use HTTPS
    app.run(host="0.0.0.0", port=5000, debug=False)
