from flask import Blueprint, render_template, request, redirect, url_for
from app.modules.db.db import get_connection
bp = Blueprint('admin', __name__, url_prefix='/admin')

conexion = get_connection()

@bp.route('/')
def admin_home():
    return render_template('admin/index.html')


@bp.route('/upload', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        nombre = requet.form['nombre']
        autor = request.form['autor']
        imagenURL = request.files['imagenURL']
        url = request.form['url']
        precio = request.form['precio']
        data = [nombre, autor, precio]
    return render_template('admin/upload.html')

