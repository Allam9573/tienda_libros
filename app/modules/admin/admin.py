from flask import Blueprint, render_template, request, redirect, url_for
from app.modules.db.db import get_connection
from datetime import datetime
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
        tiempo = datetime.now()
        fechaActual = tiempo.strftime("%Y%H%M%S")

        if imagenURL.filename != '':
            nuevoNombre = fechaActual + "_"+imagenURL.filename
            imagenURL.save('app/static/img/'+nuevoNombre)
        cursor = conexion.cursor(buffered=True)
        query = "INSERT INTO libros(nombre, autor, imagen, precio) VALUES(%s,%s,%s,%s)"
        cursor.execute(query, (nombre, autor, nuevoNombre, precio))
        conexion.commit()
        return redirect(url_for('admin.books_list'))
    else:
        cursor = conexion.cursor(buffered=True)
        cursor.execute("SELECT * FROM libros")
        data = cursor.fetchall()
    return render_template('admin/upload.html', data=data, title='Upload Book')


@bp.route('/books_list')
def books_list():
    cursor = conexion.cursor(buffered=True)
    cursor.execute("SELECT * FROM libros")
    data = cursor.fetchall()
    return render_template('admin/upload.html', data=data, title='Books List')


@bp.route('/delete_book/<id>')
def delete_book(id):
    cursor = conexion.cursor(buffered=True)
    cursor.execute('DELETE FROM libros WHERE id=%s', [id])
    conexion.commit()
    return redirect(url_for('admin.books_list'))


@bp.route('/create_user')
def create_user():
    return render_template('admin/create_user.html')
