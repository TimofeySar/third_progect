from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DateTimeField, EmailField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class CommForm(FlaskForm):
    Name = IntegerField('Номер маршрута', validators=[DataRequired()])
    Comm = StringField('Комментарий', validators=[DataRequired()])
    Mark = IntegerField('Оценка', validators=[DataRequired()])
    submit = SubmitField('Отправить')
