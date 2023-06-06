from flask import Blueprint, render_template, request

bp = Blueprint('admin', __name__, url_prefix='/admin')


@bp.route('/')
def admin_home():
    return render_template('admin/index.html')


@bp.route('/upload', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        nombre = request.form['nombre']
        imagenURL = request.form['imagenURL']
        url = request.form['url']
        precio = request.form['precio']
    return render_template('admin/upload.html')
