from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password_hash = db.Column(db.String(128))
    name = db.Column(db.String(120))
    email = db.Column(db.String(120), unique=True)
    photo = db.Column(db.String(200))
    date_joined = db.Column(db.DateTime, default=datetime.utcnow)

    profiles = db.relationship('Profile', backref='user', lazy=True)
    favourites = db.relationship('Favourite', backref='user', lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'name': self.name,
            'email': self.email,
            'photo': self.photo,
            'date_joined': self.date_joined.isoformat()
        }

class Profile(db.Model):
    __tablename__ = 'profiles'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id_fk = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    description = db.Column(db.String(255))
    parish = db.Column(db.String(100))
    biography = db.Column(db.Text)
    sex = db.Column(db.String(20))
    race = db.Column(db.String(50))
    birth_year = db.Column(db.Integer)
    height = db.Column(db.Float)
    fav_cuisine = db.Column(db.String(50))
    fav_colour = db.Column(db.String(50))
    fav_school_subject = db.Column(db.String(50))
    political = db.Column(db.Boolean)
    religious = db.Column(db.Boolean)
    family_oriented = db.Column(db.Boolean)

    def to_dict(self):
        return {
            'id': self.id,
            'user_id_fk': self.user_id_fk,
            'description': self.description,
            'parish': self.parish,
            'biography': self.biography,
            'sex': self.sex,
            'race': self.race,
            'birth_year': self.birth_year,
            'height': self.height,
            'fav_cuisine': self.fav_cuisine,
            'fav_colour': self.fav_colour,
            'fav_school_subject': self.fav_school_subject,
            'political': self.political,
            'religious': self.religious,
            'family_oriented': self.family_oriented
        }

class Favourite(db.Model):
    __tablename__ = 'favourites'

    id = db.Column(db.Integer, primary_key=True)
    user_id_fk = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    fav_user_id_fk = db.Column(db.Integer, nullable=False)  # user_id of the person being favourited
