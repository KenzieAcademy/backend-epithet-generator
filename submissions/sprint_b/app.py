from . import app, jsonify
from helpers import EpithetGenerator
from helpers import Vocabulary


@app.route('/')
def generate_epithets():
    word_one, word_two, word_three = EpithetGenerator.epithet()
    epithet = "Thou {} {} {}!".format(word_one, word_two, word_three)
    response = {"epithets": epithet}
    return jsonify(response)


@app.route('/vocabulary')
def vocabulary():
    data = Vocabulary.from_file(
            "/Users/berg/projects/Kenzie/flask/backend-epithet-generator/resources/data.json"
            )
    response = {"vocabulary": data}
    return jsonify(response)
