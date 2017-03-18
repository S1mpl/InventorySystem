from flask import Blueprint

datacenters = Blueprint('datacenters', __name__)

from . import views, forms, errors