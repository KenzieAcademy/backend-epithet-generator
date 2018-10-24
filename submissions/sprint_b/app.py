from . import app, jsonify
from helpers import FileManager
from helpers import Vocabulary


@app.route('/')
def generate_epithets():
    data = FileManager.read_json(".../resources/data.json")
    print(data)
    response = {"epithets": []}
    return jsonify(response)


@app.route('/vocabulary')
def vocabulary():
    response = {"vocabulary": {}}
    return jsonify(response)
