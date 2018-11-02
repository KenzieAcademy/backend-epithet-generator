from flask import jsonify
import random

from sprint_c import app
from sprint_c.helpers import EpithetGenerator
from sprint_c.helpers import Vocabulary

path = ('/Users/aj/Documents/Back-End/backend-epithet-generator/resources/data.json')
path2 = ('/Users/aj/Documents/Back-End/backend-epithet-generator/resources/data.csv')


@app.route('/')
def generate_epithets():
    epithet = EpithetGenerator.get_epithet(path)
    response = {'epithet': epithet}
    return jsonify(response)


@app.route('/vocabulary')
def vocabulary():
    response = Vocabulary.from_file(path2)
    return jsonify(response)


@app.route('/epithets/<int:amount>')
def amount(amount):
    response = EpithetGenerator.get_epithets(path, amount)
    return jsonify(response)


@app.route('/epithets/random')
def random_epithets():
    amount = random.randint(1, 10)
    response = EpithetGenerator.get_epithets(path, amount)
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=False)
