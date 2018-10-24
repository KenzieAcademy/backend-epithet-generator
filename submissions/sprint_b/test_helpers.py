from sprint_b.helpers import FileManager, Vocabulary, EpithetGenerator
from flask import json
import os
import json
import shutil

"""     use pytest      """

path = "../../resources/data.json"
sad_path = ".fake./.path./resources123/data321.json"

with open(os.path.abspath(path)) as json_data:
    data = json.load(json_data)

def test_get_extension():
    assert FileManager.get_extension(path) == "json"


def test_read_json():
    assert FileManager.read_json(path) == data


def test_from_file():
    assert Vocabulary.from_file(path) == (data, data.keys())


def test_from_json():
    assert Vocabulary.from_json(path) == (data, data.keys())


def test_strategies():
    assert Vocabulary.strategies("json") == Vocabulary.from_json

def test_happy_path():
    """Tests that the first word in the generated epithet is Thou,
        the second word is in the first json column,
        the third word is in the second json column,
        and the last word is in the last json column
    """

    rand_epithet = EpithetGenerator.get_rand(path)

    #same dict used to generate epithets
    vocab = Vocabulary.from_file(path)

    #split up each word in the epithet generated
    split_epithet = rand_epithet.split()

    #pop off the 'Thou'
    split_epithet.pop(0)

    #split up dict to compare first column with first word and so on 
    first_col = vocab[0]["Column 1"]
    second_col = vocab[0]["Column 2"]
    third_col = vocab[0]["Column 3"]

    for word in first_col:
        if word in split_epithet[0]:
            word1 = word
    
    for word in second_col:
        if word in split_epithet[1]:
            word2 = word

    for word in third_col:
        if word in split_epithet[2]:
            word3 = word

    assert rand_epithet == "Thou {} {} {}".format(
        word1, word2, word3
    )


def test_sad_path():
    try:
        EpithetGenerator.get_rand(sad_path)
    except Exception as e:
        assert e == FileNotFoundError(2, 'No such file or directory')

