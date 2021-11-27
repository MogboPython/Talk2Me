# Chat App Using Flask-SocketIO & Deployed in Heroku

## Introduction
This is a chat application, implemented using Flask-SocketIO with both the database (PostgreSQL) and the app deployed in Heroku. It also has user registration and authentication functionalities.
I followed 
<a href="https://www.youtube.com/playlist?list=PLlLKnYbrXi_rFrzsPa0NxZayHrT52a777"><img src="https://github.com/sandeepsudhakaran/rchat-app/blob/master/static/images/rchat-playlist.png" alt="Watch Code Along Series"></a>
A 13-part video series where he built this app from scratch.


## Files in the program
- **application.py**: This is the main app file and contains both the registration/login page logic and the Flask-SocketIO backend for the app.
- **models.py**: Contains Flask-SQLAlchemy models used for user registration and login in application.py
- **wtform_fields.py**: Contains the classes for WTForms/Flask-WTF and the custom validators for the fields
- **create.py**: optional file only required if repo is to be cloned. *See 'Usage' section below.*
- **Procfile**: file required for Heroku
- **requirements.txt**: list of Python packages installed (also required for Heroku)
- **templates/**: folder with all HTML files
- **static/**: for with all JS scripts and CSS files


## Usage
### Run app
Use [the link to the production server](https://talk2me-app.herokuapp.com/) directly.

### Clone/Modify app
1. Modify application.py to replace the secret key *(i.e. os.environ.get('SECRET'))* with a secret key of your choice and the database link *(i.e. os.environ.get('DATABASE_URL'))* with the link to your own database.

    The two lines to be edited in application.py are shown below:
```python
app.secret_key=os.environ.get('SECRET')
app.config['SQLALCHEMY_DATABASE_URI']=os.environ.get('DATABASE_URL')
```

