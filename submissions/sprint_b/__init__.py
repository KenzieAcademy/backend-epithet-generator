def configure_app():
    import os

    import dotenv
    from flask import Flask, jsonify

    PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
    dotenv.load_dotenv(os.path.join(PROJECT_ROOT, '.env'))
    app = Flask(__name__)
    return app, jsonify


app, jsonify = configure_app()
