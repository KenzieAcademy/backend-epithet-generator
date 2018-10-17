from sprint_b import app
import json
from helpers import EpithetGenerator


@app.route('/')
def generate_epithets():
    epithets = EpithetGenerator.generate_epithets('../../resources/data.json')
    response = {"epithets": epithets}
    return json.dumps(response)


@app.route('/vocabulary')
def vocabulary():
    vocabulary = {}
    response = {"vocabulary": vocabulary}
    return json.dumps(response)


if __name__ == '__main__':
    app.run(debug=True)
