from flask import jsonify

from sprint_a import app

@app.route("/")
def generate_epithets():
    """Serves a randomly generated epithet."""
    return jsonify({"epithets": []})


@app.route("/vocabulary")
def vocabulary():
    """Serves the vocabulary to create an epithet."""
    return jsonify({"vocabulary": {}})
