from flask import Flask
from flask import render_template
from flask_wtf import CSRFProtect
import sys
sys.path.append('./')

csrf = CSRFProtect()


def create_app():

    app = Flask(__name__)

    """ CSRF TOKEN """
    app.config['SECRET_KEY'] = 'secretkey'

    """ Config INIT"""
    if app.config['DEBUG']:
        app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1

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