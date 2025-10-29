import os
import cgi
import cgitb
import psycopg2
from validators.captcha import generate_captcha, verify_captcha

cgitb.enable()
print("Content-Type: text/html; charset=utf-8\n")

form = cgi.FieldStorage()
email = form.getfirst("email", "").strip()
password = form.getfirst("password", "").strip()
user_captcha = form.getfirst("captcha_input", "").strip()
true_captcha = form.getfirst("captcha_code", "").strip()

if not form or (not email and not password):
    captcha_code = generate_captcha()
    path = os.path.join(os.path.dirname(__file__), "../templates/sign_in_form.html")
    with open(os.path.abspath(path), "r", encoding="utf-8") as f:
        html_content = f.read()
    html_content = html_content.replace("{captcha}", captcha_code)
    html_content = html_content.replace(
        "{captcha_hidden}",
        f'<input type="hidden" name="captcha_code" value="{captcha_code}">'
    )
    print(html_content)
    exit()

if not email or not password:
    print("<h1>Please enter your email and password</h1>")
    print('<a href="/cgi-bin/login.py">Back to login</a>')
    exit()

if not verify_captcha(user_captcha, true_captcha):
    print("<h1>Invalid captcha</h1>")
    print('<a href="/cgi-bin/login.py">Back to login</a>')
    exit()

try:
    connection = psycopg2.connect(
        host="localhost",
        database="accounts",
        user="postgres",
        password="admin"
    )
    cursor = connection.cursor()
    cursor.execute(
        "SELECT * FROM users WHERE email = %s AND password = %s",
        (email, password)
    )
    user = cursor.fetchone()

    if user:
        print(f"""
            <html><body>
            <meta http-equiv="refresh" content="0; url=/cgi-bin/profile.py?email={email}">
            </body></html>
        """)
        exit()
    else:
        print("<h1>Invalid email or password</h1>")
        print('<a href="/cgi-bin/login.py">Try again</a>')

except Exception as e:
    print(f"<h1>Database error: {e}</h1>")

finally:
    if "connection" in locals():
        cursor.close()
        connection.close()
