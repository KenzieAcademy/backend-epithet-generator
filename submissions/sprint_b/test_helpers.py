import unittest
import shutil
import os
import json

from .helpers import FileManager, Vocabulary, EpithetGenerator


class Epithet_tests(unittest.TestCase):

    path = 'fake/fake_file.json'

    def setUp(self):
        data = {
            "Column 1": ["bar"],
            "Column 2": ["foo"],
            "Column 3": ["baz"]
        }
        if os.path.isdir('fake'):
            shutil.rmtree('fake')
            os.mkdir('./fake')
            with open(self.path, 'w') as test_file:
                json.dump(data, test_file)
        else:
            os.mkdir('./fake')
            with open(self.path, 'w') as test_file:
                json.dump(data, test_file)

    def tearDown(self):
        shutil.rmtree('./fake')

    def test_get_extension(self):
        self.assertEqual(FileManager.get_extension(self.path), 'json')

    def test_read_json(self):
        self.assertEqual(FileManager.read_json(self.path), {
            "Column 1": ["bar"],
            "Column 2": ["foo"],
            "Column 3": ["baz"]
        })

    def test_from_file(self):
        self.assertEqual(Vocabulary.from_file(self.path, fields=False), {
            "Column 1": ["bar"],
            "Column 2": ["foo"],
            "Column 3": ["baz"]
        })

    def test_serve_insult(self):
        self.assertEqual(EpithetGenerator.serve_insult(self.path),
                         'bar foo baz')

    def test_serve_vocab(self):
        self.assertEqual(EpithetGenerator.serve_vocab(self.path),
                         'bar, foo, baz')
