from flask_wtf import FlaskForm
from wtforms import BooleanField, SubmitField, FileField, SelectField
from wtforms import PasswordField, DateField, StringField, TextAreaField, SubmitField, BooleanField, EmailField
from wtforms.validators import DataRequired


class TaskForm(FlaskForm):
    is_private = BooleanField("В открытом доступе?")
    submit = SubmitField('Применить')
    project_name = StringField('Название задачи', validators=[DataRequired])
    description = TextAreaField('Описание задачи', validators=[DataRequired])
    project = SelectField()
    deadline = DateField()