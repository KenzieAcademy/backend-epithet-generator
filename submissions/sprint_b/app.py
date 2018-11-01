from sprint_b import app
from sprint_b.helpers import epithet_generator
from flask import jsonify

@app.route('/<variable>')
def generate_epithets(variable):
    epithets = []
    for i in range(int(variable)):
        epithets.append(epithet_generator.epi_generator())
    return jsonify({"epithets": epithets})

@app.route('/vocabulary')
def get_vocabulary():
    vocabulary = epithet_generator.vocab_generator()
    return jsonify(vocabulary[0])

if __name__ == "__main__":
    app.run(debug=True)