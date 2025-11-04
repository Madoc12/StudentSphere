from student_data import app, db
import student_data.routes
from student_data.models import Teacher, Student


if __name__ == "__main__":
    # Create all database tables before starting the server
    with app.app_context():
        db.create_all()
        print("Database tables created/verified successfully.")

    # with app.app_context():
        # user = Teacher.query.filter_by(username="madoc")
        # print(user)
           
    #     teachers = Teacher.query.all()
    #     if teachers == []:
    #         print("Empty")
    #     else:
    #         for teacher in teachers:
    #             print(teacher.username)
    app.run(debug=True, port=8000)