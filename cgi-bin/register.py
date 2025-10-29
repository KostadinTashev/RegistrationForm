import os
import psycopg2
import cgi
import cgitb
from validators.validate_data import validate_name, validate_email, validate_password
from validators.captcha import generate_captcha, verify_captcha

cgitb.enable()
print("Content-Type: text/html; charset=utf-8\n")
form = cgi.FieldStorage()

if "first_name" not in form or "last_name" not in form or "email" not in form or "password" not in form:
    captcha_code = generate_captcha()
    path = os.path.join(os.path.dirname(__file__), "../templates/registration_form.html")
    with open(os.path.abspath(path), "r", encoding="utf-8") as f:
        html_content = f.read()
    html_content = html_content.replace("{captcha}", captcha_code)
    html_content = html_content.replace("{captcha_hidden}",
                                        f'<input type="hidden" name="captcha_code" value="{captcha_code}">')
    print(html_content)
    exit()

first_name = form.getfirst("first_name", "").strip()
last_name = form.getfirst("last_name", "").strip()
email = form.getfirst("email", "").strip()
password = form.getfirst("password", "")
repeat_password = form.getfirst("repeat-password", "")
user_captcha = form.getfirst("captcha_input", "").strip()
true_captcha = form.getfirst("captcha_code", "").strip()

if not verify_captcha(user_captcha, true_captcha):
    print(f'Captcha validation failed.')
    print('<a href="/cgi-bin/register.py">Back</a>')
    exit()

valid, msg = validate_name(first_name)
if not valid:
    print(msg)
    exit()

valid, msg = validate_name(last_name)
if not valid:
    print(msg)
    exit()
valid, msg = validate_email(email)
if not valid:
    print(msg)
    exit()
valid, msg = validate_password(password)
if not valid:
    print(msg)
    exit()

if not all([first_name, last_name, email, password, repeat_password]):
    print("<h1>Please fill in all fields!</h1>")
    exit()

if password != repeat_password:
    print("<h1>Passwords do not match!</h1>")
    exit()
try:
    connection = psycopg2.connect(
        host="localhost",
        database="accounts",
        user="postgres",
        password="admin",
    )
    cursor = connection.cursor()
    cursor.execute(
        """
        INSERT INTO users (first_name, last_name, email, password)
        VALUES (%s, %s, %s, %s) RETURNING id;
        """, (first_name, last_name, email, password))
    connection.commit()
    print("<h1>Registered successfully!</h1>")
    print("<a href='/cgi-bin/login.py'>Click here to log in</a>")
except Exception as e:
    print(f"Error: {e}")
    print("<a href='/cgi-bin/register.py'>Back to registration</a>")
finally:
    if 'connection' in locals():
        cursor.close()
        connection.close()
