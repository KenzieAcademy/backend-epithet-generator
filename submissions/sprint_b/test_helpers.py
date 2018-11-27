from helpers import FileManager
from helpers import Vocabulary
import unittest
import json
import time
import os



class TestFileManager(unittest.TestCase):

    def setUp(self):
        data = {
            "1": "foo",
            "2": "bar"
        }
        files = os.listdir(os.getcwd())
        if 'data.json' not in files:
            with open('data.json', "w") as output:
                json.dump(data, output)
        self.path = os.path.join(os.getcwd(), 'data.json')

    def test_get_extension(self):
        file_manager = FileManager()
        result = file_manager.get_extension(
            "./backend-epithet-generator/submissions/sprint_b/data.json"
            )
        self.assertEqual(result, "json")

    def test_read_json(self):
        file_manager = FileManager()
        result = file_manager.read_json(self.path)
        self.assertEqual(result, {u'1': u'foo', u'2': u'bar'})

    def tearDown(self):
        os.remove('data.json')


class TestVocabulary(unittest.TestCase):

    def setUp(self):
        data = {
            "1": "foo",
            "2": "bar"
        }
        files = os.listdir(os.getcwd())
        if 'data.json' not in files:
            with open('data.json', "w") as output:
                json.dump(data, output)
        self.path = os.path.join(os.getcwd(), 'data.json')

    def test_from_file(self):
        vocabulary = Vocabulary()
        result = vocabulary.from_file(self.path)
        self.assertEqual(result, ({u'1': u'foo', u'2': u'bar'}, [u'1', u'2']))

    def test_from_file_sad(self):
        files = os.listdir(os.getcwd())
        if 'test.txt' not in files:
            with open('test.txt', "w"):
                pass
        path = os.path.join(os.getcwd(), 'test.txt')
        with self.assertRaises(KeyError):
            Vocabulary.from_file(path)
        os.remove('test.txt')

    def test_from_json(self):
        vocabulary = Vocabulary()
        result = vocabulary.from_json(self.path)
        self.assertEqual(result, ({u'1': u'foo', u'2': u'bar'}, [u'1', u'2']))

    def test_strategies(self):
        vocabulary = Vocabulary()
        result = vocabulary.strategies("json")
        self.assertTrue(result)

    def tearDown(self):
        os.remove('data.json')
