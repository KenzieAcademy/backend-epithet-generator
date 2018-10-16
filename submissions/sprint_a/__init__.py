
def configure_app():
    import os
    from dotenv import load_dotenv
    from flask import Flask

    PROJECT_ROOT = os.path.dirname('.')
    print(PROJECT_ROOT)
    dotenv_path = os.path.abspath(
        os.path.join(PROJECT_ROOT, '.', '.env')
    )
    load_dotenv(dotenv_path)
    app = Flask(__name__)

    return app
    # dotenv2 = load_dotenv(os.path.join(PROJECT_ROOT, '.', '.env'))


app = configure_app()
