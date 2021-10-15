from flask_study_1 import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(20), unique=True, nullable=False)
    user_name = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(300), nullable=False)

    @classmethod
    def fine_one_by_user_id(cls, user_id):
        return User.query.filter_by(user_id=user_id).first()
