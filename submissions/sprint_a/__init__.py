def configure_app():
    import os
    import dotenv
    from flask import Flask
    PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))
    dotenv.load_dotenv(dotenv_path=os.path.join(PROJECT_ROOT, '.env'))
    app = Flask(__name__)
    return app
