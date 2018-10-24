import json
import os
import random


class FileManager:
    """Handle local file system IO."""

    @staticmethod
    def get_extension(path):
        """Get file extension from file path."""
        return os.path.splitext(path)[-1][1:]

    @staticmethod
    def read_json(path, mode='r', *args, **kwargs):
        """opens and returns data from file as json"""
        with open(path, mode=mode, *args, **kwargs) as handle:
            return json.load(handle)


class Vocabulary:
    """Standardize vocabulary representation from multiple sources."""

    files = FileManager()

    @classmethod
    def from_file(cls, path, *args, **kwargs):
        """Runs the get_extension method from FileManager
        and then runs the class method within Vocabulary
        based on the extension type"""
        extension = cls.files.get_extension(path)
        representation = cls.strategies(extension)(path, *args, **kwargs)
        return representation

    @classmethod
    def from_json(cls, path, fields=True, *args, **kwargs):
        """Reads the json file passed to it from the read_json method.
        It then returns the data or data and data.keys()
        based on if fields arg is true or false"""
        data = cls.files.read_json(path, *args, **kwargs)
        if fields:
            representation = (data, data.keys())
        else:
            representation = data
        return representation

    @classmethod
    def strategies(cls, file_extension, intent='read'):
        """Identifies the extension type passed to it and runs a class method
        based on the extension type.  Currently only json is supported."""
        input_strategies = {'json': cls.from_json}
        if intent is 'read':
            return input_strategies[file_extension]


class EpithetGenerator:
    """Generates a randomly selected epithet from a vocabulary list"""
    def serve_insult(path):
        """Reads a data file of insult words.
        A random word is chosen from each column
        and then concatenated."""
        insult_dict = Vocabulary.from_file(path, fields=False)
        random_insult = (random.choice(insult_dict['Column 1']) + ' '
                         + random.choice(insult_dict['Column 2']) + ' '
                         + random.choice(insult_dict['Column 3']))
        return random_insult

    def serve_vocab(path):
        """Reads a data file of insult words.
        All words are then joined on ',' and returned"""
        insult_dict = Vocabulary.from_file(path, fields=False)
        full_vocab = (insult_dict['Column 1']
                      + insult_dict['Column 2']
                      + insult_dict['Column 3'])
        return ', '.join(full_vocab)
