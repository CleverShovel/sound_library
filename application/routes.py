from flask import current_app as app
from flask import render_template, request, redirect, url_for, flash, Markup, abort, send_from_directory
from .forms import UploadSoundForm
from werkzeug.utils import secure_filename
from os import path
from pathlib import Path
from .models import db, User, Sound


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html', sounds=Sound.query.all())


@app.route('/play/<path:filename>')
def download_sound(filename):
    return send_from_directory(app.config['SOUND_FOLDER'],
                               filename)


@app.route('/sound/<int:id>')
def sound(id):
    sound_row = Sound.query.get(id)
    if sound_row:
      print(sound_row, sound_row.path)
      return render_template('sound.html', sound_row=sound_row)
    abort(404)


@app.route('/upload_sound', methods=['GET', 'POST'])
def upload_sound():
    form = UploadSoundForm()
    if form.validate_on_submit():
        file = form.sound_file.data
        old_path = Path(file.filename)
        sound_name = form.name.data or old_path.stem
        file_path = path.join(app.config['SOUND_FOLDER'], str(
            Sound.query.count() + 1) + old_path.suffix)
        file.save(file_path)
        new_sound = Sound(name=sound_name, path=str(
            Sound.query.count() + 1) + old_path.suffix)
        db.session.add(new_sound)
        db.session.commit()
        flash(Markup("File <strong>{}</strong> successfully uploaded!".format(sound_name)),
              'success')
        return redirect(url_for('upload_sound'))
    return render_template('upload.html', form=form)
