import os

BASE_PATH = os.path.dirname(os.path.abspath(__file__))

class Config:
    """ Flask Config """
    SECRET_KEY = 'secretkey'
    SESSION_COOKIE_NAME = 'flask_study_1'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:password@localhost/flask_study_1?charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SWAGGER_UI_DOC_EXPANSION = 'list'


class DevelopmentConfig(Config):
    """ Flask Config for dev """
    DEBUG = True
    SEND_FILE_MAX_AGE_DEFAULT = 1
    # TODO: Front 호출시 처리
    WTF_CSRF_ENABLED = False


class ProductionConfig(DevelopmentConfig):
    pass


class TestingConfig(DevelopmentConfig):
    __test__ = False
    TESTING = True
    # Test시에는 Sqllite를 이용해서 테스트를 한다.
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(BASE_PATH, "sqllite_test.db")}'