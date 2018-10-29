import random

from flask import abort

from initialize import app, jsonify
from helpers import EpithetGenerator, Vocabulary


@app.route('/')
def generate_epithet():
    epithet = EpithetGenerator.generate_epithet()
    return jsonify({"epithet": epithet})


@app.route('/epithets/<quantity>')
def generate_epithets_quantity(quantity):
    if quantity.isnumeric():
        quantity = int(quantity)
    else:
        abort(400, 'Quantity parameter must be an integer, friend.')
    epithets = []
    for n in range(quantity):
        epithets.append(EpithetGenerator.generate_epithet())
    return jsonify({"epithets": epithets})


@app.route('/epithets/random')
def generate_epithets_quantity_random():
    random_num = random.randint(1, 100)
    random_epithets = []
    for n in range(random_num):
        random_epithets.append(EpithetGenerator.generate_epithet())
    return jsonify({"random_epithets": random_epithets})


@app.route('/vocabulary')
def vocabulary():
    vocab = Vocabulary().from_file('../../resources/data.json', fields=False)
    return jsonify({"vocabulary": vocab})


if __name__ == "__main__":
    app.run()
