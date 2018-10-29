from intitialize import app, jsonify
from helpers import EpithetGenerator
from helpers import Vocabulary
import random


@app.route('/')
def generate_epithets():
    word_one, word_two, word_three = EpithetGenerator.epithet()
    epithet = "Thou {} {} {}!".format(word_one, word_two, word_three)
    response = {"epithets": epithet}
    return jsonify(response)


@app.route('/epithet/<amount>')
def generate_epithet_by_amount(amount):
    word_one, word_two, word_three = EpithetGenerator.epithet()
    epithets = {}
    for i in range(int(amount)):
        word_one, word_two, word_three = EpithetGenerator.epithet()
        epithet = "Thou {} {} {}!".format(word_one, word_two, word_three)
        epithets[i+1] = epithet
    return jsonify(epithets)


@app.route('/epithet/random')
def generate_epithet_random():
    word_one, word_two, word_three = EpithetGenerator.epithet()
    epithets = {}
    for i in range(random.randrange(20)):
        word_one, word_two, word_three = EpithetGenerator.epithet()
        epithet = "Thou {} {} {}!".format(word_one, word_two, word_three)
        epithets[i+1] = epithet
    return jsonify(epithets)


@app.route('/vocabulary')
def vocabulary():
    data = Vocabulary.from_file(
            "/Users/berg/projects/Kenzie/flask/backend-epithet-generator/resources/data.json"
            )
    response = {"vocabulary": data}
    return jsonify(response)