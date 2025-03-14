from flask import Flask
from blueprints.home import home_page

def create_app():
    app = Flask(__name__)
    app.register_blueprint(home_page)

    return app
