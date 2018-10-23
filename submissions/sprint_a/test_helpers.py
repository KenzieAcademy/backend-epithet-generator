import unittest

from helpers import FileManager
from helpers import EpithetGenerator
from helpers import Vocabulary

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
        self.assertTrue(Vocabulary.csv_reader(test_path), {"vocabulary": ["Blue", "Two", "Hoo"]})

class TestEpithetGenerator(unittest.TestCase):

    def test_random_words(self):
        self.assertEqual(EpithetGenerator.random_words(test_path), ['Blue', 'Two', 'Hoo'])

    def test_get_epithet(self):
        self.assertEqual(EpithetGenerator.get_epithet(test_path), "Thou Blue Two Hoo!!")

    def test_get_epithets(self):
        self.assertEqual(EpithetGenerator.get_epithets(test_path, 2), {'epithet': ["Thou Blue Two Hoo!!", "Thou Blue Two Hoo!!"]})

if __name__ == '__main__':
    unittest.main()