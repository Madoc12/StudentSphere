from student_data import app, db
import student_data.routes
# from student_data.models import Teacher, Student
# from flask_login import current_user


if __name__ == "__main__":
    app.run(debug=True, port=8000)