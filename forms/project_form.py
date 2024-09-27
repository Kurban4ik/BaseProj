from flask_wtf import FlaskForm
from wtforms import BooleanField, SubmitField, FileField, SelectField
from wtforms import PasswordField, StringField, TextAreaField, SubmitField, BooleanField, EmailField
from wtforms.validators import DataRequired


class ProjectForm(FlaskForm):
    is_private = BooleanField("В открытом доступе?")
    submit = SubmitField('Применить')
    project_name = StringField('Название проекта', validators=[DataRequired])
    description = TextAreaField('Описание проекта', validators=[DataRequired])
