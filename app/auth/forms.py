from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Regexp, EqualTo
from wtforms import ValidationError
from ..models import Users

class LoginForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')

class RegisterForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[
        DataRequired(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$',0,
                                              'Имя пользователя должно содержать только буквы, цифры, точки и подчеркивания')])
    password = PasswordField('Пароль', validators=[
        DataRequired(), EqualTo('password2',message='Пароли должны совпадать')])
    password2 = PasswordField('Подтверждение пароля', validators=[DataRequired()])
    submit = SubmitField('Зарегистрироваться')

    def validate_username(self, field):
        if Users.query.filter_by(username=field.data).first():
            raise ValidationError('Имя пользователя уже используется')