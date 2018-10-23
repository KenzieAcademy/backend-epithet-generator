#!/usr/bin/env python3
from flask import jsonify

from sprint_a import app


@app.route('/')
def generate_epithets():
    return jsonify({"epithets": []})


@app.route('/vocabulary')
def vocabulary():
    return jsonify({"vocabulary": {}})
