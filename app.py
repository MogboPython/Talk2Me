from flask import Flask, render_template, redirect, url_for, flash
from flask_wtf import form
from wtform_fields import *
from models import *
from flask_login import LoginManager, login_user, current_user, login_required, logout_user

#Configure App
app = Flask(__name__)
app.secret_key = 'password'

#Configure database
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://gaqsswswfjeipz:a2eefd3c917fb89e84fadccc358cd77f8ad859c06a2465e16652ca15c746150c@ec2-3-218-47-9.compute-1.amazonaws.com:5432/dcv7dg2kkk2kgp'
db = SQLAlchemy(app)

#Configure Flask Login
login = LoginManager(app)
login.init_app(app)

@login.user_loader
def load_user(id):

    return User.query.get(int(id))

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

        flash('Registered suceessfully. Please login.','success')
        return redirect(url_for('login'))

    return render_template("index.html", form = reg_form)

@app.route("/login", methods = ["GET","POST"])
def login():
    login_form = LoginForm()

    #Allow Login if Validation Success
    if login_form.validate_on_submit():
        user_object = User.query.filter_by(username = login_form.username.data).first()
        login_user(user_object)
        return redirect(url_for('chat'))
    
    return render_template('login.html', form = login_form)

@app.route("/chat", methods = ["GET", "POST"])
def chat():
    if not current_user.is_authenticated:
        flash('Please login', 'danger')
        return redirect(url_for('login'))
    return "Chat with Me!"

@app.route("/logout", methods = ["GET"])
def logout():
    logout_user()
    flash('You have logged out successfully', 'success')
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=True)