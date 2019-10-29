from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import TextField
from wtforms.validators import DataRequired, Regexp, Length, Optional
import re


class UploadSoundForm(FlaskForm):
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
