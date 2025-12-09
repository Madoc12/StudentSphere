from student_data import app, db
import student_data.routes
from student_data.models import Teacher, Student
from flask_login import current_user


if __name__ == "__main__":
    # Create all database tables before starting the server
    # with app.app_context():
    #     db.create_all()
    #     students=Student.query.filter_by(teacher_id=1).all()
    #     for student in students:
    #         if student.grade:
    #             print(f"{student.name}: {student.grade}")
    #     print("Database tables created/verified successfully.")

    # with app.app_context():
        # user = Teacher.query.filter_by(username="madoc")
        # print(user)
           
    #     teachers = Teacher.query.all()
    #     if teachers == []:
    #         print("Empty")
    #     else:
    #         for teacher in teachers:
                # print(teacher.username)
    app.run(debug=True, port=8000)