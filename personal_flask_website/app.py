from flask import Flask

from personal_flask_website.blueprints.page import page
from personal_flask_website.blueprints.blog import blog


def create_app():
    app = Flask(__name__)
    app.register_blueprint(page)
    app.register_blueprint(blog)
    return app
