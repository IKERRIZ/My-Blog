from flask import render_template,redirect,flash,url_for
from . import auth
from ..models import User
from .forms import RegistrationForm, LoginForm
from .. import db
from flask_login import login_user,logout_user,login_required


@auth.route('/login',methods=['GET','POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email = login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user,login_form.remember.data)
            return redirect('/')
            return render_template('login.html')

        flash('Invalid username or Password')

    title = "blog login"
    return render_template('auth/login.html',login_form = login_form,title=title)
