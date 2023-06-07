from flask import Blueprint, render_template
from app.modules.db.db import get_connection

bp = Blueprint('books', __name__, url_prefix='/books')
conexion = get_connection()


@bp.route('/list')
def list():
    cursor = conexion.cursor(dictionary=True)
    query = "SELECT * FROM libros"
    cursor.execute(query)
    data = cursor.fetchall()
    return render_template('books/books.html', data=data)
