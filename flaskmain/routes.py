from flask import Flask, render_template, url_for, flash, redirect, request
from flaskmain import application, db, bcrypt
from flaskmain.models import Users, updateNetWorth
from flaskmain.forms import RegistrationForm, LoginForm
from flask_login import login_user, current_user, logout_user, login_required

data = [
    {
        'name': 'Bob Smith',
        'worth': '1000',
    },
]
@application.route("/")
@application.route("/home")
def home():
    return render_template("index.html", title = "Home")

@application.route("/pricing")
def pricing():
    return render_template("pricing.html", title ="Pricing")

@application.route("/faqs")
def faqs():
    return render_template("faqs.html", title ="FAQs")

@application.route("/contact")
def contact():
    return render_template("contact.html", title ="Contact")

@application.route("/signin", methods = ["GET", "POST"])
def signin():
    if current_user.is_authenticated:
        print("Already Logged In")
        return redirect(url_for("overview"))
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get("next")
            return redirect(next_page) if next_page else redirect(url_for("overview"))
        else:
            flash("Login Unsuccessful. Please check email and password.", "danger")
    return render_template("signin.html", title ="Sign In", form = form)

@application.route("/register", methods = ["GET", "POST"])
def register(): 
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        user = Users(name = form.name.data, email = form.email.data, password = hashed_password) #User method from models.py
        db.session.add(user)
        db.session.commit()
        print("Created Account")
        #might want to redirect to login

        login_user(user)
        
        flash(f"Account Created for {form.name.data}!", "success")
        return redirect(url_for("overview"))

    return render_template("register.html", title ="Register", form = form)

@application.route("/signout")
def signout():
    logout_user()
    return redirect(url_for("home"))

@application.route("/introduction")
def introduction():
    return render_template("introduction.html", title ="Introduction")

@application.route("/launch")
def launch():
    return render_template("launch.html", title ="Launch", data = data)

@application.route("/overview")
@login_required
def overview():
    return render_template("overview.html", title ="Overview", data = data)

@application.route("/budget")
@login_required
def budget():
    return render_template("budget.html", title ="Budget")

@application.route("/investing")
@login_required
def investing():
    return render_template("investing.html", title ="Investing")

@application.route("/financialplan")
@login_required
def financialplan():
    return render_template("financialplan.html", title ="Financial Plan")

@application.route("/settings")
@login_required
def settings():
    return render_template("settings.html", title ="Settings")