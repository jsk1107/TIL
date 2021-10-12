from flask import Flask
from flask import render_template
from flask_wtf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import sys
sys.path.append('./')

csrf = CSRFProtect()
db = SQLAlchemy()
migrate = Migrate()

def create_app():

    app = Flask(__name__)

    """ CSRF TOKEN """
    app.config['SECRET_KEY'] = 'secretkey'
    app.config['SESSION_COOKIE_NAME'] = 'flask_study_1'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost/flask_study_1?charset=utf8'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    """ Config INIT"""
    if app.config['DEBUG']:
        app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1

    """ Database INIT"""
    db.init_app(app)
    if app.config['SQLALCHEMY_DATABASE_URI'].startswith('sqllite'):
        migrate.init_app(app, db, render_as_batch=True)
    migrate.init_app(app, db)

    """ Routes INIT """
    from flask_study_1.routes import base_route, auth_route
    app.register_blueprint(base_route.bp)
    app.register_blueprint(auth_route.bp)

    """ CSRF INIT"""
    csrf.init_app(app)

    @app.errorhandler(404)
    def page_404(error):
        return render_template('404.html'), 404
    return app