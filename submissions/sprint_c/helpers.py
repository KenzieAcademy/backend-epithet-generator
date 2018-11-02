import json
import os
import random
import csv


class FileManager:
    """Handle local file system IO."""

    @staticmethod
    def get_extension(path):
        """Get file extension from file path."""
        return os.path.splitext(path)[-1][1:]

    @staticmethod
    def read_json(path, mode='r', *args, **kwargs):
        """Reads the file and returns its contents."""
        with open(path, mode=mode, *args, **kwargs) as handle:
            return json.load(handle)


class Vocabulary:
    """Standardize vocabulary representation from multiple sources."""

    files = FileManager()

    @classmethod
    def from_file(cls, path, *args, **kwargs):
        """Takes a path determines its extension and returns the files data"""
        extension = cls.files.get_extension(path)
        if extension == 'csv':
            representation = cls.csv_reader(path)
        else:
            representation = cls.strategies(extension)(path, *args, **kwargs)
        return representation

    @classmethod
    def from_json(cls, path, fields=True, *args, **kwargs):
        """Takes a path and returns the files data"""
        data = cls.files.read_json(path, *args, **kwargs)
        return data

    @classmethod
    def strategies(cls, file_extension, intent='read'):
        """Takes a json file and returns an object"""
        input_strategies = {'json': cls.from_json}
        if intent is 'read':
            return input_strategies[file_extension]

    @classmethod
    def csv_reader(cls, path):
        """Takes the given path and returns the CSV data"""
        csvfile = open(path, 'r')
        words = csv.reader(csvfile, delimiter=',')
        vocabulary = {'vocabulary': []}
        line = 0
        for row in words:
            if line == 0:
                line += 1
                continue
            else:
                vocabulary['vocabulary'].extend(row)

        vocabulary['vocabulary'] = [v for v in vocabulary['vocabulary'] if v != '']
        return vocabulary


class EpithetGenerator:
    path = """
       /Users/aj/Documents/Back-End/backend-epithet-generator/resources/data.json
        """

    @classmethod
    def random_words(cls, path):
        """Generators a list of 3 random words, one from each column"""
        data = Vocabulary.from_file(path)
        vocabulary = [random.choice(data[col]) for col in data]
        return(vocabulary)

    @classmethod
    def get_epithet(cls, path):
        """Returns one epithet"""
        words = cls.random_words(path)
        epithet = "Thou %s %s %s!!" % (words[0], words[1], words[2])
        return epithet

    @classmethod
    def get_epithets(cls, path, amount):
        """Returns multiple epithets based on the amount given"""
        epithets = []
        for i in range(amount):
            eg = EpithetGenerator()
            epithets.append(eg.get_epithet(path))
        response = {'epithet': epithets}
        return response
