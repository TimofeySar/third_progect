from flask_wtf import FlaskForm

from wtforms import StringField, IntegerField, DateTimeField, EmailField, PasswordField, BooleanField, SubmitField
from wtforms.fields.choices import SelectField
from wtforms import StringField, SelectField, SubmitField, FileField
from wtforms.validators import DataRequired


class CommForm(FlaskForm):
    Name = SelectField('Маршрут', choices=[(str(i), str(i)) for i in range(1, 7)])
    Comm = StringField('Комментарий', validators=[DataRequired()])
    Mark = SelectField('Оценка', choices=[(str(i), str(i)) for i in range(1, 11)])
    Upload = FileField('Загрузить файл')
    submit = SubmitField('Отправить')
