import os
import sys
sys.path.append('.')
from flask_study_1.configs import TestingConfig
from flask_study_1 import create_app, db
from flask_study_1.models.user import User as UserModel
from flask_study_1.models.memo import Memo as MemoModel
import pytest


@pytest.fixture(scope='session')
def user_data():
    yield {'user_id': 'test',
           'user_name': 'tester',
           'password': 'test'}


@pytest.fixture(scope='session')
def memo_data():
    yield {'title': 'title',
           'content': 'content'}


@pytest.fixture(scope='session')
def app(user_data, memo_data):
    app = create_app(TestingConfig())
    with app.app_context():
        db.drop_all()
        db.create_all()
        user = UserModel(**user_data)
        db.session.add(user)
        db.session.flush() # 임시 트랜잭션.
        memo_data['user_id'] = user.id
        db.session.add(MemoModel(**memo_data))
        db.session.commit()
        yield app
        # 불필요 디비 정리
        db.drop_all()
        db_path = app.config['SQLALCHEMY_DATABASE_URI'].replace(
            'sqlite:///', ''
        )
        if os.path.isfile(db_path):
            os.remove(db_path)

@pytest.fixture(scope='session')
def client(app, user_data):
    with app.test_client() as client:
        with client.session_transaction() as session:
            session['user_id'] = user_data.get('user_id')
        yield client