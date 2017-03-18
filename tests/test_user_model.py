import unittest
from app.models import Users

class UserModelTestCase(unittest.TestCase):
    def test_password_setter(self):
        u = Users(password='test')
        self.assertTrue(u.password_hash is not None)

    def test_no_password_getter(self):
        u = Users(password='test')
        with self.assertRaises(AttributeError):
            u.password

    def test_password_verification(self):
        u = Users(password='test')
        self.assertTrue(u.verify_password('test'))
        self.assertFalse(u.verify_password('tes2t'))

    def test_password_salts_are_random(self):
        u = Users(password='test')
        u2 = Users(password='test')
        self.assertTrue(u.password_hash != u2.password_hash)