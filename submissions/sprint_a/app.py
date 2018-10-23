from flask import jsonify

from sprint_a import app
from sprint_a.helpers import EpithetGenerator
from sprint_a.helpers import Vocabulary

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


if __name__ == '__main__':
    app.run(debug=False)
