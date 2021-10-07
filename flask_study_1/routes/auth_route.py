from flask import Blueprint, render_template, flash
from forms.auth_form import LoginForm, RegisterForm

NAME = 'auth'
bp = Blueprint(NAME, __name__, url_prefix='/auth')


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

        return f'{user_id}, {password}'
    else:
        # TODO: Error
        pass
    return render_template(f'{NAME}/login.html', form=form)


@bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        user_id = form.data.get('user_id')
        user_name = form.data.get('user_name')
        password = form.data.get('password')
        repassword = form.data.get('repassword')

        return f'{user_id}, {user_name}, {password}, {repassword}'
    else:
        pass
    return render_template(f'{NAME}/register.html', form=form)


@bp.route('/logout')
def logout():
    return 'LogOut'
