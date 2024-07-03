from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField, PasswordField
from wtforms.validators import InputRequired, Length

class UserForm(FlaskForm):
    name = StringField("Write your name:", validators=[InputRequired(),Length(min=2, max=30)])
    #email = StringField("Write Your Email:",validators=[InputRequired()])
    
    #password = PasswordField("Write Your Password:",validators=[Length(min=10)])

    submit = SubmitField("Sign Up")