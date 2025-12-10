from student_data import db, login_manager # db comes from student_data.__init__.py
from student_data import bcrypt
from flask_login import UserMixin
import os

# Teacher Table
class Teacher(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    # store the hashed password in a separate column to avoid shadowing the property
    password_hash = db.Column(db.String(200), nullable=False)

    # One teacher has many students
    students = db.relationship('Student', backref='teacher', lazy=True)
    @property
    def password(self):
        raise AttributeError("Password is write-only")

    @password.setter
    def password(self, plain_text_password):
        # store the bcrypt hash in password_hash to avoid recursion
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    def check_password(self, attempted_password):
        # If password_hash is missing or not a valid bcrypt hash, return False
        if not self.password_hash:
            return False
        try:
            return bcrypt.check_password_hash(self.password_hash, attempted_password)
        except (ValueError, TypeError):
            # Invalid salt or bad hash format stored in DB; treat as authentication failure
            return False
        



# Student Table
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    grade = db.Column(db.Float, nullable=True)
    english = db.Column(db.Integer, nullable=True)
    math = db.Column(db.Integer, nullable=True)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teacher.id'), nullable=False)

    def __repr__(self):
        return f"<Student {self.name}, Age: {self.age}, Eng: {self.english}, Math: {self.math}>"

    
