from datetime import date
from flask_wtf import FlaskForm
from countries import CountrySelectField
from wtforms import StringField, SubmitField, EmailField, PasswordField, TextAreaField, DateField, BooleanField, SelectField
from wtforms.validators import InputRequired, Length,EqualTo,Regexp

class UserForm(FlaskForm):
    firstName = StringField("Write your given name:", validators=[InputRequired(),Length(min=2, max=30)])
    lastName = StringField("Write your family name:", validators=[InputRequired(),Length(min=2, max=30)])
    email = EmailField("Write Your Email:",validators=[InputRequired()])
            
    validateEmail = EmailField("Confirm Your Email:",validators=[InputRequired(),EqualTo(fieldname="email")])
    phone = StringField("Phone Number: ", validators=[Regexp("^\+\d{1,3}[\-\s]?\d{2,4}[\-\s]?\d{2,4}[\-\s]?\d{2,4}[\-\s]?\d{2,4}$")])
    mensaID = StringField("Write Your Mensa ID", validators=[Regexp("^([9]\d|20[01]\d|202[0-4])\d{3}$")])
    birthday = DateField("Date of Birth", validators=[InputRequired()])
    snoring = BooleanField('Do you snore?')
    submit = SubmitField('Submit')
    diet = SelectField(u'Diet:', choices=['None','Vegan', 'Other'])
    otherdiet = TextAreaField("Other:")
    country = CountrySelectField("Country of residence:", default='DK', validators=[InputRequired()])
    password = PasswordField("Write Your Password:",validators=[InputRequired(),Length(min=10)])
    validatePassword = PasswordField("Confirm Your Password:",validators=[InputRequired(),EqualTo(fieldname="password",message="Passwords must be equal")])

    submit = SubmitField("Sign Up")