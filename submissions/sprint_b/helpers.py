import os
import json
import random


class FileManager:
    """Handle local file system I0."""

    @staticmethod
    def get_extension(path):
        """Get file extension from path."""
        return os.path.splitext(path)[-1][1:]

    @staticmethod
    def read_json(path, mode='r', *args, **kwargs):
        with open(path, mode=mode, *args, **kwargs) as handle:
            return json.load(handle)


class Vocabulary:
    """Standardize vocabulary representation from multiple sources."""

    files = FileManager()

    @classmethod
    def from_file(cls, path, *args, **kwargs):
        extension = cls.files.get_extension(path)
        representation = cls.strategies(extension)(path, *args, **kwargs)
        return representation

    @classmethod
    def from_json(cls, path, fields=True, *args, **kwargs):
        data = cls.files.read_json(path, *args, **kwargs)
        if fields:
            representation = (data, data.keys())
        else:
            representation = data
        return representation

    @classmethod
    def strategies(cls, file_extension, intent='read'):
        input_strategies = {'json': cls.from_json}
        if intent is 'read':
            return input_strategies[file_extension]


class EpithetGenerator:
    """Generate an epithet."""

    @classmethod
    def select_random_words(cls, file_contents):
        word1 = file_contents['Column 1'][random.randint(0, 59)]
        word2 = file_contents['Column 2'][random.randint(0, 59)]
        word3 = file_contents['Column 3'][random.randint(0, 59)]
        return [word1, word2, word3]

    @classmethod
    def generate_epithets(cls, vocabulary_file):
        global FileManager
        file_contents = FileManager.read_json(vocabulary_file)
        words = cls.select_random_words(file_contents)
        response = 'Thou {} {} {}.'.format(words[0], words[1], words[2])
        return response
