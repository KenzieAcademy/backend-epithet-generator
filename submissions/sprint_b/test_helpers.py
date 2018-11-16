"""
This module serves to test methods for each class in helpers.py.
"""
import unittest
import json

from helpers import FileManager, Vocabulary, EpithetGenerator

happy_path = '../../resources/data.json'
sad_path = '../../resources/foo.bar'
csv_path = '../../resources/data.csv'
fake_path = '../../fake.json'
dir_path = '../../resources/'
with open(happy_path, 'r') as f:
    data = json.loads(f.read())


class TestFileMangager(unittest.TestCase):
    """
    This class contains all logic for testing the FileManager class
    and its methods.
    """

    def test_get_extension_json(self):
        """
        This test confirms that passing in a happy path will
        return the appropriate file extension.
        """
        self.assertEqual(
            FileManager.get_extension(happy_path), 'json'
        )

    def test_get_extension_csv(self):
        """
        This test confirms that passing in a csv path will
        return the appropriate file extension.
        """
        self.assertEqual(
            FileManager.get_extension(csv_path), 'csv'
        )

    def test_get_extension_dir(self):
        """
        This test confirms that passing in a path without a file extension will
        return an empty string.
        """
        self.assertEqual(
            FileManager.get_extension(dir_path), ''
        )
        with self.assertRaises(TypeError):
            FileManager.get_extension(1)

    def test_read_json_happypath(self):
        """
        This test confirms that passing in a happy path will
        return approprately formatted data.
        """
        self.assertEqual(
            FileManager.read_json(happy_path), data
        )

    def test_read_json_sadpath(self):
        """
        This test confirms that passing in a sad path will
        raise an expected error.
        """
        with self.assertRaises(FileNotFoundError):
            FileManager.read_json(sad_path)


class TestVocabulary(unittest.TestCase):
    """
    This class contains all logic for testing the Vocabulary class
    and its methods.
    """

    def test_from_file_happypath(self):
        """
        This function tests to confirm that passing in a happy path to the
        from_file method will result in approprately formatted data.
        """
        self.assertEqual(
            Vocabulary.from_file(happy_path, fields=False), data
        )

    def test_from_file_sadpath(self):
        """
        This function tests to confirm passing in a sad path will result in
        an expected error.
        """
        with self.assertRaises(KeyError):
            Vocabulary.from_file(sad_path)

    def test_from_json_happypath(self):
        """
        This function tests to confirm that passing in a happy path to the
        from_json method will result in approprately formatted data.
        """
        self.assertEqual(
            Vocabulary.from_json(happy_path, fields=False), data
        )

    def test_from_json_sadpath(self):
        """
        This function tests to confirm that passing in a sad path
        will result in an expected error.
        """
        with self.assertRaises(FileNotFoundError):
            Vocabulary.from_json(sad_path, fields=False)

    def test_strategies_happy(self):
        """
        This function tests to confirm that passing in a happy path to the
        strategies method will result in approprately formatted data.
        """
        self.assertEqual(Vocabulary.strategies('json'), Vocabulary.from_json)

    def test_strategies_sad(self):
        """
        This function tests to confirm that passing in a unexpected value
        will result in an expected error.
        """
        with self.assertRaises(KeyError):
            Vocabulary.strategies('foo')


class TestEpithetGenerator(unittest.TestCase):
    """
    This class contains all logic for testing the EpithetGenerator class 
    and its methods.
    """

    def test_select_random_word_from_each_column_c1(self):
        """
        This function tests to confirm the first random word is from
        the JSON data's first column.
        """
        self.assertIn(
            EpithetGenerator.select_random_word_from_each_column()[0],
            data['Column 1']
        )

    def test_select_random_word_from_each_column_c2(self):
        """
        This function tests to confirm the second random word is from
        the JSON data's second column.
        """
        self.assertIn(
            EpithetGenerator.select_random_word_from_each_column()[1],
            data['Column 2']
        )

    def test_select_random_word_from_each_column_c3(self):
        """
        This function tests to confirm the third random word is from
        the JSON data's third column.
        """
        self.assertIn(
            EpithetGenerator.select_random_word_from_each_column()[2],
            data['Column 3']
        )

    def test_select_random_word_from_each_column_fakepath(self):
        """
        This function tests for the expected error message when
        passing in a fake path.
        """
        with self.assertRaises(FileNotFoundError):
            EpithetGenerator.select_random_word_from_each_column(
                file_path=fake_path)

    def test_select_random_word_from_each_column_sadpath(self):
        """
        This function tests for the expected error message when
        passing in a sad path.
        """
        with self.assertRaises(KeyError):
            EpithetGenerator.select_random_word_from_each_column(
                file_path=sad_path)

    def test_select_random_word_from_each_column_csvpath(self):
        """
        This function tests for the expected error message when
        passing in a csv path.
        """
        with self.assertRaises(KeyError):
            EpithetGenerator.select_random_word_from_each_column(
                file_path=csv_path)

    def test_generate_epithet_zeroidx(self):
        """
        This function tests to see if the string at the zero index matches
        what is expected of the epithet sentence format.
        """
        test_list = EpithetGenerator.generate_epithet()[0].split(' ')
        self.assertEqual(test_list[0], 'Thou')

    def test_generate_epithet_oneidx(self):
        """
        This function tests to see if the string at the one index matches
        what is expected of the epithet sentence format.
        """
        test_list = EpithetGenerator.generate_epithet()[0].split(' ')
        self.assertIn(test_list[1], data['Column 1'])

    def test_generate_epithet_twoidx(self):
        """
        This function tests to see if the string at the two index matches
        what is expected of the epithet sentence format.
        """
        test_list = EpithetGenerator.generate_epithet()[0].split(' ')
        self.assertIn(test_list[2], data['Column 2'])

    def test_generate_epithet_threeidx(self):
        """
        This function tests to see if the string at the three index matches
        what is expected of the epithet sentence format.
        """
        test_list = EpithetGenerator.generate_epithet()[0].split(' ')
        self.assertIn(test_list[3], data['Column 3'])

    def test_generate_epithet_fakepath(self):
        """
        This function tests for the error message when passing in
        a fake file path.
        """
        with self.assertRaises(FileNotFoundError):
            EpithetGenerator.generate_epithet(file_path=fake_path)

    def test_generate_epithet_sadpath(self):
        """
        This function tests for the error message when passing in
        a sad file path.
        """
        with self.assertRaises(KeyError):
            EpithetGenerator.generate_epithet(file_path=sad_path)

    def test_generate_epithet_csv_path(self):
        """
        This function tests for the error message when passing in
        a csv file path.
        """
        with self.assertRaises(KeyError):
            EpithetGenerator.generate_epithet(file_path=csv_path)


if __name__ == '__main__':
    unittest.main()
