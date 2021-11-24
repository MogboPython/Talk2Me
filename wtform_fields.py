from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, EqualTo, ValidationError
from models import User
from passlib.hash import pbkdf2_sha256


def invalid_credentials(form, field):
    """Username and Password Checker"""

    username_entered = form.username.data
    password_entered = field.data

    #Check Credentials exists
    user_object = User.query.filter_by(username = username_entered).first() #I feel username_entered should be here
    if user_object is None:
        raise ValidationError("Username or Password is Incorrect")
    elif not pbkdf2_sha256.verify(password_entered, user_object.password):
        raise ValidationError("Username or Password is Incorrect") 

class RegistrationForm(FlaskForm):
    """Registration form"""

    username = StringField('username_label', validators=[InputRequired(message = "Username required"), Length(min = 4, max = 25, message="Username must be between 4 and 25 characters")])

    password = PasswordField('password_label', validators=[InputRequired(message = "Password required"), Length(min=4, max = 8, message="Password must be between 4 and 8 characters")])

    confirm_pass = PasswordField('confirm_pass_label', validators=[InputRequired(message = "Confirm Password"), EqualTo('password', message="Passwords must match")])


    def validate_username(self, username):
        user_object = User.query.filter_by(username = username.data).first()
        if user_object:
            raise ValidationError("Username already Exists")
        

class LoginForm(FlaskForm):
    """Login Form"""

    username = StringField('username_label', validators = [InputRequired(message="Username Required")])
    password = PasswordField('password_label', validators=[InputRequired(message="Password Required"), invalid_credentials])