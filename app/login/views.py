from datetime import datetime
from flask import render_template, sessions, url_for, redirect
from . import login
from .. import db
from ..models import Users

@login.route('/login', methods=['GET', 'POST'])
def index():
    return render_template('errors/404.html')