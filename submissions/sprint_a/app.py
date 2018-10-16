import app


@app.route('/')
def generate_epithets():
    epithets = []
    return {"epithets": epithets}


@app.route('/vocabulary')
def vocabulary():
    vocabulary = {}
    return {"vocabulary": vocabulary}


if __name__ == '__main__':
    app.run(debug=True)
