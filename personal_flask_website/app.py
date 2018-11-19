from flask import Flask

from personal_flask_website.blueprints.page import page

#@application.route("/")
#def hello():
#    return "<h1 style='color:blue'>Hello There!</h1>"

def create_app():
    app = Flask(__name__)
    app.register_blueprint(page)
    return app
