from flask import current_app as app
from flask import render_template, request, redirect, url_for
from .forms import SearchForm, UploadSoundForm


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
  search_form = SearchForm()
  form = UploadSoundForm()
  if search_form.validate_on_submit():
    return 'Submitted!'
  if form.validate_on_submit():
    print(form.sound_file.data)
    print(request.files)
    return redirect(url_for('index'))
  return render_template('upload.html', search_form=search_form, form=form)
