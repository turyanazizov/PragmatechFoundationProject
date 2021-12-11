from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app=Flask(__name__,template_folder='Views')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
from Controllers.Admin.routes import *
from Controllers.App.routes import *
from Controllers.Login.routes import *

if __name__=='__main__':
    app.run(debug=True)