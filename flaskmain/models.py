from flaskmain import db, login_manager
from datetime import datetime
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), unique = False, nullable = False)
    email = db.Column(db.String(120), unique = True, nullable = False)
    # image_file = db.Column(db.String(20), nullable = False, default = "default.png")
    password = db.Column(db.String(60), nullable = False)
    #posts = db.relationship('Post', backref = "username", lazy = True) multiple posts
    phone = db.Column(db.String(60), unique = True, nullable = False)
    dob = db.Column(db.String(60), nullable = False)

    def __repr__(self):
        return f"Users('{self.name}', '{self.email}','{self.password}','{self.phone}','{self.dob}')"

class updateNetWorth(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    networth = db.Column(db.Float, nullable = False)
    #user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    def __repr__(self):
        return f"updateNetWorth('{self.networth}')"
