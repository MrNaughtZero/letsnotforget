from app.db import db
import hashlib
from hashlib import sha256

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(500), nullable=False)
    pw = db.Column(db.String(500), nullable=False)

    def add(self):
        db.session.add(self)
        db.session.commit()

    def get_id(self):
        return self.id
    
    def is_authenticated(self):
        return True

    def is_active(self):
        return True
    
    def is_anonymous(self):
        return False

    def checkIfRegistered(self, email):
        return self.query.filter_by(email=email).first()

    @staticmethod
    def hashPassword(password):
        return sha256(password.encode('utf8')).hexdigest()
    

class List(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userID = db.Column(db.String(10), nullable=False)
    text = db.Column(db.String(300), nullable=False)

    def add(self):
        db.session.add(self)
        db.session.commit()
        return str(self.id)

    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()

    def fetchAll(self, user):
        return self.query.filter_by(userID=user).all()

    def fetchItem(self, user, text):
        return self.query.filter_by(userID=user, text=text).first()