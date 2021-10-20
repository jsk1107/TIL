from flask import Blueprint, g, abort
from flask_restx import Api
from .user import ns as UserNamespace
from .memo import ns as MemoNamespace
from functools import wraps


def check_session(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not g.user:
            abort(401)
        return func(*args, **kwargs)
    return wrapper


bp = Blueprint('api', __name__, url_prefix='/api')

api = Api(bp, title='Flask Study 1 API', version='1.0', doc='/docs', decorators=[check_session],
          description='빡공해서 백앤드 정복하자')

api.add_namespace(UserNamespace)
api.add_namespace(MemoNamespace)