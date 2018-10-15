def configure_app():
    import os
    import dotenv
    import flask
    PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
    dotenv.load_dotenv(os.path.join(PROJECT_ROOT, '.env'))
    return flask.Flask(__name__)

app = configure_app()
