from flask import Blueprint

api = Blueprint('api', __name__)

from . import task_one
from . import rnd