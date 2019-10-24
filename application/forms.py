from flask_wtf import FlaskForm
from wtforms import TextField
from wtforms.validators import DataRequired

class SearchForm(FlaskForm):
  search_field = TextField('', validators=[DataRequired()])