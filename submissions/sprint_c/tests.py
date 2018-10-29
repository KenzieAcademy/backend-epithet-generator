import unittest

from flask_testing import TestCase

from app import app


class TestApp(TestCase):
    def create_app(self):
        print("==> Creating test app")
        global app
        app = app
        app.config['TESTING'] = True
        return app

    def test_root(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status, '200 OK')
        self.assertTrue(resp.json.get('epithet'))
        self.assertTrue(isinstance(resp.json.get('epithet'), str))
        self.assertEqual(len(resp.json.get('epithet').split(' ')), 4)

    def test_epithets_quantity(self):
        resp = self.client.get('/epithets/5')
        self.assertEqual(resp.status, '200 OK')
        self.assertTrue(resp.json.get('epithets'))
        self.assertTrue(isinstance(resp.json.get('epithets'), list))
        self.assertTrue(len(resp.json.get('epithets')) is 5)

    def test_vocabulary(self):
        resp = self.client.get('/vocabulary')
        self.assertEqual(resp.status, '200 OK')
        self.assertTrue(resp.json['vocabulary'].get('Column 1'))
        self.assertTrue(resp.json['vocabulary'].get('Column 2'))
        self.assertTrue(resp.json['vocabulary'].get('Column 3'))
        self.assertNotIn('Column 4', resp.json)
        self.assertTrue(
            isinstance(
                resp.json['vocabulary'].get('Column 1'),
                list
            )
        )
        self.assertTrue(
            isinstance(
                resp.json['vocabulary'].get('Column 2'),
                list
            )
        )
        self.assertTrue(
            isinstance(
                resp.json['vocabulary'].get('Column 3'),
                list
            )
        )

    def test_epithets_quantity_random(self):
        resp = self.client.get('/random')
        self.assertEqual(resp.status, '200 OK')
        self.assertTrue(resp.json.get('random_epithets'))
        self.assertTrue(isinstance(resp.json.get('random_epithets'), list))
        self.assertTrue(len(resp.json.get('random_epithets')) <= 100)
        self.assertTrue(len(resp.json.get('random_epithets')) >= 1)


if __name__ == '__main__':
    unittest.main()
