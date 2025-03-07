import os
from flask import redirect, render_template, flash, Blueprint, request, session, url_for
from flask_login import login_required, logout_user, current_user, login_user
from flask import current_app as app
from werkzeug.security import generate_password_hash, check_password_hash
from .forms import LoginForm, SignupForm
from .models import db, User
from . import login_manager


auth_bp = Blueprint('auth_bp', __name__,
                    template_folder='templates')


@auth_bp.route('/login', methods=['GET', 'POST'])
def login_page():
    """User login page."""
    if current_user.is_authenticated:
        return redirect(url_for('main_bp.index'))
    login_form = LoginForm()
    # POST: Create user and redirect them to the app
    if request.method == 'POST':
        if login_form.validate():
            # Get Form Fields
            email = request.form.get('email')
            password = request.form.get('password')
            # Validate Login Attempt
            user = User.query.filter_by(email=email).first()
            if user:
                if user.check_password(password=password):
                    login_user(user)
                    next = request.args.get('next')
                    return redirect(next or url_for('main_bp.index'))
        flash('Invalid username/password combination', 'warning')
        return redirect(url_for('auth_bp.login_page'))
    # GET: Serve Log-in page
    return render_template('login.html',
                           form=login_form)


@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup_page():
    """User sign-up page."""
    signup_form = SignupForm()
    # POST: Sign user in
    if request.method == 'POST':
        if signup_form.validate():
            # Get Form Fields
            name = request.form.get('name')
            email = request.form.get('email')
            password = request.form.get('password')
            existing_user = User.query.filter_by(email=email).first()
            if existing_user is None:
                user = User(name=name,
                            email=email,
                            password=generate_password_hash(
                                password, method='sha256'),
                            admin=False)
                db.session.add(user)
                db.session.commit()
                login_user(user)
                return redirect(url_for('main_bp.index'))
            flash('A user already exists with that email address.', 'warning')
            return redirect(url_for('auth_bp.signup_page'))
    # GET: Serve Sign-up page
    return render_template('/signup.html',
                           form=signup_form)


@auth_bp.route("/logout")
@login_required
def logout_page():
    """User log-out logic."""
    logout_user()
    return redirect(url_for('auth_bp.login_page'))


@login_manager.user_loader
def load_user(user_id):
    """Check if user is logged-in on every page load."""
    if user_id is not None:
        return User.query.get(user_id)
    return None


@login_manager.unauthorized_handler
def unauthorized():
    """Redirect unauthorized users to Login page."""
    flash('You must be logged in to view that page.', 'warning')
    return redirect(url_for('auth_bp.login_page'))