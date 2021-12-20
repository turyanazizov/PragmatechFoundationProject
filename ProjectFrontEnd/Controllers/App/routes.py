# Controllers/App/routes.py
from flask import render_template,request,redirect
from start import app
from database.models import *
import datetime

@app.route('/')
def index():
    return render_template('App/index.html')

@app.route('/about',methods=['GET','POST'])
def about():
    about=About.query.get(1)
    return render_template('App/about.html',about=about)

@app.route('/blog',methods=['GET','POST'])
def blog():
    blogs=Blog.query.all()
    return render_template('App/blog.html',blogs=blogs)

@app.route('/contact',methods=['GET','POST'])
def contact():
    messages=Message.query.all()
    if request.method=='POST':
        _fullname=request.form['fullname']
        _email=request.form['email']
        _text=request.form['text']
        _date=datetime.datetime.now()
        message=Message(username=_fullname,email=_email,text=_text,date=_date)
        db.session.add(message)
        db.session.commit()
        render_template('Admin/control-inbox.html',messages=messages)
        return redirect('/contact')
    else:
        return render_template('App/contact.html')

@app.route('/portfolio',methods=['GET','POST'])
def portfolio():
    portfolios=Portfolio.query.all()
    return render_template('App/portfolio.html',portfolios=portfolios)

@app.route('/resume',methods=['GET','POST'])
def resume():
    resumes=Resume.query.all()
    return render_template('App/resume.html',resumes=resumes)