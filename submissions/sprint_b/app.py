from sprint_a import app
import json


@app.route('/')
def generate_epithets():
    epithets = []
    response = {"epithets": epithets}
    return json.dumps(response)


@app.route('/vocabulary')
def vocabulary():
    vocabulary = {}
    response = {"vocabulary": vocabulary}
    return json.dumps(response)


if __name__ == '__main__':
    app.run(debug=True)
