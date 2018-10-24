import os
import random

from sprint_c import app
from sprint_c.helpers import EpithetGenerator, Vocabulary

VOCAB_FILE_PATH = os.getenv("VOCAB_FILE_PATH")


@app.route("/")
def generate_epithet():
    """Serves a randomly generated epithet."""
    return EpithetGenerator.generate_epithet(VOCAB_FILE_PATH)


@app.route("/vocabulary")
def vocabulary():
    """Serves the vocabulary to create an epithet."""
    columns = Vocabulary.from_file(VOCAB_FILE_PATH)
    column1 = "Column 1: {}".format(columns["Column 1"])
    column2 = "Column 2: {}".format(columns["Column 2"])
    column3 = "Column 3: {}".format(columns["Column 3"])
    return "{}<br/><br/>{}<br/><br/>{}".format(column1, column2, column3)


@app.route("/epithets/<int:num>")
def generate_epithets(num):
    """Generates a number of epithers that are specified."""
    string = ""
    for x in range(num):
        string += "{}<br/>".format(
            EpithetGenerator.generate_epithet(VOCAB_FILE_PATH)
        )
    return string


@app.route("/epithets/random")
def random_epithets():
    """Generates a random number of epithets."""
    string = ""
    num = random.randint(1, 10)
    for x in range(num):
        string += "{}<br/>".format(
            EpithetGenerator.generate_epithet(VOCAB_FILE_PATH)
        )
    return string
