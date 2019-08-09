from flask import Flask
from celery import Celery

from blueprints.page import page
from blueprints.blog import blog
from blueprints.yt2spec import yt2spec
from blueprints.celery_tester import celery_tester

CELERY_BROKER_URL = 'amqp://guest:guest@rabbitmq:5672'
CELERY_BACKEND = 'rpc://'


def make_celery(app):
    celery = Celery(
        app.import_name,
        backend=app.config['CELERY_RESULT_BACKEND'],
        broker=app.config['CELERY_BROKER_URL']
    )
    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'TODO REPLACE ME AT SOME POINT'
    app.config['CELERY_BROKER_URL'] = CELERY_BROKER_URL
    app.config['CELERY_RESULT_BACKEND'] = CELERY_BACKEND

    app.config.update(
        CELERY_BROKER_URL=CELERY_BROKER_URL,
        CELERY_RESULT_BACKEND=CELERY_BACKEND
    )
    celery = make_celery(app)
    print("Celery setup!")

    app.register_blueprint(page)
    app.register_blueprint(blog)
    app.register_blueprint(yt2spec)
    app.register_blueprint(celery_tester)

    return app
