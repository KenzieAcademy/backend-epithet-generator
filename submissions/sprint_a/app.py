from sprint_a import app
from flask import jsonify

@app.route('/')
def generate_epithets():
    epithets = []
    return jsonify({"epithets": epithets})

@app.route('/vocabulary')
def get_vocabulary():
    vocabulary = {}
    return jsonify({"vocabulary": {}})

if __name__ == "__main__":
    app.run(debug=True)