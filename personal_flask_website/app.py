from flask import Flask

@application.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"

if __name__ == "__main__":
    application = Flask(__name__)
    application.run(host='0.0.0.0')