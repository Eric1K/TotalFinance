from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "de1ec9c6bc343e6995d959526e2a3d93"

"""
Only run:
python -m flask --app flaskmain run

Run with making changes:
python -m flask --app flaskmain run --debug
npx tailwindcss -i ./static/css/input.css -o ./static/css/output.css --watch

installations:
pip install Flask
pip install flask-wtf

other libraries:
flowcharts: https://flowbite.com/docs/plugins/charts/
apexcharts: https://apexcharts.com/docs/installation/#
https://tabler-icons.io/

"""
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

@app.route("/signin")
def signin():
    form = LoginForm()
    return render_template("signin.html", title ="Sign In", form = form)

@app.route("/register", methods = ['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        print("yay")
        flash(f"Account Created for!", "success")
        return redirect(url_for("overview"))
    else:
        print("no2")
    
    return render_template("register.html", title ="Register", form = form)


@app.route("/overview")
def overview():
    return render_template("overview.html", title ="Overview")

@app.route("/budget")
def budget():
    return render_template("budget.html", title ="Budget")

@app.route("/investing")
def investing():
    return render_template("investing.html", title ="Investing")

@app.route("/financialplan")
def financialplan():
    return render_template("financialplan.html", title ="Financial Plan")

@app.route("/settings")
def settings():
    return render_template("settings.html", title ="Settings")

if __name__ == "__main__":
    app.run(debug=True)
