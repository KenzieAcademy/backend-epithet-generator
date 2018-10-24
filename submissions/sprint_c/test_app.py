from flask_testing import TestCase

from sprint_c.app import app


class AppTest(TestCase):
    def create_app(self):
        self.app = app
        self.app.config['TESTING'] = True
        return self.app

    def test_single_epithet(self):
        assert self.client.get('/').status_code == 200
        assert self.client.get('/').data

    def test_vocabulary(self):
        assert self.client.get('/vocabulary').status_code == 200
        assert self.client.get('/vocabulary').data

    def test_multiple_epithets(self):
        assert self.client.get('/epithets/4').status_code == 200
        assert self.client.get('/epithets/4').data

    def test_random_epithets(self):
        assert self.client.get('/epithets/random').status_code == 200
        assert self.client.get('/epithets.random').data

    def test_bad_path(self):
        assert self.client.get('/unicorn').status_code == 404
