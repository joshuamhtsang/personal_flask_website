from flask import Flask

from blueprints.page import page
from blueprints.blog import blog
from blueprints.yt2spec import yt2spec


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'TODO REPLACE ME AT SOME POINT'
    app.register_blueprint(page)
    app.register_blueprint(blog)
    app.register_blueprint(yt2spec)
    return app
