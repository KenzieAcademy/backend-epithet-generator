import unittest
import pytest

from sprint_c.helpers import FileManager
from sprint_c.helpers import EpithetGenerator
from sprint_c.helpers import Vocabulary


#fix this
test_path = '/Users/aj/Documents/Back-End/backend-epithet-generator/resources/test.json'

test_dict = {
    "Red": [
        "Blue"
    ],
    "One": [
        "Two"
    ],
    "Yoo": [
        "Hoo"
    ]
}


class TestFileManager(unittest.TestCase):

    def test_get_extension(self):
        self.assertEqual(FileManager.get_extension(test_path), 'json')

    def test_read_json(self):
        self.assertEqual(FileManager.read_json(test_path), test_dict)


class TestVocabulary(unittest.TestCase):

    def test_from_file(self):
        self.assertEqual(Vocabulary.from_file(test_path), test_dict)

    def test_from_json(self):
        self.assertEqual(Vocabulary.from_json(test_path), test_dict)

    def test_strategies(self):
        self.assertTrue(Vocabulary.strategies('json'))

    def test_csv(self):
        self.assertTrue(Vocabulary.csv_reader(test_path), {
                        "vocabulary": ["Blue", "Two", "Hoo"]})


class TestEpithetGenerator(unittest.TestCase):

    def test_random_words(self):
        self.assertEqual(EpithetGenerator.random_words(
            test_path), ['Blue', 'Two', 'Hoo'])

    def test_get_epithet(self):
        self.assertEqual(EpithetGenerator.get_epithet(
            test_path), "Thou Blue Two Hoo!!")

    def test_get_epithets(self):
        self.assertEqual(EpithetGenerator.get_epithets(test_path, 2), {
                         'epithet': ["Thou Blue Two Hoo!!", "Thou Blue Two Hoo!!"]})


@pytest.fixture
def client():
    from .app import app
    return app


def test_get(client):
    result = client.test_client().get('/')
    assert isinstance(result.data.decode('utf-8'),
                        str) == True
    assert result.status_code == 200


def test_get_vocabulary(client):
    result = client.test_client().get('/vocabulary')
    print(result)
    assert isinstance(result.data.decode('utf-8'),
                        str) == True
    assert result.status_code == 200


def test_get_amount(client):
    result = client.test_client().get('/epithets/3')
    print(result)
    assert isinstance(result.data.decode('utf-8'),
                        str) == True
    assert result.status_code == 200


def test_get_random_amount(client):
    result = client.test_client().get('/epithets/random')
    print(result)
    assert isinstance(result.data.decode('utf-8'),
                        str) == True
    assert result.status_code == 200


if __name__ == '__main__':
    unittest.main()
