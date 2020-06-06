from flask import Flask,redirect
from celery import Celery
from flasgger import Swagger
from flask_env import MetaFlaskEnv
from werkzeug.debug import DebuggedApplication
import logging
import os

from app.api import api as api_blueprint

def create_app(settings_override=None):
    class Configuration(metaclass=MetaFlaskEnv):
        ENV_LOAD_ALL = True
    app = Flask(__name__, instance_relative_config=True)
    app.logger.setLevel(logging.DEBUG)

    app.config.from_object('app.config.settings')
    #prod and dev
    env=os.environ.get('ENV') or 'prod'
    logging.info("start server with env: %s"%env)
    if env == 'dev':
        app.config.from_object('app.config.settings_dev')
    else:
        app.config.from_object('app.config.settings_prod')

    app.config.from_object(Configuration)

    if settings_override:
        app.config.update(settings_override)


    if app.debug:
        app.wsgi_app = DebuggedApplication(app.wsgi_app, evalex=True)

    
    app.register_blueprint(api_blueprint, url_prefix='/api/')

    swagger = Swagger(app)
    
    @app.route('/')
    def hello():
        return redirect('/apidocs')

    return app


def create_celery_app(app=None):
    app = app or create_app()

    CELERY_TASK_LIST = [
        'app.tasks',
    ]
    celery = Celery(app.import_name, broker=app.config['CELERY_BROKER_URL'],
                    include=CELERY_TASK_LIST)
    celery.conf.update(app.config)

    TaskBase = celery.Task

    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)
    celery.Task = ContextTask
    return celery



if __name__ == '__main__':
    app=create_app()
    app.run(debug=True)


