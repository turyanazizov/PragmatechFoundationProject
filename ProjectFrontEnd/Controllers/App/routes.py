# Controllers/App/routes.py
from flask import render_template,request,redirect
from start import app
from database.models import *
import datetime
@app.route('/')
def index():
    return render_template('App/index.html')

@app.route('/about')
def about():
    return render_template('App/about.html')

@app.route('/blog')
def blog():
    return render_template('App/blog.html')

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
        render_template('admin/control-inbox.html',messages=messages)
        return redirect('/contact')
    else:
        return render_template('app/contact.html')

@app.route('/portfolio')
def portfolio():
    return render_template('App/portfolio.html')

@app.route('/resume')
def resume():
    return render_template('App/resume.html')