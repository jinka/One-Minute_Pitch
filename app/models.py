from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))

    def __repr__(self):
        return f'User {self.name}'

class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String(255))
    password_hash = db.Column(db.String(255))
    
    # S-Pitch
    date_joined = db.Column(db.DateTime,default=datetime.utcnow)
    pitches = db.relationship('Pitch',backref = 'user',lazy = "dynamic")
    comments = db.relationship('Comment',backref = 'user',lazy = "dynamic")

    # pitches = db.relationship('Pitch',backref = 'user',lazy = "dynamic")
    # comments = db.relationship('Comment',backref = 'user',lazy = "dynamic")
    # likes = db.relationship('Like',backref = 'user',lazy = "dynamic")
    # dislikes = db.relationship('Dislike',backref = 'user',lazy = "dynamic")    
    # E-Pitch

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)
            
    def __repr__(self):
        return f'User {self.username}'

# S Pitch
class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer,primary_key = True)
    comment = db.Column(db.String(1000))
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    pitch = db.Column(db.Integer,db.ForeignKey("pitches.id"))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls,pitch):
        comments = Comment.query.filter_by(pitch_id=pitch).all()
        return comments


class Pitch(db.Model):
    __tablename__ = 'pitches'

    id = db.Column(db.Integer,primary_key = True)
    pitch_title = db.Column(db.String)
    pitch_content = db.Column(db.String(1000))
    category = db.Column(db.String)
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    likes = db.Column(db.Integer)
    dislikes = db.Column(db.Integer)

    comments = db.relationship('Comment',backref =  'pitch_id',lazy = "dynamic")

    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_pitches(cls,category):
        pitches = Pitch.query.filter_by(category=category).all()
        return pitches

    @classmethod
    def get_pitch(cls,id):
        pitch = Pitch.query.filter_by(id=id).first()

        return pitch

    @classmethod
    def count_pitches(cls,uname):
        user = User.query.filter_by(username=uname).first()
        pitches = Pitch.query.filter_by(user_id=user.id).all()

        pitches_count = 0
        for pitch in pitches:
            pitches_count += 1

        return pitches_count

# class Pitch(db.Model):
#     __tablename__= 'pitches'

#     id = db.Column(db.Integer,primary_key = True)
#     pitch_title = db.Column(db.String())
#     content = db.Column(db.String())
#     category = db.Column(db.String())
#     posted = db.Column(db.DateTime,default=datetime.utcnow)

#     author = db.Column(db.Integer,db.ForeignKey("users.id"))

#     comments = db.relationship('Comment',backref = 'pitch',lazy = "dynamic")
#     likes = db.relationship('Like',backref = 'pitch',lazy = "dynamic")
#     dislikes = db.relationship('Dislike',backref = 'pitch',lazy = "dynamic")

#     def save_pitch(self):
#         db.session.add(self)
#         db.session.commit()


#     @classmethod
#     def get_pitch(cls,id):
#         pitches = Pitch.query.filter_by(id=id).all()
#         return pitches

#     @classmethod
#     def get_all_pitches(cls):
#         pitches = Pitch.query.order_by('-id').all()
#         return pitches

#     def __repr__(self):
#         return f'Pitch {self.pitch_title}'


# class Comment(db.Model):
#     __tablename__='comments'

#     id = db.Column(db.Integer,primary_key=True)
#     comment_content = db.Column(db.String())
#     pitch_id = db.Column(db.Integer,db.ForeignKey('pitches.id'))
#     user_id = db.Column(db.Integer,db.ForeignKey('users.id'))

#     def save_comment(self):
#         db.session.add(self)
#         db.session.commit()

#     @classmethod
#     def get_comments(cls,id):
#         comments = Comment.query.filter_by(pitch_id=id).all()
#         return comments

#     @classmethod
#     def get_all_comments(cls,id):
#         comments = Comment.query.order_by('-id').all()
#         return comments
#E-Pitch


