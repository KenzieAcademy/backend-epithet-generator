import os
import json
import unittest

from .helpers import FileManager, Vocabulary, EpithetGenerator

path = os.getenv("VOCAB_FILE_PATH")


class FileManagerTest(unittest.TestCase):
    """Tests the FileManager class in helpers.py"""
    def test_get_extension(self):
        self.assertEqual(FileManager.get_extension(path), "json")

    def test_read_json(self):
        with open(os.path.abspath(path)) as file:
            self.assertEqual(json.loads(file.read()), FileManager.read_json(
                os.path.abspath(path)))

    def test_read_json_sad(self):
        with self.assertRaises(FileNotFoundError):
            FileManager.read_json("/this/is/not/a/path")


class VocabularyTest(unittest.TestCase):
    """Tests the Vocabulary class in helpers.py"""
    def test_from_file_sad_path(self):
        with self.assertRaises(KeyError):
            Vocabulary.from_file('')

    def test_junk_path(self):
        with self.assertRaises(FileNotFoundError):
            Vocabulary.from_file('/stuff.json')

    def test_json_return(self):
        with open(os.path.abspath(path)) as f:
            data = json.load(f)
            representation = (data, data.keys())
            self.assertEqual(representation, Vocabulary.from_json(path))


class EpithetGeneratorTest(unittest.TestCase):
    def test_generate_epithet(self):
        self.assertIs(type(EpithetGenerator.generate_epithet(path)), str)

    def test_generate_epithet_sad(self):
        with self.assertRaises(KeyError):
            EpithetGenerator.generate_epithet("/this/is/not/a/path")
