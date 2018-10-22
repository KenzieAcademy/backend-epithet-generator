from . import app
from sprint_b.helpers import EpithetGenerator, Vocabulary, FileManager

@app.route('/')
def generate_epithet():
    return EpithetGenerator.get_rand("../../resources/data.json")

@app.route('/vocabulary')
def vocabulary():
    columns = Vocabulary.from_json("../../resources/data.json")
    column1 = "Column 1: {}".format(columns[0]["Column 1"])
    column2 = "Column 2: {}".format(columns[0]["Column 2"])
    column3 = "Column 3: {}".format(columns[0]["Column 3"])
    return "{}\n\n{}\n\n{}".format(column1, column2, column3)

@app.route('/amount/<int:num>')
def multiple_epithets(num):
    epithets = ""
    for n in range(num):
        epithets += "{}\n".format(generate_epithet())
    return epithets
