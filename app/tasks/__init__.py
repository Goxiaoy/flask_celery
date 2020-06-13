from flask import current_app
from app.create_app import create_celery_app
celery=create_celery_app(current_app)

from . import task_one
from . import rnd