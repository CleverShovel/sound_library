from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import TextField
from wtforms.validators import DataRequired


class SearchForm(FlaskForm):
  search = TextField('')


class UploadSoundForm(FlaskForm):
  name = TextField('Enter sound name:', validators=[DataRequired()])
  sound_file = FileField('Choose file:', validators=[
      FileRequired('Empty file!'),
      #.wav, .mp3, .aac, .ogg, .oga, and .flac
      FileAllowed(['wav', 'mp3', 'aac', 'ogg', 'oga', 'flac'], 'Sounds only!')
  ])
