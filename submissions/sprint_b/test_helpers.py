import unittest
from helpers import FileManager, Vocabulary, EpithetGenerator

test_path = ('/Users/ethansternke/Documents/Kenzie/back-end'
             '/backend-epithet-generator/resources/test.json')

test_vocab = (
    {
        'Column 2': ['word2'],
        'Column 3': ['word3'],
        'Column 1': ['word1']
    },
    [
        'Column 2',
        'Column 3',
        'Column 1'
    ]
)


class TestFileManager(unittest.TestCase):
    def test_get_extension(self):
        self.assertEqual(FileManager.get_extension(test_path), 'json')

    def test_read_json(self):
        self.assertEqual(FileManager.read_json(test_path), {
            'Column 2': ['word2'],
            'Column 3': ['word3'],
            'Column 1': ['word1']
        })


class TestVocabulary(unittest.TestCase):
    def test_from_file(self):
        self.assertEqual(Vocabulary.from_file(test_path), test_vocab)

    def test_from_json(self):
        self.assertEqual(Vocabulary.from_json(test_path), test_vocab)

    def test_strategies(self):
        self.assertTrue(Vocabulary.strategies('json'))


class TestEpithetGenerator(unittest.TestCase):
    def test_select_random_words(self):
        e = EpithetGenerator()
        self.assertEqual(e.select_random_words(
            test_vocab), ['word1', 'word2', 'word3'])

    def test_generate_epithet(self):
        e = EpithetGenerator()
        self.assertEqual(e.generate_epithet(test_path),
                         'Thou word1 word2 word3.')


if __name__ == '__main__':
    unittest.main()
