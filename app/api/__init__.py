"""
Initialize blueprint for the restapi module.
"""

from flask import Blueprint

api = Blueprint('api', __name__)

from . import views, errors