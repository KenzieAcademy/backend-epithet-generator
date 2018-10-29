
def configure_app():
    import os
    import dotenv
    from flask import Flask
    from flask_restful import Api
    PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
    dotenv.load_dotenv(os.path.join(PROJECT_ROOT, '.env'))
    app = Flask(__name__)
    api = Api(app)
    return app, api


app, api = configure_app()
