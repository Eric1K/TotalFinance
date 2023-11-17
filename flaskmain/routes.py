from flask import Flask, render_template, url_for, flash, redirect, request
from flaskmain import app, db, bcrypt
from flaskmain.models import Users, updateNetWorth
from flaskmain.forms import RegistrationForm, LoginForm
from flask_login import login_user, current_user, logout_user, login_required

data = [
    {
        'name': 'Bob Smith',
        'worth': '1000',
    },
]
@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html", title = "Home")

@app.route("/pricing")
def pricing():
    return render_template("pricing.html", title ="Pricing")

@app.route("/faqs")
def faqs():
    return render_template("faqs.html", title ="FAQs")

@app.route("/contact")
def contact():
    return render_template("contact.html", title ="Contact")

@app.route("/signin", methods = ["GET", "POST"])
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

@app.route("/register", methods = ["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        user = Users(name = form.name.data, email = form.email.data, password = hashed_password) #User method from models.py
        db.session.add(user)
        db.session.commit()
        print("Created Account")
        #might want to redirect to login
        flash(f"Account Created for {form.name.data}!", "success")
        return redirect(url_for("overview"))

    return render_template("register.html", title ="Register", form = form)

@app.route("/signout")
def signout():
    logout_user()
    return redirect(url_for("home"))

@app.route("/overview")
@login_required
def overview():
    return render_template("overview.html", title ="Overview", data = data)

@app.route("/budget")
@login_required
def budget():
    return render_template("budget.html", title ="Budget")

@app.route("/investing")
@login_required
def investing():
    return render_template("investing.html", title ="Investing")

@app.route("/financialplan")
@login_required
def financialplan():
    return render_template("financialplan.html", title ="Financial Plan")

@app.route("/settings")
@login_required
def settings():
    return render_template("settings.html", title ="Settings")