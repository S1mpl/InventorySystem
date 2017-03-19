from flask import render_template, url_for, redirect, request
from . import servers
from .forms import CreateServerForm, EditServerForm, DeleteServerForm
from .. import db
from ..models import Servers
from flask_login import login_required

@servers.route('/dc/<int:id_dc>', methods=['GET', 'POST'])
@login_required
def index(id_dc):
    page = request.args.get('page', 1, type=int)
    sort_name = request.args.get('sort_name', '', type=str)
    sort_manufacturer = request.args.get('sort_manufacturer', '', type=str)
    search = request.args.get('search', '', type=str)
    if sort_manufacturer:
        pagination = Servers.query.filter_by(datacenter_id=id_dc).order_by('manufacturer '+sort_manufacturer)
    elif sort_name:
        pagination = Servers.query.filter_by(datacenter_id=id_dc).order_by('name '+sort_name)
    else:
        pagination = Servers.query.filter_by(datacenter_id=id_dc).order_by('id desc')
    if search:
        pagination = pagination.filter(Servers.name.like('%'+search+'%'))
    pagination = pagination.paginate(page, per_page=1,error_out=False)
    servers = pagination.items
    return render_template('servers/index.html', servers=servers, pagination=pagination, id_dc=id_dc)

@servers.route('/dc/<int:id_dc>/create', methods=['GET', 'POST'])
@login_required
def create(id_dc):
    form = CreateServerForm()
    if form.validate_on_submit():
        server = Servers(
            name=form.name.data,
            manufacturer=form.manufacturer.data,
            model=form.model.data,
            serial_number=form.serial_number.data,
            os=form.os.data,
            datacenter_id=id_dc
        )
        db.session.add(server)
        db.session.commit()
        return redirect( url_for('servers.index', id_dc=id_dc))
    return render_template('servers/create.html', form=form)

@servers.route('/dc/<int:id_dc>/edit/<int:id_sv>', methods=['GET', 'POST'])
@login_required
def edit(id_dc, id_sv):
    server = Servers.query.get_or_404(id_sv)
    form = EditServerForm()
    if form.validate_on_submit():
        server.name = form.name.data
        server.manufacturer = form.manufacturer.data
        server.model = form.model.data
        server.serial_number = form.serial_number.data
        server.os = form.os.data
        db.session.add(server)
        db.session.commit()
        return redirect(url_for('servers.index', id_dc=id_dc))
    form.name.data = server.name
    form.manufacturer.data = server.manufacturer
    form.model.data = server.model
    form.serial_number.data = server.serial_number
    form.os.data = server.os
    return render_template('servers/create.html', form=form)

@servers.route('/dc/<int:id_dc>/delete/<int:id_sv>', methods=['GET', 'POST'])
@login_required
def delete(id_dc, id_sv):
    server = Servers.query.get_or_404(id_sv)
    form = DeleteServerForm()
    if form.validate_on_submit():
        db.session.delete(server)
        db.session.commit()
        return redirect(url_for('servers.index', id_dc=id_dc))
    return render_template('servers/delete.html', form=form)