from flask import current_app as app
from flask import Blueprint, render_template, request, redirect, url_for, flash, Markup, abort, send_from_directory
from flask_assets import Environment, Bundle
from flask_login import current_user, login_required
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash
from os import path
from pathlib import Path
from .forms import UploadSoundForm, PasswordForm
from .models import db, User, Sound


main_bp = Blueprint('main_bp', __name__,
                    template_folder='templates')


@main_bp.route('/')
@main_bp.route('/index')
def index():
    return render_template('index.html', sounds=Sound.query.all())


@main_bp.route('/play/<path:filename>')
def download_sound(filename):
    return send_from_directory(app.config['SOUND_FOLDER'],
                               filename,
                               as_attachment=True)


@main_bp.route('/sound/<int:id>')
@login_required
def sound(id):
    sound_row = Sound.query.get(id)
    if sound_row:
      return render_template('sound.html', sound_row=sound_row)
    abort(404)


@main_bp.route('/user/<int:id>', methods=['GET', 'POST'])
@login_required
def user_page(id):
    password_form = PasswordForm()
    user_row = User.query.get(id)
    if      (request.method == 'POST' and 
            password_form.validate_on_submit()):
        new_password = request.form.get('new_password')
        user_row.password = generate_password_hash(
                                new_password, method='sha256')
        db.session.commit()
        flash('Password was changed successfully', 'success')
        return redirect(url_for('main_bp.index'))
    elif user_row:
        return render_template('user.html', user_row=user_row, form=password_form)
    abort(404)


@main_bp.route('/upload_sound', methods=['GET', 'POST'])
@login_required
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
        return redirect(url_for('main_bp.upload_sound'))
    return render_template('upload.html', form=form)
