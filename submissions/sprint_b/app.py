from . import app, jsonify


@app.route('/')
def generate_epithets():

    response = {"epithets": []}
    return jsonify(response)


@app.route('/vocabulary')
def vocabulary():
    response = {"vocabulary": {}}
    return jsonify(response)
