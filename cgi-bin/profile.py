import os
import cgi
import cgitb
import psycopg2
import html
from validators.validate_data import validate_name, validate_email, validate_password

cgitb.enable()
print("Content-Type: text/html; charset=utf-8\n")

form = cgi.FieldStorage()
old_email = form.getfirst("old_email")
method = "POST" if "first_name" in form else "GET"

if method == "GET":
    email = form.getfirst("email")
else:
    email = old_email

if not email:
    print("<h1>No email provided!</h1>")
    print('<a href="/cgi-bin/login.py">Go to login</a>')
    exit()

try:
    conn = psycopg2.connect(
        host="localhost",
        database="accounts",
        user="postgres",
        password="admin"
    )
    cur = conn.cursor()

    message = ""

    if method == "POST":
        first_name = form.getfirst("first_name", "").strip()
        last_name = form.getfirst("last_name", "").strip()
        new_email = form.getfirst("email", "").strip()
        password = form.getfirst("password", "").strip()

        for field, validator in [("First name", validate_name), ("Last name", validate_name),
                                 ("Email", validate_email), ("Password", validate_password)]:
            valid, msg = validator(locals()[field.lower().replace(" ", "_")])
            if not valid:
                print(f"<h1>{msg}</h1>")
                exit()

        cur.execute("""
            UPDATE users
            SET first_name=%s, last_name=%s, email=%s, password=%s
            WHERE email=%s
        """, (first_name, last_name, new_email, password, old_email))
        conn.commit()
        message = "<p style='color:green;'>Profile updated successfully!</p>"
        email = new_email

    cur.execute("SELECT first_name, last_name, email, password FROM users WHERE email=%s", (email,))
    user = cur.fetchone()
    if not user:
        print("<h1>User not found!</h1>")
        exit()

    first_name, last_name, email, password = map(html.escape, user)

    path = os.path.join(os.path.dirname(__file__), "../templates/profile.html")
    with open(os.path.abspath(path), "r", encoding="utf-8") as f:
        html_template = f.read()

    html_output = html_template.format(
        first_name=first_name,
        last_name=last_name,
        email=email,
        password=password,
        message=message
    )
    print(html_output)

except Exception as e:
    print(f"<h1>Database error: {e}</h1>")

finally:
    if 'conn' in locals():
        cur.close()
        conn.close()
