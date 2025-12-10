from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_wtf import CSRFProtect
from dotenv import load_dotenv
from google import genai

load_dotenv()

app = Flask(__name__)
client = genai.Client()
# Use a stable secret key; in production set SECRET_KEY via environment variable
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-change-me')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
db = SQLAlchemy(app)

bcrypt = Bcrypt(app)
login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.login_message_category = "danger"
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    # import locally to avoid circular imports at module import time
    from student_data.models import Teacher
    return Teacher.query.get(int(user_id))

# Initialize CSRF protection
csrf = CSRFProtect()
csrf.init_app(app)
app.config['WTF_CSRF_ENABLED'] = True

# Import routes at the end to avoid circular imports
from student_data import routes


