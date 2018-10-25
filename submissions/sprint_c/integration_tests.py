from app import app as app_instance
import unittest
from flask_testing import TestCase


class AppTestCase(TestCase):
    def create_app(self):
        print('==> Setting up the env for tests!')
        self.app = app_instance
        self.app.config['TESTING'] = True
        return self.app

    def tearDown(self):
        print('==> Tearing down after tests!')

    def test_root(self):
        resp = self.client.get('/')
        assert "200 OK" == resp.status
        assert "epithet" in resp.data

    def test_vocab(self):
        resp = self.client.get('/vocabulary')
        assert "200 OK" == resp.status
        assert "vocabulary" in resp.data

    def test_epithets(self):
        resp = self.client.get('/epithets')
        assert "200 OK" == resp.status
        assert "epithets" in resp.data


if __name__ == '__main__':
    unittest.main()
