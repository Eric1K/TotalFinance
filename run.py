from flaskmain import app

""" ### IMPORTANT INFORMATION ###
To run:
python -m flask --app flaskmain run

### Run with making changes: ###
python -m flask --app flaskmain run --debug
npx tailwindcss -i ./static/css/input.css -o ./static/css/output.css --watch
OR press the run button in visual studio code

### Installations: ###
pip install Flask
pip install flask-wtf
pip install flask-sqlalchemy

other libraries:
flowcharts: https://flowbite.com/docs/plugins/charts/
apexcharts: https://apexcharts.com/docs/installation/#
https://tabler-icons.io/

### database ###
python
from flaskmain import app, db
app.app_context().push()
db.create_all()

### creating a user ###
from flaskmain.models import Users, updateNetWorth
user_1 = Users(name = "Bob", email = "bob@example.com", password = "password")
db.session.add(user_1)
user_2 = Users(name = "Bob2", email = "bob2@example.com", password = "password2")
db.session.add(user_2)
db.session.commit()
Users.query.all()
Users.query.first()
Users.query.filter_by(name = "Bob").first()

user = Users.query.filter_by(name = "Bob").first()
user.id
user = Users.query.get(2)

user = Users.query.filter_by(email = "bob@example.com").first()
user.name = "jeff"

Code snippets:
{% if current_user.is_authentiacted %} stuff here
Welcome, {% for dat in data %}{{dat.name}}{% endfor %} overview.html original welcome
"""



if __name__ == "__main__":
    app.run(debug=True)


#TODO: add phone number bod, etc to database
