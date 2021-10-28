from flask import Flask, render_template, redirect, url_for
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

    #Updated database if Validation successs
    if reg_form.validate_on_submit():
        username = reg_form.username.data
        password = reg_form.password.data

        #Hash Password
        hashed_pass = pbkdf2_sha256.hash(password)
        
        #Add user to the database
        user = User(username = username, password = hashed_pass)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template("index.html", form = reg_form)

@app.route("/login", methods = ["GET","POST"])
def login():
    login_form = LoginForm()

    #Allow Login if Validation Success
    if login_form.validate_on_submit():
        return "Logged In Successfully"
    
    return render_template('login.html', form = login_form)

if __name__ == "__main__":
    app.run(debug=True)