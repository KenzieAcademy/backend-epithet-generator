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
        """deserialize a file containing JSON to a python object"""
        try:    
            with open(path, mode=mode, *args, **kwargs) as handle:
                return json.load(handle)
        except FileNotFoundError as e:
            return e

class Vocabulary:
    """Standardize vocabulary representation from multiple sources."""

    files = FileManager()

    @classmethod
    def from_file(cls, path, *args, **kwargs):
        """ gives us a representaion of the file we want to look at """
        extension = cls.files.get_extension(path)
        representation = cls.strategies(extension)(path, *args, **kwargs)
        return representation

    @classmethod
    def from_json(cls, path, fields=True, *args, **kwargs):
        """ Takes a JSON file and returns the vocab dictionary and it's keys in the form of a tuple. """
        data = cls.files.read_json(path, *args, **kwargs)
        if fields:
            try:
                representation = (data, data.keys())
            except Exception as e:
                return e
        else:
            representation = data
        return representation

    @classmethod
    def strategies(cls, file_extension, intent='read'):
        """ Handles other file types and turns them into json """   
        input_strategies = {'json': cls.from_json}
        if intent is 'read':
            return input_strategies[file_extension]

class EpithetGenerator:
    global vocab
    """
        Takes data from resources folder and builds a full epithet based on a random choice of words in each column.
    """ 
    @staticmethod
    def get_rand(path):
        try:
            vocab = Vocabulary.from_file(path)
            return "Thou {} {} {}".format(
                random.choice(vocab[0]["Column 1"]),
                random.choice(vocab[0]["Column 2"]),
                random.choice(vocab[0]["Column 3"])
            )
        except Exception as e:
            return e