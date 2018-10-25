from sprint_b import app
import json
from helpers import EpithetGenerator, Vocabulary
import random

path = ('/Users/ethansternke/Documents/Kenzie/back-end'
        '/backend-epithet-generator/resources/data.json')


@app.route('/')
def generate_epithet():
    e = EpithetGenerator()
    epithet = e.generate_epithet(path)
    response = {"epithet": epithet}
    return json.dumps(response)


@app.route('/vocabulary')
def vocabulary():
    v = Vocabulary()
    vocabulary = v.from_file(path)
    response = {"vocabulary": vocabulary}
    return json.dumps(response)


@app.route('/epithets')
def generate_random_epithets():
    e = EpithetGenerator()
    quantity = random.randint(1, 100)
    epithets = e.generate_epithets(quantity, path)
    response = {"epithets": epithets}
    return json.dumps(response)


@app.route('/epithets/<quantity>')
def generate_x_epithets(quantity):
    e = EpithetGenerator()
    epithets = e.generate_epithets(quantity, path)
    response = {"epithets": epithets}
    return json.dumps(response)


if __name__ == '__main__':
    app.run(debug=True)
