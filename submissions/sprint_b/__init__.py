def configure_app():
    import os
    from dotenv import load_dotenv
    from flask import Flask, jsonify

    PROJECT_ROOT = os.path.dirname("./")
    env_path = os.path.join(PROJECT_ROOT, ".env")
    load_dotenv(dotenv_path=env_path, verbose=True, override=True)
    app = Flask(__name__)

    return app, jsonify


app, jsonify = configure_app()
