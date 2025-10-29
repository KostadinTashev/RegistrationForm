import unittest
from validators.validate_data import validate_name, validate_email, validate_password


class TestValidateData(unittest.TestCase):
    def test_validate_name(self):
        valid, msg = validate_name("Kostadin")
        self.assertTrue(valid)

    def test_name_not_contains_at_least_two_chars(self):
        valid, msg = validate_name("k")
        self.assertFalse(valid)
        self.assertEqual(msg, "Name must contain at least 2 characters.")

    def test_name_contains_at_least_two_chars(self):
        valid, msg = validate_name("Kost")
        self.assertTrue(valid)

    def test_only_letters(self):
        valid, msg = validate_name("Kostadin123")
        self.assertFalse(valid)
        self.assertEqual(msg, "Name must contain only letters.")

    def test_validate_email(self):
        valid, msg = validate_email("kostadin0420@abv.bg")
        self.assertTrue(valid)

    def test_invalid_email(self):
        valid, msg = validate_email("kostadin0420")
        self.assertFalse(valid)
        self.assertEqual(msg, "Email address must contain a valid email address.")

    def test_email_missing_domain(self):
        valid, msg = validate_email("kostadin@")
        self.assertFalse(valid)
        self.assertEqual(msg, "Email address must contain a valid email address.")

    def test_validate_password(self):
        valid, msg = validate_password("Kostadin02")
        self.assertTrue(valid)

    def test_password_less_than_eight_characters(self):
        valid, msg = validate_password("Kost02")
        self.assertFalse(valid)
        self.assertEqual(msg, "Password must contain at least 8 characters.")

    def test_password_not_contains_at_least_two_digits(self):
        valid, msg = validate_password("Kostadin0")
        self.assertFalse(valid)
        self.assertEqual(msg, "Password must contain at least 2 digits.")

    def test_password_missing_uppercase(self):
        valid, msg = validate_password("password12")
        self.assertFalse(valid)
        self.assertEqual(msg, "Password must contain at least 1 uppercase letter")


if __name__ == '__main__':
    unittest.main()
