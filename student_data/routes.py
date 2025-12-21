from student_data import app, db, client
from flask import render_template, request, flash, redirect, url_for, jsonify, session
from student_data.models import Teacher, Student
from flask_login import login_user, logout_user, current_user, login_required
from google.genai import types

@app.route('/')
@login_required
def home():
    students=Student.query.filter_by(teacher_id=current_user.id).all()
    total_grade = sum(student.grade for student in students if student.grade is not None)
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return render_template('dashboard_partial.html', students_number=len(students), user=current_user.name, total_grade=total_grade)
    return render_template('base.html')

@app.route('/students', methods=["GET", "POST"])
@login_required
def students():
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return render_template('students.html')
    if request.method == "POST":
        try:
            age_val = int(request.form.get("age")) if request.form.get("age") not in (None, "") else None
        except (ValueError, TypeError):
            age_val = None
        new_student = Student(
            name=request.form.get("name"),
            age=age_val,
            teacher_id = current_user.id
        )
        db.session.add(new_student)
        db.session.commit()
        flash("Student added successfully", category="success")

    return render_template('base.html', title='Students')

@app.route('/edit_students')
@login_required
def edit_students():
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return render_template('edit_students.html', students=Student.query.filter_by(teacher_id=current_user.id).all())
    return render_template('edit_students.html')

@app.route('/login' ,methods=["GET", "POST"])
def login():
    if request.method == "POST":
        teacher = Teacher.query.filter_by(username=request.form.get("username")).first()

        if teacher and teacher.check_password(attempted_password=request.form.get("password")):
            login_user(teacher)
            flash("Login successful", category="success")
            return redirect(url_for("home"))
        else:
            flash("Username or password is incorrect.", category="danger")        

    return render_template("login.html")

@app.route("/chat")
@login_required
def chat():
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return render_template('chat.html')
    return render_template('chat.html')

@app.route('/chatbot', methods=['POST'])
def chatbot():

    data = request.get_json(silent=True)
    # If request body is missing or not JSON
    if not data or "message" not in data:
        return jsonify({"error": "Invalid request. Expected JSON with a 'message' field."}), 400
    action = data.get("action")
    user_message = data["message"]
    session["ai"] = False
    
    # Initialize state
    if "chat_state" not in session:
        session["chat_state"] = {}

    state = session["chat_state"]
    #Initialize AI mode
    if action == "generative_ai":
        session["ai"] = True

        user_message = data.get("message")  # always extract safely

        if not user_message:
            return jsonify({"reply": "AI mode activated! Send a message to start chatting."})

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=[user_message],
            config=types.GenerateContentConfig(
                system_instruction="You are a teacher assistant helping the teacher with managing class activities."
            )
        )

        ai_reply = response.text
        print(f"ai_reply: {ai_reply}")
        return jsonify({"reply": ai_reply})
    elif action == "exit_ai":
        session["ai"] == False
        return jsonify({"reply": "Exited AI assistant"})
    elif action == "add_student":
        session["chat_state"] = {"step": "ask_name"}
        return jsonify({"reply": "Sure! What’s the student's name?"})
    
    # Add student conversation flow for chatbot
    
    if state.get("step") == "ask_name":
        state["name"] = user_message
        state["step"] = "ask_age"
        session.modified = True
        return jsonify({"reply": f"Got it. What’s {user_message}'s age?"})
    
    elif state.get("step") == "ask_age":
        state["age"] = int(user_message)
        new_student = Student(
            name=state["name"],
            age=state["age"],
            teacher_id = current_user.id
        )
        db.session.add(new_student)
        db.session.commit()
        session.pop("chat_state")  # reset conversation
        return jsonify({"reply": f"✅ {new_student.name} added successfully!"})
    
    # View all students
    elif action == "view_students":
        students = Student.query.all()
        if not students:
            return jsonify({"reply": "No students found."})
        names = "\n".join([s.name for s in students])
        return jsonify({"reply": f"Here are all students:\n{names}"})
    
    if user_message and session["chat_state"] == {} and session["ai"] == False:
        user_message = data["message"].lower()
        if "add student" in user_message:
            return jsonify({"reply": "Sure! Cick 'Add Student' button to add a new student."})
        elif "hello" in user_message or "hi" in user_message:
            return jsonify({"reply": "Hey there! How can I assist you today?"})
        elif "view students" in user_message:
            students = Student.query.all()
            if not students:
                return jsonify({"reply": "No students found in the database."})
        
            student_list = "\n".join([f"{s.name}, Age: {s.age}" for s in students])
            return jsonify({"reply": f"Here are all students:\n{student_list}"})

        else:
            return jsonify({"reply": "I'm not sure how to handle that yet — try saying 'add student' or 'view students'."})


    

    

    


        

    return jsonify({"reply": "Didnt work"})
  
    
    




 

    



@app.route("/sign_up", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        user = request.form.get("username")
        user_exists = Teacher.query.filter_by(username=user).first()
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")
        if user_exists:
            return render_template("signup.html")
        if password1 == password2:

            new_teacher = Teacher(
                username = request.form.get("username"),
                name = request.form.get("name"),
                email = request.form.get("email"),
                password = request.form.get("password1")
            )
            db.session.add(new_teacher)
            db.session.commit()
            login_user(new_teacher)
            flash("Account created successfully.", category="success")
            return redirect("/")
        else:
            return render_template("signup.html")
    elif request.method == "GET":
        return render_template("signup.html")
    
@app.route('/logout')
def logout():
    logout_user()
    flash("You have been logged out.", category="info")
    return redirect(url_for('login'))


@app.route("/update_student/<int:student_id>", methods=["POST"])
@login_required
def update_student(student_id):
    data = request.get_json()
    student = Student.query.get(student_id)
    if not student:
        return jsonify({"error": "Student not found"}), 404
    try:
        student.name = data["name"]
        student.age = data["age"]
        student.english = data["english"]
        student.math = data["math"]
        student.grade = (int(data["english"]) + int(data["math"])) / 2
        db.session.commit()

        return jsonify({
            "message": "Updated successfully",
            "grade": student.grade
        })
    except ValueError:
        student.name = data["name"]
        student.age = data["age"]
        student.english = data["english"]
        student.math = data["math"]
        db.session.commit()
        return jsonify({"message": "Enter all fields"})

    

@app.route('/delete_student/<int:student_id>', methods=['POST'])
@login_required
def delete_student(student_id):
    student = Student.query.get_or_404(student_id)
    db.session.delete(student)
    db.session.commit()
    return jsonify({"message": "Student deleted successfully"}), 200