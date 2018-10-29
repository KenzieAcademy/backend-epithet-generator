import random

from initialize import app, jsonify
from helpers import EpithetGenerator, Vocabulary


@app.route('/')
def generate_epithet():
    epithet = EpithetGenerator.generate_epithet()
    return jsonify({"epithet": epithet})


@app.route('/epithets/<quantity>')
def generate_epithets(quantity):
    quantity = int(quantity)
    epithets = []
    for n in range(quantity):
        epithets.append(EpithetGenerator.generate_epithet())
    return jsonify({"epithets": epithets})


@app.route('/vocabulary')
def vocabulary():
    vocab = Vocabulary().from_file('../../resources/data.json', fields=False)
    return jsonify({"vocabulary": vocab})


@app.route('/random')
def random_num_epithets():
    random_num = random.randint(1, 100)
    random_epithets = []
    for n in range(random_num):
        random_epithets.append(EpithetGenerator.generate_epithet())
    return jsonify({"random_epithets": random_epithets})


if __name__ == "__main__":
    app.run()
