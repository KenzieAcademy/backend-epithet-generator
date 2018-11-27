from . import app
from flask import jsonify
from helpers import EpithetGenerator
from helpers import Vocabulary


@app.route('/')
def generate_epithets():
    epithet = EpithetGenerator().get_one()
    response = {"epithets": epithet}
    return jsonify(response)


@app.route('/epithets/<quantity>')
def generate_epithet_by_quantity(quantity):
    epithets = EpithetGenerator().get_by_amount(quantity)
    return jsonify(epithets)


@app.route('/vocabulary')
def vocabulary():
    data = Vocabulary.from_file(
            "/Users/berg/projects/Kenzie/flask/backend-epithet-generator/resources/data.json"
            )
    response = {"vocabulary": data}
    return jsonify(response)