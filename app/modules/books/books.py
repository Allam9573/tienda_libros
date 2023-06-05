from flask import Blueprint, render_template

bp = Blueprint('books', __name__,url_prefix='/books')

@bp.route('/list')
def list():
    return render_template('books/books.html')