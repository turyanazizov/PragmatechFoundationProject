# Controllers/Login/routes.py
from flask import render_template,request,redirect
from start import app

@app.route('/admin',methods=["GET","POST"])
def admin():
    from database.models import Login
    from start import db
    loggedUser=Login.query.get(1)
    if request.method=='POST':
        if request.form['username']==loggedUser.username and request.form['password']==loggedUser.password:
            loggedUser.logged=1
            db.session.commit()
            return redirect('/admin/index')
        else:
            return redirect('/admin')

    return render_template('Login/login.html')

@app.route('/logout')
def logout():
    from database.models import Login
    from start import db
    loggedUser=Login.query.get(1)
    loggedUser.logged=0
    db.session.commit()
    return redirect('/admin')
