from helpers import FileManager
from helpers import Vocabulary
import unittest
import json
import os


def createJSON():
        data = {
            "1": "foo",
            "2": "bar"
        }
        files = os.listdir(os.getcwd())
        if 'data.json' not in files:
            with open('data.json', "w") as output:
                json.dump(data, output)
        path = os.path.join(os.getcwd(), 'data.json')
        return path


class TestFileManager(unittest.TestCase):

    def test_get_extension(self):
        result = FileManager.get_extension(
            "./backend-epithet-generator/submissions/sprint_b/data.json"
            )
        self.assertEqual(result, "json")

    def test_read_json(self):
        path = createJSON()
        result = FileManager.read_json(path)
        self.assertEqual(result, {u'1': u'foo', u'2': u'bar'})
        os.remove('data.json')


class TestVocabulary(unittest.TestCase):

    def test_from_file(self):
        path = createJSON()
        result = Vocabulary.from_file(path)
        self.assertEqual(result, ({u'1': u'foo', u'2': u'bar'}, [u'1', u'2']))
        os.remove('data.json')

