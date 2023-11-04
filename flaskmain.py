from flask import Flask, render_template, url_for
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
"""
@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html", title = "Home")

@app.route("/pricing")
def pricing():
    return render_template("pricing.html", title ="Pricing")

@app.route("/faqs")
def fqs():
    return render_template("faqs.html", title ="FAQs")

@app.route("/contact")
def contact():
    return render_template("contact.html", title ="Contact")

@app.route("/signin")
def signin():
    form = LoginForm()
    return render_template("signin.html", title ="Sign In", form = form)

@app.route("/register")
def registerp():
    form = RegistrationForm()
    return render_template("register.html", title ="Register", form = form)



if __name__ == "__main__":
    app.run(debug=True)
