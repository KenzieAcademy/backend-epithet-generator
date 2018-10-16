from sprint_b import app
from sprint_b.helpers import EpithetGenerator, Vocabulary


@app.route("/")
def generate_epithet():
    """Serves a randomly generated epithet"""
    return EpithetGenerator.generate_epithet("../../resources/data.json")


@app.route("/vocabulary")
def vocabulary():
    """Serves the vocabulary to create an epithet"""
    columns = Vocabulary.from_file("../../resources/data.json")
    column1 = "Column 1: {}".format(columns["Column 1"])
    column2 = "Column 2: {}".format(columns["Column 2"])
    column3 = "Column 3: {}".format(columns["Column 3"])
    return "{}<br/><br/>{}<br/><br/>{}".format(column1, column2, column3)


@app.route("/epithets/<int:num>")
def generate_epithets(num):
    string = ""
    for x in range(num):
        string += "{}<br/>".format(
            EpithetGenerator.generate_epithet("../../resources/data.json")
        )
    return string
