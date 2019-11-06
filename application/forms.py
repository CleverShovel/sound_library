from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import TextField, PasswordField, StringField
from wtforms.validators import DataRequired, Regexp, Length, Optional, Email, EqualTo, ValidationError


class SignupForm(FlaskForm):
  """User Signup Form."""

  name = StringField('Name',
                     validators=[DataRequired(message=('Enter your name.'))])
  email = StringField('Email',
                      validators=[Email(
                          message=('Please enter a valid email address.')),
                          DataRequired(message=('Please enter a valid email address.'))])
  password = PasswordField('Password',
                           validators=[DataRequired(message='Please enter a password.'),
                                       Length(min=6, message=(
                                           'Please select a stronger password.')),
                                       EqualTo('confirm', message='Passwords must match')])
  confirm = PasswordField('Confirm Password')


class LoginForm(FlaskForm):
    """User Login Form."""

    email = StringField('Email', validators=[DataRequired('Please enter a valid email address.'),
                                             Email('Please enter a valid email address.')])
    password = PasswordField('Password', validators=[
                             DataRequired('Enter password')])


class UploadSoundForm(FlaskForm):
  """Upload sound form"""

  name = TextField('Enter sound name:', validators=[
      Optional(False),
      Regexp(r"^[а-яА-Яa-zA-Z\. ]+$",
             message="Incorrect name: only russian or english letters, dot and space are accepted!"),
      Length(min=1, max=255, message="Maximum length 255 characters!")])
  sound_file = FileField('Choose file:', validators=[
      FileRequired('Empty file!'),
      #.wav, .mp3, .aac, .ogg, .oga, and .flac
      FileAllowed(['wav', 'mp3', 'aac', 'ogg', 'oga', 'flac'], 'Sounds only!')
  ])
