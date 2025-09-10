from flask import render_template, request, redirect, url_for, session, Blueprint 

main_bp = Blueprint("main", __name__)

# ---------- Routes ----------
@main_bp.route('/')
def home():
    return render_template('index.html', logged_in=("user_id" in session))

@main_bp.route('/food')
def food():
    if "user_id" not in session:
        return redirect(url_for("auth.login"))
    return render_template('food.html')

@main_bp.route('/training')
def training():
    if "user_id" not in session:
        return redirect(url_for("auth.login"))
    return render_template('training.html')

@main_bp.route('/adopt')
def adopt():
    if "user_id" not in session:
        return redirect(url_for("auth.login"))
    return render_template('adopt.html')

@main_bp.route('/donate')
def donate():
    if "user_id" not in session:
        return redirect(url_for("auth.login"))
    return render_template('donate.html')































# from flask import Flask, render_template, request, redirect, url_for , session
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# app.secret_key = "supersecretkey" 

# app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///users.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key =True)
#     user = db.Column(db.String(120), nullable = False)
#     email = db.Column(db.String(200), nullable = False)
#     password = db.Column(db.String(120), nullable = False)

# with app.app_context():
#     db.create_all()
# # ---------- Routes ----------
# @app.route('/')
# def home():
#     logged_in = "user_id" in session
#     return render_template('index.html' , logged_in=('user_id' in session))

# @app.route('/food')
# def food():
#     if "user_id" not in session:
#         return redirect(url_for("login"))
#     return render_template('food.html')

# @app.route('/training')
# def training():
#     if "user_id" not in session:
#         return redirect(url_for("login"))
#     return render_template('training.html')

# @app.route('/adopt')
# def adopt():
#     if "user_id" not in session:
#         return redirect(url_for("login"))
#     return render_template('adopt.html')

# @app.route('/donate')
# def donate():
#     if "user_id" not in session:
#         return redirect(url_for("login"))
#     return render_template('donate.html')

# @app.route('/login', methods = ['GET','POST'])
# def login():
#     if request.method == "POST":
#         email = request.form['email']
#         password = request.form['password']

#         user = User.query.filter_by(email=email, password=password).first()

#         if user:
#             session["user_id"] = user.id
#             session["username"] = user.user
#             return redirect(url_for("home"))
#         else:
#             return "Invalid email or password."
#     return render_template('login.html')


# @app.route("/signup", methods=["GET", "POST"])
# def signup():
#     if request.method == "POST":
#         user = request.form["username"]
#         email = request.form["email"]
#         password = request.form["password"]

#         new_user = User(user=user, email=email, password=password)
#         db.session.add(new_user)
#         db.session.commit()
#         return redirect(url_for("login"))

#     return render_template("signup.html")

# @app.route("/logout", methods=['POST'])
# def logout():
#     session.clear()
#     return redirect(url_for("home"))







# # @app.route("/users")
# # def users():
# #     all_users = User.query.all()
# #     return "<br>".join([f"{u.user} - {u.email} - {u.password}" for u in all_users])


# # ---------- Run ----------
# if __name__ == '__main__':
#     app.run(debug=True)
