from sprint_a import app
from flask import jsonify


@app.route('/')
def generate_epithets():
    """Serves up placeholder for future insult generator"""
    return jsonify({'epithets': []})


@app.route('/vocabulary')
def vocabulary():
    """Serves up a vocab list of insult words from a file"""
    return jsonify({'vocabulary': {}})
