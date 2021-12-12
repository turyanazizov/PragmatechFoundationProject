# Controllers/Admin/routes.py
from flask import render_template,request,redirect
from start import app
from database.models import *

@app.route('/admin/index')
def admin_index():
    from database.models import Login
    from start import db
    loggedUser=Login.query.get(1)
    if loggedUser.logged==1:
        return render_template('Admin/index.html')
    else:
        return redirect('/admin')

@app.route('/admin/control-home')
def admin_home():
    from database.models import Login
    from start import db
    loggedUser=Login.query.get(1)
    if loggedUser.logged==1:
        return render_template('Admin/control-home.html')
    else:
        return redirect('/admin')

@app.route('/admin/control-about')
def admin_about():
    from database.models import Login
    from start import db
    loggedUser=Login.query.get(1)
    if loggedUser.logged==1:
        return render_template('Admin/control-about.html')
    else:
        return redirect('/admin')

@app.route('/admin/control-resume')
def admin_resume():
    from database.models import Login
    from start import db
    loggedUser=Login.query.get(1)
    if loggedUser.logged==1:
        return render_template('Admin/control-resume.html')
    else:
        return redirect('/admin')

@app.route('/admin/control-portfolio')
def admin_portfolio():
    from database.models import Login
    from start import db
    loggedUser=Login.query.get(1)
    if loggedUser.logged==1:
        return render_template('Admin/control-portfolio.html')
    else:
        return redirect('/admin')

@app.route('/admin/control-blog')
def admin_blog():
    from database.models import Login
    from start import db
    loggedUser=Login.query.get(1)
    if loggedUser.logged==1:
        return render_template('Admin/control-blog.html')
    else:
        return redirect('/admin')

@app.route('/admin/control-contact',methods=['GET','POST'])
def admin_contact():
    from database.models import Login
    from start import db
    loggedUser=Login.query.get(1)
    if loggedUser.logged==1:
        return render_template('Admin/control-contact.html')
    else:
        return redirect('/admin')

@app.route('/admin/control-inbox')
def admin_inbox():
    from database.models import Login
    from start import db
    loggedUser=Login.query.get(1)
    if loggedUser.logged==1:
        messages=Message.query.all()
        return render_template('Admin/control-inbox.html',messages=messages)
    else:
        return redirect('/admin')

@app.route('/admin/control-inbox/delete/<int:id>',methods=['GET','POST'])
def delete(id):

    from database.models import Login
    from start import db
    loggedUser=Login.query.get(1)
    if loggedUser.logged==1:
        message=Message.query.get(id)
        db.session.delete(message)
        db.session.commit()
        return redirect('/admin/control-inbox')
    else:
        return redirect('/admin')

@app.route('/admin/control-inbox/update/<int:id>',methods=['GET','POST'])
def update(id):
    from database.models import Login
    from start import db
    message=Message.query.get(id)
    loggedUser=Login.query.get(1)
    if loggedUser.logged==1:
        if request.method=="POST":
            message.username=request.form['fullname']
            message.email=request.form['email']
            message.text=request.form['text']
            db.session.commit()
            return redirect('/admin/control-inbox')
    return render_template('Admin/update.html',message=message)
    
