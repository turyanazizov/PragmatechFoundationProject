# Controllers/Admin/routes.py
from flask import render_template,request,redirect
from Controllers.App.routes import resume
from start import app
from database.models import *
import os

@app.route('/admin/index')
def admin_index():
    from database.models import Login
    from start import db
    loggedUser=Login.query.get(1)
    if loggedUser.logged==1:
        return render_template('Admin/index.html')
    else:
        return redirect('/admin')

@app.route('/admin/control-resume',methods=['GET','POST'])
def admin_resume():
    from database.models import Login
    from database.models import Resume
    from start import db
    loggedUser=Login.query.get(1)
    if loggedUser.logged==1:
        resumes=Resume.query.all()
        if request.method=="POST":
            _exptitle=request.form['exptitle']
            _expdetail=request.form['expdetail']
            _expcontent=request.form['expcontent']
            _edutitle=request.form['edutitle']
            _edudetail=request.form['edudetail']
            _educontent=request.form['educontent']
            resume=Resume(experience_title=_exptitle,experience_info=_expdetail,experience_content=_expcontent,education_title=_edutitle,education_info=_edudetail,education_content=_educontent)
            db.session.add(resume)
            db.session.commit()
            render_template('App/resume.html',resumes=resumes)
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

@app.route('/admin/control-blog',methods=['GET','POST'])
def admin_blog():
    from database.models import Login
    from database.models import Blog
    from start import db
    loggedUser=Login.query.get(1)
    if loggedUser.logged==1:
        blogs=Blog.query.all()
        if request.method=="POST":
            file=request.files['photo']
            _title=request.form['title']
            _detail=request.form['detail']
            _photo=file.filename
            file.save(os.path.join('static/uploads',_photo))
            blog=Blog(blog_title=_title,blog_detail=_detail,photo=_photo)
            db.session.add(blog)
            db.session.commit()
            return redirect('/admin/control-blog')
        render_template('App/blog.html',blogs=blogs)
        return render_template('Admin/control-blog.html',blogs=blogs)
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

@app.route('/admin/control-about/delete/<int:id>',methods=['GET','POST'])
def delete_about(id):
    from database.models import Login
    from database.models import About
    from start import db
    loggedUser=Login.query.get(1)
    if loggedUser.logged==1:
        about=About.query.get(id)
        db.session.delete(about)
        db.session.commit()
        return redirect('/admin/control-about')
    else:
        return redirect('/admin')

@app.route('/admin/control-about',methods=['GET','POST'])
def update_about():
    from database.models import Login
    from database.models import About
    from start import db
    loggedUser=Login.query.get(1)
    if loggedUser.logged==1:
        about=About.query.get(1)     
        if request.method=="POST":          
            about.first_text=request.form['firstcontent']
            about.second_text=request.form['secondcontent']
            db.session.commit()
            render_template('App/about.html',about=about)
            return render_template('Admin/control-about.html',about=about)
    return render_template('Admin/control-about.html',about=about)

@app.route('/admin/control-blog/delete/<int:id>',methods=['GET','POST'])
def delete_blog(id):
    from database.models import Login
    from database.models import Blog
    from start import db
    loggedUser=Login.query.get(1)
    if loggedUser.logged==1:
        blog=Blog.query.get(id)
        db.session.delete(blog)
        db.session.commit()
        return redirect('/admin/control-blog')
    else:
        return redirect('/admin')