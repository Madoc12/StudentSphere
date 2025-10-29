from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return render_template('index_partial.html')
    return render_template('base.html')

@app.route('/students')
def students():
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return render_template('students.html')
    return render_template('base.html', title='Students')

@app.route('/attendance')
def attendance():
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return render_template('attendance.html', partial=True)
    return render_template('attendance.html')

@app.route('/login')
def login():
    return render_template("login.html")


if __name__ == '__main__':
    app.run(debug=True)