from flaskmain import application

""" ### IMPORTANT INFORMATION ###
To run:
python -m flask --app flaskmain run

### Run with making changes: ###
python -m flask --app flaskmain run --debug
npx tailwindcss -i ./flaskmain/static/css/input.css -o ./flaskmain/static/css/output.css --watch
OR press the run button in visual studio code

### Installations: ###
pip install Flask
pip install flask-wtf
pip install flask-sqlalchemy
pip install flask_bcrypt
pip install flask_login
pip install email_validator

other libraries:
flowcharts: https://flowbite.com/docs/plugins/charts/
apexcharts: https://apexcharts.com/docs/installation/#
https://tabler-icons.io/

### database ###
python
from flaskmain import application, db
application.app_context().push()
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

Users.query.filter_by(name = "jeff").delete()
Users.query.filter_by(email = "bob@example.com").delete()

Delete all:
db.session.query(Users).delete()
db.session.commit()

Code snippets:
{% if current_user.is_authentiacted %} stuff here
Welcome, {% for dat in data %}{{dat.name}}{% endfor %} overview.html original welcome
"""



if __name__ == "__main__":
    application.run(debug=True)
    #application.run(debug=False)
    #application.run(host='0.0.0.0', port=5000)


#TODO: add phone number bod, etc to database
#pip freeze > requirements.txt
#https://www.youtube.com/watch?v=dhHOzye-Rms
