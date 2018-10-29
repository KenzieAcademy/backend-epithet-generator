from flask_testing import TestCase
import unittest
from app import app


class TestApp(TestCase):

    def create_app(self):
        return app


    def test_generate_epithet(self):
        res = self.client.get('/')
        self.assertIsInstance(res.json["epithets"].encode("utf-8"), str)

    def test_generate_epithet_by_amount(self):
        res = self.client.get('/')
        self.assertIsInstance(res.json["epithets"].encode("utf-8"), str)

if __name__ == '__main__':
    unittest.main()