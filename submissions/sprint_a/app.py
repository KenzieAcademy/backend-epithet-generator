from sprint_a import app

data = {
    "epithets": [],
    "vocabulary": {}
}

@app.route('/')
def generate_epithets():
    return data["epithets"]

@app.route('/vocabulary')
def vocabulary():
    return data["vocabulary"]