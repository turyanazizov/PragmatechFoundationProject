# Controllers/Admin/routes.py
from flask import render_template,request,redirect
from start import app

@app.route('/admin')
def admin_index():
    return render_template('Admin/index.html')