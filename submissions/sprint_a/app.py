from sprint_a import app
from flask import jsonify


@app.route('/')
def generate_epithets():
    """Serves a placeholder for future epithet generator"""
    return jsonify({'epithets': []})


@app.route('/vocabulary')
def vocabulary():
    """Serves a placeholder for future insult vocabulary"""
    return jsonify({'vocabulary': {}})
