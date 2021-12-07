from flask import Flask


app=Flask(__name__,template_folder='Views')

from Controllers.Admin.routes import *
from Controllers.App.routes import *

if __name__=='__main__':
    app.run(debug=True)

