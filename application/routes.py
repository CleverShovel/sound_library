from flask import current_app as app
from flask import render_template, request, redirect, url_for, flash, Markup
from .forms import SearchForm, UploadSoundForm
from werkzeug.utils import secure_filename
from os import path
from pathlib import Path


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
  search_form = SearchForm()
  if search_form.validate_on_submit():
    return 'Submitted!'
  return render_template('index.html', search_form=search_form)

@app.route('/sound/<int:id>')
def sound(id):
  return 'Sound #{}'.format(id)

@app.route('/upload_sound', methods=['GET', 'POST'])
def upload_sound():
  form = UploadSoundForm()
  if form.validate_on_submit():
    file = form.sound_file.data
    filename = secure_filename(
        form.name.data + Path(file.filename).suffix if form.name.data else file.filename)
    file.save(path.join(app.config['SOUND_FOLDER'], filename))
    flash(Markup("File <strong>{}</strong> successfully uploaded!".format(filename)),
          'success')
    return redirect(url_for('upload_sound'))
  return render_template('upload.html', form=form)
