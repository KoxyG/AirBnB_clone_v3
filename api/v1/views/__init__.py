#!/usr/bin/python3

"""Init file for views model"""

from flask import Blueprint


app_view = Blueprint('app_view', __name__, url_prefix='/api/v1')

