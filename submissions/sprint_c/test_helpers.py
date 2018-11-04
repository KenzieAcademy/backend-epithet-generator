from helpers import FileManager, Vocabulary, EpithetGenerator
import os
import json
import pytest
import app

@pytest.fixture(scope='module')
def test_client():
    app.app.config['TESTING'] = True
    client = app.app.test_client()

    yield client

def test_get_todos(test_client):
    response = test_client.get('/')
    json_to_object_response = json.loads(response.data)['epithets']
    object_response_split = json_to_object_response.split(' ')
    assert len(object_response_split) == 4
    assert response.status_code == 200

def test_random_epithet(test_client):
    response = test_client.get('/random')
    num_of_epithets = json.loads(response.data)['random_int']
    list_of_random_epith = json.loads(response.data)['insult_list']
    assert len(list_of_random_epith) == num_of_epithets
    assert response.status_code == 200

def test_file_manager():
    file_manager = FileManager()
    file_extension = file_manager.get_extension("../resources/data.json")
    
    assert file_extension == "json"


def test_read_json():
    file_manager = FileManager()
    # Refactor
    path_name = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', '..', 'resources', 'data.json'))
    with open(path_name, mode='r') as handle:
        open_json_load = json.load(handle)
    read_json = file_manager.read_json(path_name)
    assert open_json_load == read_json


def test_strategies():
    vocab = Vocabulary()
    vocab_strategies = vocab.strategies('json')
    assert vocab_strategies == vocab.from_json


def test_vocab_from_file():
    vocab = Vocabulary()
    path_name = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', '..', 'resources', 'data.json'))

    repr_from_file = vocab.from_file(path_name)
    repr_from_file_keys = repr_from_file[0].keys()
    assert len(repr_from_file_keys) == 3



def test_vocab_from_json():
    vocab = Vocabulary()
    file_manager = FileManager()

    path_name = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', '..', 'resources', 'data.json'))
    with open(path_name, mode='r') as handle:
        open_json_load = json.load(handle)
    read_json = file_manager.read_json(path_name)

    assert read_json == open_json_load

def test_generator_random_word():
    epithet_generator = EpithetGenerator()
    random_words = epithet_generator.random_word()

    assert len(random_words) == 3

def test_generate_epithets():
    epithet_generator = EpithetGenerator()
    generated_epithets = epithet_generator.generate_epithets()
    split_epithet = generated_epithets.split(' ')
    
    assert len(split_epithet) == 4




    

