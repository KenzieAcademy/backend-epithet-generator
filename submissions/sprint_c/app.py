from . import app
from .helpers import EpithetGenerator
from flask import jsonify

data_path = '../../resources/data.json'


@app.route('/')
def generate_epithets():
    return jsonify(EpithetGenerator.serve_insult(data_path))


@app.route('/vocabulary')
def vocabulary():
    return jsonify(EpithetGenerator.serve_vocab(data_path))


@app.route('/random')
def random():
    return jsonify(EpithetGenerator.serve_random(data_path))
