from flask import current_app as app
from flask import render_template, request
from .forms import SearchForm

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
  form = SearchForm(request.form)
  if not form.validate_on_submit():
    return render_template('index.html', form=form)
  if request.method == 'POST':
    return 'Submitted!'