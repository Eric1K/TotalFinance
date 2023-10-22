from flask import Flask
app = Flask(__name__)
"""
Only run:
python -m flask --app flaskmain run

Run with making changes:
python -m flask --app flaskmain run --debug
"""
@app.route("/")
@app.route("/home")
def hello_world():
    return "<h1>Hello0s, World!</h1>"

@app.route("/about")
def about():
    return "<h1>About World!</h1>"


"""
if __name__ == "__main__":
    app.run(debug=True)
"""