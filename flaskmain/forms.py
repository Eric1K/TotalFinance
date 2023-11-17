from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, DateField
from wtforms.validators import DataRequired, Optional, Length, Email, EqualTo, ValidationError
from flaskmain.models import Users

class RegistrationForm(FlaskForm):
    name = StringField("Full Name", validators = [DataRequired()])
    email = StringField("Email Address", validators = [DataRequired(), Email()])
    password = PasswordField("Password", validators = [DataRequired()])
    confirm_password = PasswordField("Confirm Password", validators = [DataRequired(), EqualTo("password")])
    phone = StringField('Phone Number (Optional)', validators=[Optional()])
    birthday = DateField("Date of Birth", validators=[DataRequired()])
    
    submit = SubmitField("Create Account")

    def validate_email(self, email):
        #check if email is already registered
        user = Users.query.filter_by(email = email.data).first()
        if user:
            raise ValidationError("This email is already taken.")
        

class LoginForm(FlaskForm):
    email = StringField("Email Address", validators = [DataRequired(), Email()])
    password = PasswordField("Password", validators = [DataRequired()])
    remember = BooleanField("Remember Me")
    submit = SubmitField("Login")
