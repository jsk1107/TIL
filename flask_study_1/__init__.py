import sys
sys.path.append('.')

from flask import Flask, g
from flask import render_template
from flask_wtf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

csrf = CSRFProtect()
db = SQLAlchemy()
migrate = Migrate()

def create_app(config=None):

    app = Flask(__name__)

    """ Flask Config """
    from .configs import DevelopmentConfig, ProductionConfig

    if not config:
        if app.config['DEBUG']:
            config = DevelopmentConfig()
        else:
            config = ProductionConfig()
    app.config.from_object(config)

    """ Database INIT"""
    db.init_app(app)
    if app.config['SQLALCHEMY_DATABASE_URI'].startswith('sqllite'):
        migrate.init_app(app, db, render_as_batch=True)
    else:
        migrate.init_app(app, db)

    """ Routes INIT """
    from flask_study_1.routes import base_route, auth_route
    app.register_blueprint(base_route.bp)
    app.register_blueprint(auth_route.bp)

    """ Restx INIT """
    from flask_study_1.apis import bp as api
    app.register_blueprint(api)

    """ CSRF INIT"""
    csrf.init_app(app)

    """ REQUEST HOOK """
    @app.before_request
    def before_request():
        g.db = db.session

    @app.teardown_request
    def teardown_request(exception):
        if hasattr(g, 'db'):
            g.db.close()

    @app.errorhandler(404)
    def page_404(error):
        return render_template('404.html'), 404
    return app