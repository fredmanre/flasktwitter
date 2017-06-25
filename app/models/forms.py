from flask_wtf import FlaskForm  # para el manejo de formularios
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField(
        "username",
        validators=[DataRequired(message="Este campo es requerido")])
    password = PasswordField(
        "password",
        validators=[DataRequired(message="Este campo es obligatorio!")])
    remember_me = BooleanField("remember_me")
