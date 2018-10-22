from helpers import FileManager
from helpers import Vocabulary
import unittest


class TestFileManager(unittest.TestCase):

    def test_get_extension(self):
        result = FileManager.get_extension()
        self.assertEqual(result, "")

    def test_read_json(self):
        result = FileManager.read_json()
        self.assertEqual(result, "")


class TestVocabulary():

    def test_from_file(self):
        result = Vocabulary.from_file()
        self.assertEqual(result, "")

    def test_from_json(self):
        result = Vocabulary.from_json()
        self.assertEqual(result, "")

    def test_strategies(self):
        result = Vocabulary.strategies()
        self.assertEqual(result, "")


if __name__ == '__main__':
    unittest.main()
