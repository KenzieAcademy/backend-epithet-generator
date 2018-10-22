from helpers import FileManager, Vocabulary
import os


def test_FileManager_get_extension():
    path = "../../resources/data.json"
    assert FileManager.get_extension(path) == "json"


def test_FileManager_read_json():
    path = "../../resources/data.json"
    assert FileManager.read_json(os.path.abspath(path))


def test_Vocabulary_from_json():
    path = "../../resources/data.json"
    assert Vocabulary.from_json(path)


def test_Vocabulary_from_file():
    path = "../../resources/data.json"
    assert Vocabulary.from_file(path)


def test_Vocabulary_strategies():
    file_extension = 'json'
    assert Vocabulary.strategies(file_extension)