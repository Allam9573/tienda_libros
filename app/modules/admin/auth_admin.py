from flask import Blueprint, render_template

bp = Blueprint('auth_admin', __name__, url_prefix='/auth/admin')


@bp.route('/login')
def login():
    return render_template('admin/login.html')
