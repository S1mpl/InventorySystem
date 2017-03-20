from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

class CreateServerForm(FlaskForm):
    name = StringField('Название сервера', validators=[DataRequired()])
    manufacturer =  StringField('Производитель', validators=[DataRequired()])
    model = StringField('Модель', validators=[DataRequired()])
    serial_number = StringField('Серийный номер', validators=[DataRequired()])
    os = SelectField('Операционная система',
                     choices=[('Ubuntu server', 'Ubuntu server'), ('Debian', 'Debian'), ('Red Hat', 'Red Hat')],
                     coerce=str)
    submit = SubmitField('Создать')

class EditServerForm(FlaskForm):
    name = StringField('Название сервера', validators=[DataRequired()])
    manufacturer = StringField('Производитель', validators=[DataRequired()])
    model = StringField('Модель', validators=[DataRequired()])
    serial_number = StringField('Серийный номер', validators=[DataRequired()])
    os = SelectField('Операционная система',
                     choices=[('Ubuntu server', 'Ubuntu server'), ('Debian', 'Debian'), ('Red Hat', 'Red Hat')],
                     coerce=str)
    submit = SubmitField('Изменить')

class DeleteServerForm(FlaskForm):
    submit = SubmitField('Удалить')