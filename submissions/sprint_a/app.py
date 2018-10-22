from sprint_a import app

data = {
    "epithets": [],
    "vocabulary": {}
}

@app.route('/')
def generate_epithets():
    return str(data["epithets"])

@app.route('/vocabulary')
def vocabulary():
    return str(data["vocabulary"])