from Flask import jsonify

from sprint_b import app
from sprint_b.helpers import EpithetGenerator, Vocabulary


@app.route('/')
def generate_epithet():
    epithet = EpithetGenerator.generate_epithet()
    return jsonify({"epithet": epithet})


@app.route('/epithets/<int:quantity>')
def generate_epithets(quantity):
    epithets = EpithetGenerator.generate_epithet(quantity=quantity)
    return jsonify({"epithets": epithets})


@app.route('/vocabulary')
def vocabulary():
    vocab = Vocabulary().from_file('../../resources/data.json', fields=False)
    return jsonify({"vocabulary": vocab})
