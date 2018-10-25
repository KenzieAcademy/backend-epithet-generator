from sprint_b import app, jsonify
from sprint_b.helpers import EpithetGenerator, Vocabulary


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
