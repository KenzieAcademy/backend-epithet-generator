from sprint_a import app
import json


@app.route("/")
def generate_epithets():
    """Serves a randomly generated epithet"""
    return json.dumps({"epithets": []})


@app.route("/vocabulary")
def vocabulary():
    """Serves the vocabulary to create an epithet"""
    return json.dumps({"vocabulary": {}})
