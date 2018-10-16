def configure_app():
    import os
    import dotenv
    import flask import Flask

    PROJECT_ROOT = os.path.dirname(".")
    dotenv.load_dotenv(os.path.join(PROJECT_ROOT), '.env')
    app = Flask(__name__)
    return app

app = configure_app()