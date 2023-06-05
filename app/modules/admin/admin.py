from flask import Blueprint, render_template

bp = Blueprint('admin',__name__,url_prefix='/admin')

@bp.route('/')
def admin_home():
    return render_template('admin/index.html')

@bp.route('/upload')
def upload():
    return render_template('admin/upload.html')