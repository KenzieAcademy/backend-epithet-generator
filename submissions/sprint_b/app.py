from . import app
from flask import jsonify
from helpers import EpithetGenerator
from helpers import Vocabulary
import os
RESOURCES = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
JSON = os.path.join(RESOURCES, "./resources/data.json")

@app.route('/')
def generate_epithets():
    generator = EpithetGenerator()
    epithet = generator.get_one()
    return jsonify(epithet)


@app.route('/<quantity>')
def generate_epithet_by_quantity(quantity):
    generator = EpithetGenerator()
    epithets = generator.get_by_amount(quantity)
    return jsonify(epithets)


@app.route('/vocabulary')
def vocabulary():
    data = Vocabulary.from_file(JSON)
    return jsonify(data)