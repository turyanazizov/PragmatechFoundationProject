from start import db

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80),nullable=False)
    email = db.Column(db.String(120),nullable=False)
    text = db.Column(db.String(80), nullable=False)
    date = db.Column(db.DateTime)
    
class Login(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(50))
    logged = db.Column(db.Boolean)
