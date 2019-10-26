from flask import current_app as app
from flask import render_template, request, redirect, url_for
from .forms import SearchForm, UploadSoundForm


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
  form = SearchForm()
  if not form.validate_on_submit():
    return render_template('index.html', form=form)
  if request.method == 'POST':
    return 'Submitted!'

@app.route('/sound/<int:id>')
def sound(id):
  return 'Sound #{}'.format(id)

@app.route('/upload_sound', methods=['GET', 'POST'])
def upload_sound():
  form = UploadSoundForm()
  if form.validate_on_submit():
    print(form.sound_file.data)
    print(request.files)
    return redirect(url_for('index'))
  return render_template('upload.html', form=form)
