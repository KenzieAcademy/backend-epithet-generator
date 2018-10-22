from sprint_b.helpers import FileManager, Vocabulary, EpithetGenerator
import os

path = "../../resources/data.json"

def test_get_extension():
    global path
    assert FileManager.get_extension(path) == "json"