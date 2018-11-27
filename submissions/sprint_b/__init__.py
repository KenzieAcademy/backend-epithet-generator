def configure_app():
    import os
    from dotenv import load_dotenv
    from flask import Flask

    PROJECT_ROOT = os.path.dirname(__file__)
    env_path = os.path.join(PROJECT_ROOT, ".env")
    load_dotenv(dotenv_path=env_path, verbose=True, override=True)
    app = Flask(__name__)

    return app


app = configure_app()
