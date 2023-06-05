from flask import Flask, render_template
from app.modules.auth import auth
from app.modules.books import books


def create_app():
    app = Flask(__name__)
    app.register_blueprint(auth.bp)
    app.register_blueprint(books.bp)

    @app.route('/')
    def index():
        return render_template('index.html')
    return app
