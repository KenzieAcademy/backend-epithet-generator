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
    """Select words from data file for epithet and generates epithet string"""
    
    vocab = Vocabulary()

    @classmethod
    def select_random_word_from_each_column(cls, file_path=None):
        if not file_path:
            data, keys = cls.vocab.from_file(
                '/Users/petermarsh/Projects/back_end/8_python_web_server/'
                'backend-epithet-generator/resources/data.json'
            )
        else:
            data, keys = cls.vocab.from_file(file_path)
        vocab_choices = [random.choice(data.get(key)) for key in keys]
        return vocab_choices

    @classmethod
    def generate_epithet(cls, file_path=None):
        my_str = 'Thou {} {} {}'
        if not file_path:
            return my_str.format(*cls.select_random_word_from_each_column())
        else:
            return my_str.format(
                *cls.select_random_word_from_each_column(file_path=file_path)
            )
