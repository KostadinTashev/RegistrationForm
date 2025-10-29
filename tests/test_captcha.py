import unittest
from validators.captcha import generate_captcha, verify_captcha


class TestCaptcha(unittest.TestCase):
    def test_captcha_length(self):
        captcha = generate_captcha()
        self.assertEqual(len(captcha), 5)

    def test_captcha_characters(self):
        captcha = generate_captcha()
        for char in captcha:
            self.assertTrue(char.isalnum())

    def test_verify_valid_captcha(self):
        true_captcha = 'Auwb8'
        user_input = 'Auwb8'
        self.assertTrue(verify_captcha(true_captcha, user_input))

    def test_verify_invalid_captcha(self):
        true_captcha = 'Ki90w'
        user_input = 'Ko90W'
        self.assertFalse(verify_captcha(true_captcha, user_input))

    def test_verify_invalid_captcha_with_empty_input(self):
        true_captcha = 'Lsad9'
        user_input = ''
        self.assertFalse(verify_captcha(true_captcha, user_input))

    def test_verify_invalid_captcha_with_whitespaces(self):
        true_captcha = 'Kol8w'
        user_input = 'Kol8W   '
        self.assertFalse(verify_captcha(true_captcha, user_input))


if __name__ == '__main__':
    unittest.main()
