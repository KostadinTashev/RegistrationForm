import random
import string


def generate_captcha(length=5):
    symbols = string.ascii_letters + string.digits
    return ''.join(random.choice(symbols) for _ in range(length))


def verify_captcha(user_input, true_captcha):
    if not user_input or not true_captcha:
        return False
    return user_input.strip() == true_captcha.strip()
