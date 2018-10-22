from helpers import FileManager, Vocabulary, EpithetGenerator
import os

path = os.getenv("VOCAB_FILE_PATH")


def test_FileManager_get_extension():
    assert FileManager.get_extension(path) == "json"


def test_FileManager_read_json():
    assert FileManager.read_json(os.path.abspath(path))


def test_Vocabulary_from_json():
    assert Vocabulary.from_json(path)


def test_Vocabulary_from_file():
    assert Vocabulary.from_file(path)


def test_Vocabulary_strategies():
    file_extension = 'json'
    assert Vocabulary.strategies(file_extension)


def test_EpithetGenerator_generate_epithet():
    assert type(EpithetGenerator.generate_epithet(path)) is str
