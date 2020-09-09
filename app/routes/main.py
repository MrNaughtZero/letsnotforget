from flask import Blueprint, redirect, url_for, render_template
from flask_login import login_required, current_user
from app.models import List

main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
def index():
    if not current_user.is_authenticated:
        return redirect(url_for('auth.login'))
    return render_template('/main/index.html', list=List().fetchAll(current_user.get_id()))

@main.route('/add/<item>', methods=['GET'])
def add_item(item):
    if not current_user.is_authenticated:
        return redirect(url_for('auth.login'))
    return List(userID=current_user.get_id(), text=item).add()
    

@main.route('/delete/<item>', methods=['GET'])
def delete_item(item):
    if not current_user.is_authenticated:
        return redirect(url_for('auth.login'))
    try:
        print(current_user.get_id())
        print(item)
        query = List().fetchItem(current_user.get_id(), item)
        query.delete()
    except Exception as e:
        print(e)