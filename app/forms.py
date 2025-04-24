from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms.fields.choices import SelectField
from wtforms.fields.simple import StringField, BooleanField, SubmitField, PasswordField, TextAreaField, FileField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class Loginform(FlaskForm):
    email_or_username = StringField('Почта или логин', validators=[Length(max=50),
        DataRequired(message='Введите почту или логин')
    ])
    password = PasswordField('Пароль', validators=[Length(max=50),
        DataRequired(message='Введите пароль')
    ])
    remember = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


class RegistrationForm(FlaskForm):
    username = StringField('Логин', validators=[
        DataRequired(message='Придумайте пароль'),
        Length(3, 20, message='Логин должен быть от 3 до 20 символов')
    ])
    email = StringField('Почта', validators=[
        DataRequired(message='Введите почту'),
        Email(message='Неверный email адрес')
    ])
    password = PasswordField('Пароль', validators=[
        Length(max=50),
        DataRequired(message='Придумайте пароль')
    ])
    password2 = PasswordField('Повторите пароль', validators=[
        Length(max=50),
        DataRequired(message='Повторите пароль'),
        EqualTo('password', message='Неверный пароль')
    ])
    submit = SubmitField('Зарегистрироваться')


class PostForm(FlaskForm):
    text = TextAreaField('Содержание', validators=[
        DataRequired(message="Поле обязательно")
    ])
    image = FileField('Изображение', validators=[
        FileAllowed(['jpg', 'jpeg', 'png'], 'Только изображения (jpg, png)')
    ])


class ProfileForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired(), Length(max=50)])
    description = TextAreaField('О себе', validators=[Length(max=500)])
    profile_image = FileField('Аватар')
    password = PasswordField('Новый пароль (оставьте пустым, если не меняется)')
