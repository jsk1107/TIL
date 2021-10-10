from flask import Blueprint, render_template, redirect, url_for, flash, session, request
from flask_study_1.forms.auth_form import LoginForm, RegisterForm
from werkzeug import security

NAME = 'auth'
bp = Blueprint(NAME, __name__, url_prefix='/auth')


""" only for testing """
class User:
    def __init__(self, user_id, user_name, password):
        self.user_id = user_id
        self.user_name = user_name
        self.password = password

USERS = []
USERS.append(User('jsk', 'jsk', security.generate_password_hash('1234')))
USERS.append(User('admin', 'admin', security.generate_password_hash('1234')))
USERS.append(User('tester', 'tester', security.generate_password_hash('1234')))


@bp.route('/')
def index():
    return redirect(url_for(f'{NAME}.login'))


@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    # POST, validate OK -> 정상적으로 제출이 되었다면?
    if form.validate_on_submit():
        # TODO
        #  1) 유저조회
        #  2) 존재하는 유저인지 확인
        #  3) Password 정합확인
        #  4) 로그인 유지(Session)

        user_id = form.data.get('user_id')
        password = form.data.get('password')

        user = [user for user in USERS if user.user_id == user_id]
        if user:
            user = user[0]
            if not security.check_password_hash(user.password, password):
                flash('Password is not valid.')
            else:
                session['user_id'] = user_id
                return redirect(url_for('base.index'))
        else:
            flash('User Id is not exists.')
    else:
        flash_form_errors(form)
    return render_template(f'{NAME}/login.html', form=form)


@bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        user_id = form.data.get('user_id')
        user_name = form.data.get('user_name')
        password = form.data.get('password')
        repassword = form.data.get('repassword')

        user = [user for user in USERS if user.user_id == user_id]
        if user:
            flash('User Id is already exists.')
            return redirect(request.path)
        else:
            USERS.append(
                User(
                    user_id=user_id,
                    user_name=user_name,
                    password=security.generate_password_hash(password)
                )
            )
            session['user_id'] = user_id
            return redirect(url_for('base.index'))
    else:
        flash_form_errors(form)
    return render_template(f'{NAME}/register.html', form=form)


@bp.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for(f'{NAME}.login'))


def flash_form_errors(form):
    for k, v in form.errors.items():
        for error in v:
            flash(error)