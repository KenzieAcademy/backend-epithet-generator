import unittest
from helpers import FileManager
import json

path = ('/Users/ethansternke/Documents/Kenzie/back-end'
        '/backend-epithet-generator/resources/data.json')

json_data = json.load(open(path))


class TestFileManager(unittest.TestCase):
    def test_get_extension(self):
        self.assertEqual(FileManager.get_extension(path), 'json')

    def test_read_json(self):
        self.assertEqual(FileManager.read_json(path), json_data)


if __name__ == '__main__':
    unittest.main()
