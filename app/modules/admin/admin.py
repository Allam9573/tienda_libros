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
        nombre = request.form['nombre']
        autor = request.form['autor']
        imagenURL = request.files['imagenURL']
        url = request.form['url']
        precio = request.form['precio']
        cursor = conexion.cursor(buffered=True)
        query = "INSERT INTO libros(nombre, autor, imagen, precio) VALUES(%s,%s,%s,%s)"
        cursor.execute(query, (nombre, autor, imagenURL.filename, precio))
        conexion.commit()
        return redirect(url_for('admin.books_list'))
    else:
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT * FROM libros")
        data = cursor.fetchall()
    return render_template('admin/upload.html', data=data)


@bp.route('/books_list')
def books_list():
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT * FROM libros")
    data = cursor.fetchall()
    return render_template('admin/upload.html', data=data)
