import os
import json
import random

class FileManager:
    """Handle local file system IO."""

    @staticmethod
    def get_extension(path):
        """Get file extension from file path."""
        return os.path.splitext(path)[-1][1:]

    @staticmethod
    def read_json(path, mode='r', *args, **kwargs):
        """Open a file and turn JSON data into Python objects"""
        with open(path, mode=mode, *args, **kwargs) as handle:
            return json.load(handle)


class Vocabulary:
    """Standardize vocabulary representation from multiple sources."""

    files = FileManager()

    @classmethod
    def from_file(cls, path, *args, **kwargs):
        """Returns data in a proper format to allow easier extraction"""
        extension = cls.files.get_extension(path)
        representation = cls.strategies(extension)(path, *args, **kwargs)
        return representation

    @classmethod
    def from_json(cls, path, fields=True, *args, **kwargs):
        """Reads data from a json file and returns it as a python object"""
        data = cls.files.read_json(path, *args, **kwargs)
        if fields:
            representation = (data, data.keys())
        else:
            representation = data
        return representation

    @classmethod
    def strategies(cls, file_extension, intent='read'):
        """Determines whether a file is a json file to appropriate handle it"""
        input_strategies = {'json': cls.from_json}
        if intent is 'read':
            return input_strategies[file_extension]


class EpithetGenerator:
    
    @classmethod
    def random_word(cls):
        """Chooses three random words from three lists in a json file"""
        path_name = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', '..', 'resources', 'data.json'))

        representation = Vocabulary().from_file(path_name)
        column1_random = random.choice(representation[0]['Column 1'])
        column2_random = random.choice(representation[0]['Column 2'])
        column3_random = random.choice(representation[0]['Column 3'])

        random_words = [column1_random, column2_random, column3_random]
        return random_words
    
    @classmethod
    def generate_epithets(cls):
        """Formats the three random chosen words into the proper string"""
        random_word_lst = cls.random_word()
        final_string = "Thou {insult1} {insult2} {insult3}".format(
                                                                   insult1=random_word_lst[0], 
                                                                   insult2=random_word_lst[1], 
                                                                   insult3=random_word_lst[2]
                                                                  )
        return final_string