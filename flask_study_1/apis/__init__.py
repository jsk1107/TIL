from flask import Blueprint
from flask_restx import Api
from .user import ns as UserNamespace


bp = Blueprint('api', __name__, url_prefix='/api')

api = Api(bp, title='Flask Study 1 API', version='1.0', doc='/docs', description='빡공해서 백앤드 정복하자')

api.add_namespace(UserNamespace)