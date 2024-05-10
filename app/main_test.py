import unittest
from main import return_backwards_string, get_mode
import os

class TestMain(unittest.TestCase):
    def test_return_backwards_string(self):
        self.assertEqual(return_backwards_string('hello'), 'olleh')
        self.assertEqual(return_backwards_string('hello world'), 'dlrow olleh')
        self.assertEqual(return_backwards_string('123456789'), '987654321')
        self.assertEqual(return_backwards_string('!@#$%^&*()'), ')(*&^%$#@!')
        self.assertEqual(return_backwards_string(''), '')

    def test_get_mode(self):
        self.assertEqual(get_mode(), os.environ.get('MODE'))


if __name__ == '__main__':
    unittest.main()