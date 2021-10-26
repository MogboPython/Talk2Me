from flask import Flask, render_template
from flask_wtf import form
from wtform_fields import *
from models import *

#Configure App
app = Flask(__name__)
app.secret_key = 'password'

#Configure database
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://gaqsswswfjeipz:a2eefd3c917fb89e84fadccc358cd77f8ad859c06a2465e16652ca15c746150c@ec2-3-218-47-9.compute-1.amazonaws.com:5432/dcv7dg2kkk2kgp'
db = SQLAlchemy(app)

@app.route("/", methods = ["GET","POST"])
def index():

    reg_form = RegistrationForm()
    if reg_form.validate_on_submit():
        username = reg_form.username.data
        password = reg_form.password.data
        
        #Add user to the database
        user = User(username = username, password = password)
        db.session.add(user)
        db.session.commit()
        return "Inserted into DB successfully!"

    return render_template("index.html", form = reg_form)

if __name__ == "__main__":
    app.run(debug=True)