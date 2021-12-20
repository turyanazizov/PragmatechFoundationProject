from os import name
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

class About(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_text = db.Column(db.Text)
    second_text = db.Column(db.Text)

class Resume(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    experience_title = db.Column(db.String(100))
    experience_info = db.Column(db.String(100))
    experience_content = db.Column(db.Text)
    education_title = db.Column(db.String(100))
    education_info = db.Column(db.String(100))
    education_content = db.Column(db.Text)

class Portfolio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    link = db.Column(db.Text)
    portfolio_title = db.Column(db.String(50))
    portfolio_detail = db.Column(db.String(50))
    photo = db.Column(db.String(200))

class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    blog_title = db.Column(db.String(50))
    blog_detail = db.Column(db.String(50))
    photo = db.Column(db.String(200))