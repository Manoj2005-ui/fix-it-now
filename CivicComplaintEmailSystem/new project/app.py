from flask import Flask,render_template
from flask import request, redirect, url_for, flash

app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    username = db.Column(db.String, primary_key=True)
    name=db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    role=db.Column(db.String(20), nullable=False)  # 'user' or 'admin'


class Complaint(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(150), nullable=False)
    department = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(20), default="Pending")
    image= db.Column(db.String(100000000))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///complaints.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '23232323232323'
db.init_app(app)
@app.route('/') 
def login():
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        role = 'user'  # Default role is 'user'
        if not username or not name or not email or not password:
            flash('All fields are required!', 'danger')
            return redirect(url_for('register'))
        new_user = User(username=username, name=name, email=email, password=password, role=role)
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful! Please log in.', 'success')
    return render_template('register.html')

@app.route('/user_dashboard')
def user_dashboard():
    return render_template('dashboard.html')


@app.route('/admin')
def complaint():
    return render_template('admin_dashboard.html')    



if __name__ == '__main__':
    app.run(debug=True, port=5000)