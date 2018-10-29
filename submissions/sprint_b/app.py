from . import app
from flask import jsonify
from .helpers import EpithetGenerator, Vocabulary


@app.route("/")
def generate_epithets():
    epithet_generator = EpithetGenerator()
    final_string = epithet_generator.generate_epithets()

    return jsonify({"epithets": final_string})

@app.route("/<int:insults>")
def insults(insults):
    epithet_generator = EpithetGenerator()
    insult_list = []
    i = 0
    while i < insults:
        insult = epithet_generator.generate_epithets()

        insult_list.append(insult)
        i += 1
    
    return jsonify({'insults': insult_list})

@app.route("/vocabulary")
def vocabulary():
    vocab_return = Vocabulary().from_file('../../resources/data.json')
    return jsonify({"vocabulary": vocab_return})
