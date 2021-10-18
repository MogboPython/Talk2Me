from flask import Flask, render_template
from flask_wtf import form
from wtform_fields import *

#Configure App
app = Flask(__name__)
app.secret_key = 'password'

@app.route("/", methods = ["GET","POST"])
def index():

    reg_form = RegistrationForm()
    if reg_form.validate_on_submit():
        return 'It works'

    return render_template("index.html", form = reg_form)

if __name__ == "__main__":
    app.run(debug=True)