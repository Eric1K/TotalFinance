from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, DateField, FloatField
from wtforms.validators import DataRequired, Optional, Length, Email, EqualTo, ValidationError
from flaskmain.models import Users

class RegistrationForm(FlaskForm):
    name = StringField("Full Name", validators = [DataRequired()])
    email = StringField("Email Address", validators = [DataRequired(), Email()])
    password = PasswordField("Password", validators = [DataRequired()])
    confirm_password = PasswordField("Confirm Password", validators = [DataRequired(), EqualTo("password")])
    phone = StringField('Phone Number', validators=[Optional()])
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

class AssetListForm(FlaskForm):
    #Asset classes are: bankacc, cash, and stock
    assettype = StringField("Asset Type", validators = [DataRequired()])
    assetname = StringField("Asset Name", validators = [DataRequired()]) 
    assetvalue = FloatField("Asset Value", validators = [DataRequired()])
    assetprice = FloatField("Asset Price", validators = [DataRequired()])
    doa = StringField("Date of Acquisition", validators = [DataRequired()])


#Forms for Settings
class SettingNameForm(FlaskForm):
    name = StringField("Full Name", validators = [DataRequired()])
    submit = SubmitField("Confirm Name")

class SettingEmailForm(FlaskForm):
    email = StringField("Email Address", validators = [DataRequired(), Email()])
    submit = SubmitField("Confirm Email")
    def validate_email(self, email):
        #check if email is already registered
        user = Users.query.filter_by(email = email.data).first()
        if user:
            raise ValidationError("This email is already taken.")

class SettingPhoneForm(FlaskForm):
    phone = StringField('Phone Number', validators=[DataRequired()])
    submit = SubmitField("Confirm Phone")
    def validate_phone(self, phone):
        #check if email is already registered
        user = Users.query.filter_by(phone = phone.data).first()
        if user:
            raise ValidationError("This phone number is already taken.")

class SettingDOBForm(FlaskForm):
    birthday = DateField("Date of Birth", validators=[DataRequired()])
    submit = SubmitField("Confirm Birthday")

