from datetime import datetime
from flask import render_template, sessions, url_for, redirect
from . import datacenters
from .. import db
from ..models import Users

@datacenters.route('/', methods=['GET', 'POST'])
def index():
    return render_template('errors/404.html')