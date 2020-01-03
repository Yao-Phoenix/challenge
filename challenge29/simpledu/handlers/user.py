from flask import Blueprint, render_template, abort
from simpledu.models import User
user = Blueprint('user', __name__, url_prefix='/user')

@user.route('/<username>')
def detail(username):
    user = User.query.filter_by(username=username).first()
    if not user:
        abort(404)
    return render_template('detail.html', user=user)

