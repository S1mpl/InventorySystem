from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, IntegerField
from wtforms.validators import DataRequired, Length, Regexp, EqualTo
from wtforms import ValidationError
from ..models import Users

class CreateDatacenterForm(FlaskForm):
    name = StringField('Название датацентра', validators=[DataRequired()])
    location =  StringField('Место расположения', validators=[DataRequired()])
    capacity = IntegerField('Вместимость', validators=[DataRequired()])
    tier = SelectField('Tier', choices=[(1,1),(2,2),(3,3)], coerce=int)
    submit = SubmitField('Создать')

class EditDatacenterForm(FlaskForm):
    name = StringField('Название датацентра', validators=[DataRequired()])
    location =  StringField('Место расположения', validators=[DataRequired()])
    capacity = IntegerField('Вместимость', validators=[DataRequired()])
    tier = SelectField('Tier', choices=[(1,1),(2,2),(3,3)], coerce=int)
    submit = SubmitField('Изменить')

class DeleteDatacenterForm(FlaskForm):
    submit = SubmitField('Удалить')


