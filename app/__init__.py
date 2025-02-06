from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt  # Import Bcrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'

# Initialize extensions
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)  # Initialize Bcrypt
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Import routes and models at the end to avoid circular imports
from app import routes, models