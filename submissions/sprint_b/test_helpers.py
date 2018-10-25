import unittest
import json

from helpers import FileManager, Vocabulary, EpithetGenerator

happy_path = '../../resources/data.json'
sad_path = '../../resources/foo.bar'
csv_path = '../../resources/data.csv'
fake_path = '../../fake.json'
with open(happy_path, 'r') as f:
    data = json.loads(f.read())


class TestFileMangager(unittest.TestCase):

    def test_get_extension(self):
        self.assertEqual(
            FileManager.get_extension(happy_path), 'json'
        )
        self.assertEqual(
            FileManager.get_extension(csv_path), 'csv'
        )
        self.assertEqual(
            FileManager.get_extension('test/testo/westo/'), ''
        )
        with self.assertRaises(TypeError):
            FileManager.get_extension(1)

    def test_read_json(self):

        self.assertEqual(
            FileManager.read_json(happy_path), data
        )

        with self.assertRaises(FileNotFoundError):
            FileManager.read_json(sad_path)


class TestVocabulary(unittest.TestCase):

    def test_from_file(self):
        self.assertEqual(
            Vocabulary.from_file(happy_path, fields=False), data
        )
        with self.assertRaises(KeyError):
            Vocabulary.from_file(sad_path)

    def test_from_json(self):
        self.assertEqual(
            Vocabulary.from_json(happy_path, fields=False), data
        )
        with self.assertRaises(FileNotFoundError):
            Vocabulary.from_json(sad_path, fields=False)

    def test_strategies(self):
        self.assertEqual(Vocabulary.strategies('json'), Vocabulary.from_json)
        with self.assertRaises(KeyError):
            Vocabulary.strategies('foo')


class TestEpithetGenerator(unittest.TestCase):

    def test_select_random_word_from_each_column(self):
        self.assertIn(
            EpithetGenerator.select_random_word_from_each_column()[0],
            data['Column 1']
        )
        self.assertIn(
            EpithetGenerator.select_random_word_from_each_column()[1],
            data['Column 2']
        )
        self.assertIn(
            EpithetGenerator.select_random_word_from_each_column()[2],
            data['Column 3']
        )

        with self.assertRaises(FileNotFoundError):
            EpithetGenerator.select_random_word_from_each_column(
                file_path=fake_path)
        with self.assertRaises(KeyError):
            EpithetGenerator.select_random_word_from_each_column(
                file_path=sad_path)
        with self.assertRaises(KeyError):
            EpithetGenerator.select_random_word_from_each_column(
                file_path=csv_path)

    def test_generate_epithet(self):
        test_list = EpithetGenerator.generate_epithet().split(' ')
        self.assertEqual(test_list[0], 'Thou')
        self.assertIn(test_list[1], data['Column 1'])
        self.assertIn(test_list[2], data['Column 2'])
        self.assertIn(test_list[3], data['Column 3'])

        with self.assertRaises(FileNotFoundError):
            EpithetGenerator.generate_epithet(file_path=fake_path)
        with self.assertRaises(KeyError):
            EpithetGenerator.generate_epithet(file_path=sad_path)
        with self.assertRaises(KeyError):
            EpithetGenerator.generate_epithet(file_path=csv_path)


if __name__ == '__main__':
    unittest.main()
