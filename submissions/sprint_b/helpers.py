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

    def select_random_words(self, vocab):
        vocab[1].sort()
        return [random.choice(vocab[0][vocab[1][col]]) for col in range(3)]

    def generate_epithet(self, vocabulary_file):
        vocab = Vocabulary.from_json(vocabulary_file)
        words = self.select_random_words(vocab)
        return 'Thou {} {} {}.'.format(words[0], words[1], words[2])
