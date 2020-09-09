from app.models import User
from flask import Blueprint, render_template, redirect, flash, get_flashed_messages, request, url_for
from flask_login import login_user, current_user, logout_user, login_required

auth = Blueprint('auth', __name__)

@auth.route('/auth/register', methods=['GET'])
def register():
    return render_template('/auth/register.html')

@auth.route('/auth/register/user', methods=['POST'])
def addUser():
    if not User().checkIfRegistered(request.form.get('form-email')):
        User(email=request.form.get('form-email'), pw=User.hashPassword(request.form.get('form-password'))).add()
        flash('Succesfully registered. Please login')
    else:
        flash('Your email has already been registered. Please login')
    
    return redirect(url_for('auth.login'))

@auth.route('/auth/login', methods=['GET'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    return render_template('/auth/login.html', message=get_flashed_messages())

@auth.route('/auth/login/attempt', methods=['POST'])
def loginUser():
    usr = User().checkIfRegistered(request.form.get('form-email'))
    if not usr:
        flash('Incorrect login details')
        return redirect(url_for('auth.login'))
    if User().hashPassword(request.form.get('form-password')) != usr.pw:
        flash('Incorrect login details')
        return redirect(url_for('auth.login'))
    
    login_user(usr)
    return redirect(url_for('main.index'))

@auth.route('/auth/logout')
def logout():
    if current_user.is_authenticated:
        logout_user()
    
    return redirect(url_for('auth.login'))