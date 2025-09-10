from flask import Blueprint, render_template, request, session, redirect, url_for, Flask
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User


auth_bp = Blueprint("auth",__name__)

@auth_bp.route("/login", methods =['GET','POST'])
def login():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            session["user_id"] = user.id
            session["user"] = user.user
            return redirect(url_for("main.home"))
        else:
            return "Invalid email or password."
    return render_template('login.html')

@auth_bp.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        user = request.form["user"]
        email = request.form["email"]
        password = request.form["password"]

        # Hash password
        hashed_pw = generate_password_hash(password)
        new_user = User(user=user, email=email, password=hashed_pw)
        
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("auth.login"))

    return render_template("signup.html")

@auth_bp.route("/logout" , methods=['POST'])
def logout():
    session.clear()
    return redirect(url_for("main.home"))
