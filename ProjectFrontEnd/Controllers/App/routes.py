# Controllers/App/routes.py
from flask import render_template,request,redirect
from start import app

@app.route('/')
def index():
    return render_template('App/index.html')

@app.route('/about')
def about():
    return render_template('App/about.html')

@app.route('/blog')
def blog():
    return render_template('App/blog.html')

@app.route('/contact')
def contact():
    return render_template('App/contact.html')

@app.route('/portfolio')
def portfolio():
    return render_template('App/portfolio.html')

@app.route('/resume')
def resume():
    return render_template('App/resume.html')