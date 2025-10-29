import re


def validate_name(name):
    if not name.isalpha():
        return False, 'Name must contain only letters.'
    if len(name) < 2:
        return False, 'Name must contain at least 2 characters.'
    return True, ""


def validate_email(email):
    pattern = r'^[\w\w.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, email):
        return True, ''
    return False, "Email address must contain a valid email address."


def validate_password(password):
    if len(password) < 8:
        return False, 'Password must contain at least 8 characters.'
    if len(re.findall(r"\d", password)) < 2:
        return False, "Password must contain at least 2 digits."
    if not re.search(r"[A-Z]", password):
        return False, "Password must contain at least 1 uppercase letter"
    return True, ""
