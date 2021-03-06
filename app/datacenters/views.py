from flask import render_template, url_for, redirect, request
from . import datacenters
from .. import db
from ..models import Datacenters
from flask_login import login_required
from .forms import CreateDatacenterForm, EditDatacenterForm, DeleteDatacenterForm

@datacenters.route('/', methods=['GET', 'POST'])
@login_required
def index():
    page = request.args.get('page', 1, type=int)
    sort = request.args.get('sort', '', type=str).replace('_', ' ')

    if sort:
        if 'server' in sort:
            pagination = Datacenters.query.order_by(
                '(SELECT count(id) FROM servers WHERE datacenter_id=datacenters.id) ' + sort.split(' ')[1])
        else:
            pagination = Datacenters.query.order_by(sort)
    else:
        pagination = Datacenters.query.order_by('id desc')
    pagination = pagination.paginate(page, per_page=10, error_out=False)
    datacenters = pagination.items
    return render_template('datacenter/index.html', datacenters=datacenters, pagination=pagination)

@datacenters.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    form = CreateDatacenterForm()
    if form.validate_on_submit():
        datacenter = Datacenters(
            name=form.name.data,
            location=form.location.data,
            capacity=form.capacity.data,
            tier=form.tier.data
        )
        db.session.add(datacenter)
        db.session.commit()
        return redirect(url_for('datacenters.index'))
    return render_template('datacenter/create.html', form=form)

@datacenters.route('/edit/<int:id_dc>', methods=['GET', 'POST'])
@login_required
def edit(id_dc):
    datacenter = Datacenters.query.get_or_404(id_dc)
    form = EditDatacenterForm()
    if form.validate_on_submit():
        datacenter.name = form.name.data
        datacenter.location = form.location.data
        datacenter.capacity = form.capacity.data
        datacenter.tier = form.tier.data
        db.session.add(datacenter)
        db.session.commit()
        return redirect(url_for('datacenters.index'))

    form.name.data = datacenter.name
    form.location.data = datacenter.location
    form.capacity.data = datacenter.capacity
    form.tier.data = datacenter.tier
    return render_template('datacenter/edit.html', form=form)

@datacenters.route('/delete/<int:id_dc>', methods=['GET', 'POST'])
@login_required
def delete(id_dc):
    datacenter = Datacenters.query.get_or_404(id_dc)
    form = DeleteDatacenterForm()
    if form.validate_on_submit():
        db.session.delete(datacenter)
        db.session.commit()
        return redirect(url_for('datacenters.index'))
    return render_template('datacenter/delete.html', form=form)
