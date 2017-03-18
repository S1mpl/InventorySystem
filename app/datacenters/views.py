from datetime import datetime
from flask import render_template, sessions, url_for, redirect
from . import datacenters
from .. import db
from ..models import Users
from flask_login import login_required

@datacenters.route('/', methods=['GET', 'POST'])
@login_required
def index():
    return render_template('errors/404.html')